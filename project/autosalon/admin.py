from django.contrib import admin

# Register your models here.
from .models import Brand, Car

admin.site.register(Brand)
admin.site.register(Car)