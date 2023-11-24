from django.urls import path, include
from . import views

urlpatterns = [
        path('', views.pe_profile, name='index'),
]
