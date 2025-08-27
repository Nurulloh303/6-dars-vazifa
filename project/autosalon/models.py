from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Car(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    year = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    def __str__(self):
        return self.title