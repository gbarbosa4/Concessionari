from django.contrib import admin
from iConcessionari.models import Client
from iConcessionari.models import Factory
from iConcessionari.models import Comercial
from iConcessionari.models import Car
admin.site.register(Client)
admin.site.register(Factory)
admin.site.register(Comercial)
admin.site.register(Car)
