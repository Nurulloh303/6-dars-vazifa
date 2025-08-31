from django.http import HttpRequest
from django.shortcuts import render, redirect
from .forms import CommentForm
from .models import Brand, Car, Comment

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
        "form": CommentForm()
    }

    return render(request, 'autosalon/detail.html', context)

def save_comment(request: HttpRequest, car_id: int):
    if request.method == "POST":
        form = CommentForm(data=request.POST)
        if form.is_valid():
            Comment.objects.create(
                text=request.POST.get("text"),
                car_id=car_id,
                user=request.user
            )
    return redirect("by_car", pk=car_id)
