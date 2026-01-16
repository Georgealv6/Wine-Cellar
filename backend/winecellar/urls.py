from django.urls import path
from . import views

app_name = "wine cellar"

urlpatterns = [
    path('', views.welcomepage, name='welcome'),
    path('home/', views.homepage , name='home'),
    path('contact/', views.contactpage , name='contact'),
    path('aboutus/', views.AboutUsPage , name='about-us'),
    path('login/', views.loginpage, name='login'),
]