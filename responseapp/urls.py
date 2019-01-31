# from django.urls import path
from django.conf.urls import url
from django.contrib import admin


from responseapp import views as responseapp_views

urlpatterns = [

 url('response/', responseapp_views.responseform),
 url('thankyou/', responseapp_views.responseform),

path('', admin.site.urls),
]
