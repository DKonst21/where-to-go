import logging

import requests
from django.core.exceptions import MultipleObjectsReturned
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Place, Image


def load_place_image(place, num, url):
    try:
        logging.info(f'downloading image from url: {url}')
        response = requests.get(url)
        response.raise_for_status()

        Image.objects.create(
            place=place,
            position=num,
            image=ContentFile(response.content, name=f'{num} {place}')
        )
    except requests.HTTPError:
        logging.info('Не удалось загрузить изображение')
    except MultipleObjectsReturned:
        logging.info('Существует больше одного места с таким названием')


def add_place(serialized_place):
    try:
        title = serialized_place['title']

        place_descriptions = {
            'description_short': serialized_place.get('description_short', ''),
            'description_long': serialized_place.get('description_long', ''),
            'lng': serialized_place['coordinates']['lng'],
            'lat': serialized_place['coordinates']['lat'],
        }
    except KeyError as undefined_key:
        logging.error(f'Не хватает обязательного аргумента {undefined_key}')
        return

    place, created = Place.objects.get_or_create(
        title=title,
        defaults=place_descriptions
    )
    if not created:
        return

    images_urls = serialized_place.get('imgs', [])
    for num, url in enumerate(images_urls, start=1):
        load_place_image(place, num, url)


class Command(BaseCommand):
    help = 'Loading place to db from url with json'

    def handle(self, *args, **options):
        try:
            url = options['url']
            logging.info(f'downloading json from url: {url}')
            response = requests.get(url)
            response.raise_for_status()

            serialized_place = response.json()

            add_place(serialized_place)
        except requests.HTTPError:
            logging.info('Ошибка загрузки. Проверьте ссылку')

    def add_arguments(self, parser):
        parser.add_argument('url')