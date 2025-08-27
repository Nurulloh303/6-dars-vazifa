from django.contrib import admin
from .models import Brand, Car


class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'brand', 'year', 'price', 'created', 'updated')

    search_fields = ('title', 'brand__name')

    list_filter = ('brand', 'year')

    fields = ('title', 'description', 'brand', 'year', 'price', 'image')


admin.site.register(Brand)
admin.site.register(Car, CarAdmin)
