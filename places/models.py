from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(
        'Название',
        unique=True,
        max_length=200,
    )

    short_description = models.TextField(
        'Краткое описание',
        blank=True,
    )

    long_description = HTMLField(
        'Полное описание',
        blank=True,
    )

    lng = models.DecimalField(
        'Долгота',
        max_digits=22,
        decimal_places=16,
    )

    lat = models.DecimalField(
        'Широта',
        max_digits=22,
        decimal_places=16,
    )

    class Meta:
        verbose_name = 'место'
        verbose_name_plural = 'места'

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(
        'Place',
        on_delete=models.CASCADE,
        related_name='images'
    )

    image = models.ImageField('Изображение')

    position = models.IntegerField('Позиция', default=1, db_index=True, blank=True)

    class Meta:
        verbose_name = 'изображение'
        verbose_name_plural = 'изображения'
        ordering = ('position',)

    def __str__(self):
        return self.image.name
