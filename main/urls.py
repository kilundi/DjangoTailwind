from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.main, name='home'),
    path('base', views.base, name='base'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
]
