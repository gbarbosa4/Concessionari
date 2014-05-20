from django.conf.urls import patterns, include, url
from iConcessionari.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Concessionari.views.home', name='home'),
    # url(r'^Concessionari/', include('Concessionari.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    #Create new registers
    #url(r'^clients_page/create/$',clients_page),
    #url(r'^cars_page/create/$',cars_page),

    url(r'^factory_page/create/$',FactoryCreate.as_view()),
    url(r'^cars_page/create/$',CarCreate.as_view()),
    url(r'^clients_page/create/$',ClientCreate.as_view()),
    
    url(r'^factory_page/update/(?P<pk>\d+)/$',UpdateFactoryView.as_view(),name='Factory_edit'),
    url(r'^cars_page/update/(?P<pk>\d+)/$',UpdateCarView.as_view(),name='Car_edit'),
    url(r'^clients_page/update/(?P<pk>\d+)/$',UpdateClientView.as_view(),name='Client_edit'),


    url(r'^factory_page/delete/(?P<pk>\d+)/$',DeleteFactoryView.as_view(),name='Factory_delete'),
    url(r'^cars_page/delete/(?P<pk>\d+)/$',DeleteCarView.as_view(),name='Car_delete'),
    url(r'^clients_page/delete/(?P<pk>\d+)/$',DeleteClientView.as_view(),name='Client_delete'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', new_page, name='home'),
    url(r'^mainpage', mainpage),
    url(r'^mainpage/(\w+)/$', save),
    url(r'^user/$', userpage),
    url(r'^user/edit$', editar_perfil),
    url(r'^login/$','django.contrib.auth.views.login'),
    url(r'^clients_page/$',clients_page,name='clients_page'),
    url(r'^clients_page/(\w+)/$',client_page_info),
    url(r'^cars_page/$',cars_page,name='cars_page'),
    url(r'^cars_page/(\w+)/$',car_info),
    url(r'^factory_page/$',factory_page,name='factory_page'),
    url(r'^factory_page/(\w+)/$',factory_info),
    url(r'^Log_Out/$',new_page),
    url(r'^comercials_page/$',comercials_page),
    url(r'^registration/$',new_user),

    



    #JSON and XML
    url(r'^(\w+)/user/$', jx_userpage),
    url(r'^clients_page/$',jx_clients_page),
    url(r'^clients_page/(\w+)/$',jx_client_info),
    url(r'^(\w+)/cars_page/$',jx_cars_page),
    url(r'^(\w+)/cars_page/(\w+)/$',jx_car_info),
    url(r'^(\w+)/factory_page/$',jx_factory_page),
    url(r'^(\w+)/factory_page/(\w+)/$',jx_factory_info),
    url(r'^(\w+)/comercials_page/$',jx_comercials_page),

)
