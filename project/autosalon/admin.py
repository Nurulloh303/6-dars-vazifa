from django.contrib import admin
from .models import Brand, Car, Comment
from django.utils.safestring import mark_safe


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    readonly_fields = ('text', "user")
    can_delete = False


class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'brand', 'year', 'price', 'created', 'updated', 'get_image')

    search_fields = ('title', 'brand__name')

    list_display_links = ( 'title',)

    list_filter = ('brand', 'year')

    list_editable = ("brand", "year")

    def get_image(self, car):
        if car.image:
            return mark_safe(f'<img src="{car.image.url}"; width="150px" />')
        else:
            return '---'

    get_image.short_description = 'Rasmi'


admin.site.register(Brand)
admin.site.register(Car, CarAdmin)
