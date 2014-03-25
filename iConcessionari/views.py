# Create your views here.

from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from iConcessionari.models import Car,Factory,Comercial,Client


def newpage(request):
    template = get_template('mainpage.html')
    variables = Context({
        'titlehead': 'Concessionari app',
        'pagetitle': 'Welcome to the Concessionari aplication',
        'contentbody': 'A new page made by Guillem Barbosa, Denis Casajus and Joan Marc Capell since 2014',
    })
    output = template.render(variables)
    return HttpResponse(output)


def mainpage(request):
    template = get_template('mainpage.html')
    variables = Context({
        'titlehead': 'Concessionari app',
        'pagetitle': 'Welcome to the Concessionari aplication',
        'contentbody': 'A new page made by Guillem Barbosa, Denis Casajus and Joan Marc Capell since 2014',
        'user': request.user
    })
    output = template.render(variables)
    return HttpResponse(output)
    
def cars_page(request):
    
    template = get_template('cars_page.html')
    cars = Car.objects.all()
    variables = Context({
        'cars': cars,
    })
    output = template.render(variables)
    return HttpResponse(output)

def car_info(request,c_id):
    try:
        car = Car.objects.get(car_id=c_id)
    except:
        raise Http404('User not found.')
    template = get_template('car_info.html')
    variables = Context({
        'car': car,
    })
    output = template.render(variables)
    return HttpResponse(output)

def factory_page(request):
    
    template = get_template('factory_page.html')
    factories = Factory.objects.all()
    variables = Context({
        'factories': factories,
    })
    output = template.render(variables)
    return HttpResponse(output)    

def userpage(request, user):
    try:
        client = User.objects.get(username=user)
    except:
        raise Http404('User not found.')
    template = get_template('userpage.html')
    variables = Context({
        'user': client
    })
    output = template.render(variables)
    return HttpResponse(output)
