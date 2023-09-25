from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from places.models import Place


def show_main(request):
    locations = Place.objects.all()
    features = []
    for location in locations:
        features.append(
            {
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
        )

    context = {
        'geojson': {
            'type': 'FeatureCollection',
            'features': features,
        },
    }
    return render(request, 'index.html', context=context)


def view_place(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    images = [image.image.url for image in place.images.all()]
    context = {
        'title': place.title,
        'imgs': images,
        'short_description': place.short_description,
        'long_description': place.long_description,
        'coordinates': {
            'lat': place.lat,
            'lng': place.lng,
        }
    }
    return JsonResponse(context, safe=False, json_dumps_params={'indent': 2, 'ensure_ascii': False})
