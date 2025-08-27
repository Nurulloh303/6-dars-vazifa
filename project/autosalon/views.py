from django.shortcuts import render

from .models import Brand, Car

def home(request):
    brands = Brand.objects.all()
    cars = Car.objects.all()

    context = {
        'brands': brands,
        'cars': cars,
        "title": "Asosiy menu",
    }

    return render(request, 'autosalon/index.html', context)

def brand_by_car(request, brand_id: int):
    brands = Brand.objects.all()
    cars = Car.objects.filter(brand_id=brand_id)

    context = {
        'brands': brands,
        'cars': cars,
        "title": Brand.objects.get(pk=brand_id).name
    }


    return render(request, 'autosalon/index.html', context)


def car_detail(request, pk: int):
    car = Car.objects.get(pk=pk)
    brands = Brand.objects.all()

    context = {
        'car': car,
        'brands': brands,

    }

    return render(request, 'autosalon/detail.html', context)