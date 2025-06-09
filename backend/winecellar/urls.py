from django.urls import path
from . import views

app_name = "wine cellar"

urlpatterns = [
    path('', views.welcomepage, name='welcome'),
    path('home/', views.homepage , name='home'),
    path('conact/', views.contactpage , name='contact'),
]