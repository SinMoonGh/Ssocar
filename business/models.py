from django.db import models

# Create your models here.
class Car (models.Model):
    car_name = models.CharField(max_length=200)


class Customer (models.Model):
    customer_name = models.CharField(max_length=200)


class Rental (models.Model):
    car_name = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer_name = models.ForeignKey(Customer, on_delete=models.CASCADE)
    rental_date = models.DateField('rental date')
    price = models.IntegerField()
