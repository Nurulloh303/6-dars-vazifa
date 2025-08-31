from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name="Brand nomi")
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brandlar"


class Car(models.Model):
    title = models.CharField(max_length=100, verbose_name="Mashina nomi")
    description = models.TextField(null=True, blank=True, verbose_name="Mashina ma'lumoti")
    year = models.IntegerField(verbose_name="Ishlab chiqarilgan yili")
    published = models.BooleanField(default=0, verbose_name="Saytga chiqarish")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqti")
    updated = models.DateTimeField(auto_now=True, verbose_name="Yangilangan vaqti")
    image = models.ImageField(upload_to='image/', null=True, blank=True, verbose_name="Rasmi")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Narxi")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE,  verbose_name="Brand")
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Mashina"
        verbose_name_plural = "Mahinalar"


class Comment(models.Model):
    text = models.CharField(max_length=500, verbose_name="Matni")
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name="Maqola")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Aftor")
    created =models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqti")

    def __str__(self):
        return self.user.username


    class Meta:
        verbose_name_plural = "Izohlar"
        ordering = ['-created']
