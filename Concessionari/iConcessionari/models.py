from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Factory(models.Model):
	Factory_id = models.TextField(max_length=100)
	city = models.TextField(max_length=100)
	address = models.TextField(max_length=100)
	telephone = models.IntegerField()
	production = models.IntegerField()
	stock = models.IntegerField()

class Comercial(User):
	company_id = models.TextField(max_length=100)
	name = models.TextField(max_length=100)
	city = models.TextField(max_length=100)
	address = models.TextField(max_length=100)
	telephone = models.IntegerField()
	dni = models.TextField(max_length=9)
	sells = models.IntegerField()
	factory = models.ManyToMany(Factory)

class Client(User):
	name = models.TextField(max_length=100)
	city = models.TextField(max_length=100)
	address = models.TextField(max_length=100)
	telephone = models.IntegerField()
	dni = models.TextField(max_length=9)
	comercial = models.ForeignKey(Comercial)

class Car(models.Model):
	brand = models.TextField(max_length=30)
	model = models.TextField(max_length=30)
	price = models.IntegerField()
	car_id = models.IntegerField()
	client = models.ForeignKey(Client)
	comercial = models.ForeignKey(Comercial)
	factory = models.ForeignKey(Factory)


	


