from django.urls import path
from . import views

app_name = "wine_cellar"

urlpatterns = [
    path('', views.welcomepage, name='welcome'),
    path('home/', views.homepage , name='home'),
    path('contact/', views.Contact , name='contact'),
    path('aboutus/', views.AboutUs , name='about-us'),
    path('login/', views.Login, name='login'),
    path('blog/', views.Blog, name='blog'),
]