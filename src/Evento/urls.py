from django.urls import path
from .views import  eventos

app_name = 'Evento'

urlpatterns = [

    path('', eventos, name='list_eventos'),
]
