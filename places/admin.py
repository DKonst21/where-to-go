from django.contrib import admin
from django.utils.html import format_html, mark_safe
from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminMixin, SortableAdminBase, SortableInlineAdminMixin

from .models import Place, Image


class PreviewMixin(object):
    def preview(self, image):
        url = image.image.url
        return format_html('<img src="{}" style="max-height: 200px;">', url)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin, PreviewMixin):
    fields = (
        'place',
        'image',
        'position',
        'preview',
    )

    readonly_fields = ('preview',)


class ImageInline(SortableInlineAdminMixin, admin.StackedInline):
    extra = 1
    ordering = ['position']
    model = Image
    readonly_fields = ['place_image']
    fields = ['image', 'place_image']

    def place_image(self, image):
        return format_html('<img src={} style="max-height: {height}px">',
                           image.image.url,
                           height=200)

    place_image.short_description = 'Превью'


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    fields = (
        'title',
        'short_description',
        'long_description',
        'lng',
        'lat',
    )
    inlines = [ImageInline,]
    search_fields = ['title']