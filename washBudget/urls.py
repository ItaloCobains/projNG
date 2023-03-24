from django.urls import path
from . import views

# "link:home"
app_name = "link"

urlpatterns = [
    path('', views.home, name="home"),
    path('enviar-orcamento/', views.enviarFormSofa, name='orcamento'),
]