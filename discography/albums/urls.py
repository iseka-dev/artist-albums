from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_discography, name='get_discography'),
]
