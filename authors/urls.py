from django.urls import path
from . import views

app_name = 'ng'

urlpatterns = [
    path('registro/', views.register_view, name='registro'),
    path('registro/criar/', views.register_create, name='criar_registro'),
    path('login/', views.login_view, name='login'),
    path('login/criar/', views.login_create, name='criar_login'),
    path('logout/', views.logout_view, name='logout'),
]
