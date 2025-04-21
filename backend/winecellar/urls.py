from django.urls import path
from . import views

app_name = "wine cellar"

urlpatterns = [
    path('', views.welcomepage, name='welcome')
]