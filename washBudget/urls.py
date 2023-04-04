from django.urls import path
from . import views

# "link:home"
app_name = "link"

urlpatterns = [
    path('', views.home, name="home"),
    path('orcamento_sofa/', views.orcamento_sofa, name='orcamento_sofa'),
]