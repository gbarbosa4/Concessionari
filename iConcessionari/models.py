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
    def __unicode__(self):
        return self.city+" - "+self.address+" - "+str(self.production)+" - "+str(self.stock)

class Comercial(models.Model):
    user = models.ForeignKey(User, unique=True)
    company_id = models.TextField(max_length=100)
    #name = models.TextField(max_length=100)
    city = models.TextField(max_length=100)
    address = models.TextField(max_length=100)
    telephone = models.IntegerField()
    dni = models.TextField(max_length=9)
    sells = models.IntegerField()
    factory = models.ManyToManyField(Factory)
    def __unicode__(self):
        return self.city+" - "+self.address+" - "+self.dni

class Client(models.Model):
    user = models.ForeignKey(User, unique=True)
    #name = models.TextField(max_length=100)
    city = models.TextField(max_length=100)
    address = models.TextField(max_length=100)
    telephone = models.IntegerField()
    dni = models.TextField(max_length=9)
    comercial = models.ForeignKey(Comercial)
    def __unicode__(self):
        return self.city+" - "+self.address+" - "+self.dni

class Car(models.Model):
    brand = models.TextField(max_length=30)
    model = models.TextField(max_length=30)
    price = models.IntegerField()
    car_id = models.IntegerField()
    client = models.ForeignKey(Client)
    comercial = models.ForeignKey(Comercial)
    factory = models.ForeignKey(Factory)
    def __unicode__(self):
        return self.brand+" - "+self.model+" - "+str(self.price)

