
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('about', views.about, name='sobre min'),
    path('contacts', views.contacts, name='contacts')

]