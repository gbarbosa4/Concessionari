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

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', newpage, name='home'),
    url(r'^mainpage', mainpage),
    url(r'^user/$', userpage),
    url(r'^login/$','django.contrib.auth.views.login'),
    url(r'^cars_page/$',cars_page),
    url(r'^cars_page/(\w+)/$',car_info),
    url(r'^factory_page/$',factory_page),
    url(r'^factory_page/(\w+)/$',factory_info),
    url(r'^Log_Out/$',newpage),
    url(r'^comercials_page/$',comercials_page),
    url(r'^save/$',save),


    url(r'^(\w+)/user/$', jx_userpage),
    url(r'^(\w+)/cars_page/$',jx_cars_page),
    url(r'^(\w+)/cars_page/(\w+)/$',jx_car_info),
    url(r'^(\w+)/factory_page/$',jx_factory_page),
    url(r'^(\w+)/factory_page/(\w+)/$',jx_factory_info),
    url(r'^(\w+)/comercials_page/$',jx_comercials_page),

)
