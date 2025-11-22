from django.db import models
from django.contrib import admin
class Car(models.Model):
    brand_name=models.CharField()
    car_name=models.CharField()
    engineum=models.IntField()
    release_date=models.DateField()

class CarAdmin(admin.ModelsAdmin):
        list_display=('brand_name','car_name','engineum','release_date')
# Create your models here.
