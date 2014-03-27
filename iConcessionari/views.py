# Create your views here.
from django.shortcuts import render,RequestContext,render_to_response
from django.http import HttpResponse, Http404
from django.http import HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from iConcessionari.models import Car,Factory,Client
from django.core import serializers

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from forms import  UserCreateForm,UserForm

from django.shortcuts import render_to_response, get_object_or_404
from django.core import urlresolvers
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm

 

@login_required
def editar_perfil(request):

    if request.method == 'POST':
        # formulario enviado
        user_form = UserForm(request.POST, instance=request.user)


        if user_form.is_valid():
            # formulario validado correctamente
            user_form.save()
            return HttpResponseRedirect('/mainpage')

    else:
        # formulario inicial
        user_form = UserForm(instance=request.user)
        

    return render_to_response('user_page.html', { 'user_form': user_form}, context_instance=RequestContext(request))

def new_user(request):
    if request.method=='POST':
        formulario = UserCreateForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = UserCreateForm()
    return render_to_response('new_user.html',{'formulario':formulario},context_instance=RequestContext(request))

def save(request,formulario):
    print formulario.user
    Client.objects.set_user(formulario.user)
    template = get_template('mainpage.html')
    variables = Context({
        'titlehead': 'Concessionari app',
        'pagetitle': 'Welcome to the Concessionari aplication',
        'contentbody': 'A new page made by Guillem Barbosa, Denis Casajus and Joan Marc Capell since 2014',
        'main':'false',
    })
    output = template.render(variables)
    return HttpResponse(output)

def new_page(request):
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
        car = Car.objects.get(id=c_id)
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
        factory = Factory.objects.get(id=f_id)
    except:
        raise Http404('Factory not found.')
    template = get_template('factory_info.html')
    variables = Context({
        'factory': factory,
    })
    output = template.render(variables)
    return HttpResponse(output)    
    
def clients_page(request):
    template = get_template('clients_page.html')
    clients = Client.objects.all()
    variables = Context({
        'clients': clients,
    })
    output = template.render(variables)
    return HttpResponse(output)

def client_page_info(request,f_id):
    try:
        client = Client.objects.get(id=f_id)
    except:
        raise Http404('Client not found.')
    template = get_template('client_page_info.html')
    variables = Context({
        'client': client,
    })
    output = template.render(variables)
    return HttpResponse(output)

def userpage(request):
    try:
        user = User.objects.get(username=request.user)
    except:
        raise Http404('User not found.')
    template = get_template('user_page_info.html')
    variables = Context({
        'user': user,
    })
    output = template.render(variables)
    return HttpResponse(output)


def comercials_page(request):
    template = get_template('comercials_page.html')
    comercials = User.objects.all()
    variables = Context({
        'comercials': comercials,
    })
    output = template.render(variables)
    return HttpResponse(output)

#json i xml

def jx_cars_page(request,jx):
    data = serializers.serialize(jx, Car.objects.all())
    return HttpResponse(data,mimetype="application/"+jx)

def jx_car_info(request,jx,c_id):

    try:
        data = serializers.serialize(jx, [Car.objects.get(id=c_id)])
    except:
        raise Http404('Car not found.')
    return HttpResponse(data,mimetype="application/"+jx)

def jx_factory_page(request,jx):

    data = serializers.serialize(jx, Factory.objects.all())
    return HttpResponse(data,mimetype="application/"+jx)

def jx_factory_info(request,jx,f_id):
    try:
        data = serializers.serialize(jx, [Factory.objects.get(username=request.user)])
    except:
        raise Http404('Factory not found.')
    return HttpResponse(data,mimetype="application/"+jx)

def jx_clients_page(request,jx):

    data = serializers.serialize(jx, Client.objects.all())
    return HttpResponse(data,mimetype="application/"+jx)

def jx_client_info(request,jx,f_id):
    try:
        data = serializers.serialize(jx, [Client.objects.get(username=request.user)])
    except:
        raise Http404('Client not found.')
    return HttpResponse(data,mimetype="application/"+jx)

def jx_userpage(request,jx):
    try:
        data = serializers.serialize(jx, [User.objects.get(username=request.user)])
    except:
        raise Http404('No authorizated to do this or user not found.')
    return HttpResponse(data,mimetype="application/"+jx)

def jx_comercials_page(request,jx):
    data = serializers.serialize(jx, User.objects.all())
    return HttpResponse(data,mimetype="application/"+jx)










