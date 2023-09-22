from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from places.models import Place


def show_main(request):
    locations = Place.objects.all()
    features = []
    for location in locations:
        features = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [float(location.lng), float(location.lat)]
            },
            'properties': {
                'title': location.title,
                'placeId': location.id,
                'detailsUrl': reverse('places', args=[location.id]),
            }
        }
        features.append(features)

    context = {
        'geojson': {
            'type': 'FeatureCollection',
            'features': features,
        },
    }
    return render(request, 'index.html', context=context)


def place_view(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    context = {
        'title': place.title,
        'imgs': [image.image.url for image in place.images.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lat': place.lat,
            'lng': place.lng,
        }
    }
    return JsonResponse(context, safe=False, json_dumps_params={'indent': 2, 'ensure_ascii': False})
