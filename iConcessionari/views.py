# Create your views here.

from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from iConcessionari.models import Car,Factory,Comercial,Client
from django.core import serializers


def save(request):

    template = get_template('mainpage.html')
    variables = Context({
        'titlehead': 'Concessionari app',
        'pagetitle': 'Welcome to the Concessionari aplication',
        'contentbody': 'A new page made by Guillem Barbosa, Denis Casajus and Joan Marc Capell since 2014',
        'main':'false',
    })
    output = template.render(variables)
    return HttpResponse(output)

def newpage(request):
    template = get_template('mainpage.html')
    variables = Context({
        'titlehead': 'Concessionari app',
        'pagetitle': 'Welcome to the Concessionari aplication',
        'contentbody': 'A new page made by Guillem Barbosa, Denis Casajus and Joan Marc Capell since 2014',
        'main':'false',
    })
    output = template.render(variables)
    return HttpResponse(output)


def mainpage(request):
    template = get_template('mainpage.html')
    variables = Context({
        'titlehead': 'Concessionari app',
        'pagetitle': 'Welcome to the Concessionari aplication',
        'contentbody': 'A new page made by Guillem Barbosa, Denis Casajus and Joan Marc Capell since 2014',
        'user': request.user,
        'main':'true',
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
        raise Http404('Car not found.')
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

def factory_info(request,f_id):
    try:
        Comercial.objects.get(user=request.user)
    except:
        raise Http404('No authoritzated to do this')

    try:
        factory = Factory.objects.get(Factory_id=f_id)
    except:
        raise Http404('Factory not found.')
    template = get_template('factory_info.html')
    variables = Context({
        'factory': factory,
    })
    output = template.render(variables)
    return HttpResponse(output)    
    

def userpage(request):
    try:
        comercial = Comercial.objects.get(user=request.user)
        template = get_template('comercial_info.html')
        variables = Context({
            'user': comercial,
        })
        output = template.render(variables)
        return HttpResponse(output)    
    except:
        try:
            user = Client.objects.get(user=request.user)
        except:
            raise Http404('User not found.')
        template = get_template('userpage.html')
        variables = Context({
            'user': user,
        })
        output = template.render(variables)
        return HttpResponse(output)

def comercials_page(request):
    template = get_template('comercials_page.html')
    comercials = Comercial.objects.all()
    variables = Context({
        'comercials': comercials,
    })
    output = template.render(variables)
    return HttpResponse(output)

#json i xml

def jx_cars_page(request,jx):
    data = serializers.serialize(jx, Car.objects.all())
    return HttpResponse(data)

def jx_car_info(request,jx,c_id):
    print Car.objects.get(car_id=c_id)
    try:
        data = serializers.serialize(jx, [Car.objects.get(car_id=c_id)])
    except:
        raise Http404('Car not found.')
    return HttpResponse(data)

def jx_factory_page(request,jx):

    data = serializers.serialize(jx, Factory.objects.all())
    return HttpResponse(data)

def jx_factory_info(request,jx,f_id):
    try:
        Comercial.objects.get(user=request.user)
    except:
        raise Http404('No authoritzated to do this')
    try:
        data = serializers.serialize(jx, [Factory.objects.get(Factory_id=f_id)])
    except:
        raise Http404('Factory not found.')
    return HttpResponse(data)

def jx_userpage(request,jx):
    try:
        data = serializers.serialize(jx, Comercial.objects.get(user=request.user))
        return HttpResponse(data)
    except:
        try:
            data = serializers.serialize(jx, [Client.objects.get(user=request.user)])
        except:
            raise Http404('User not found.')
        return HttpResponse(data)



def jx_comercials_page(request,jx):
    try:
        data = serializers.serialize(jx, Comercial.objects.all())
    except:
        raise Http404('Car not found.')
    return HttpResponse(data)










