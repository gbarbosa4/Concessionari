from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class Factory(models.Model):
    city = models.TextField(max_length=100)
    address = models.TextField(max_length=100)
    telephone = models.IntegerField()
    production = models.IntegerField()
    stock = models.IntegerField()
    def __unicode__(self):
        return self.city+" - "+self.address+" - "+str(self.production)+" - "+str(self.stock)

#class Comercial(models.Model):
    #user = models.OneToOneField(User)
    #dni = models.TextField(max_length=9)
    #telephone = models.IntegerField()
    #city = models.TextField(max_length=100)
    #address = models.TextField(max_length=100)
    #sells = models.IntegerField()
    #factory = models.ManyToManyField(Factory)
    #def __unicode__(self):
     #   return self.city+" - "+self.address+" - "+self.dni

class Client(models.Model):
    name = models.TextField(max_length=20)
    last_name = models.TextField(max_length=20)
    email = models.TextField(max_length=20)
    dni = models.TextField(max_length=9)
    telephone = models.IntegerField()
    city = models.TextField(max_length=100)
    address = models.TextField(max_length=100)
    def __unicode__(self):
        return self.city+" - "+self.address+" - "+self.dni

class Car(models.Model):
    brand = models.TextField(max_length=30)
    model = models.TextField(max_length=30)
    price = models.IntegerField()
    client = models.ForeignKey(Client)
    factory = models.ForeignKey(Factory)
    def __unicode__(self):
        return self.brand+" - "+self.model+" - "+str(self.price)

