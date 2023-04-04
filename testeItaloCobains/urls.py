from django.urls import path
from . import views

app_name = 'teste'

urlpatterns = [
        path('produto/edit/<int:produto_id>/', views.edit_sofa, name="edit_produto"),
        path('produto/list/', views.produto_list, name="produto_list"),
        path('produto/create/', views.create_sofa, name='create_sofa'),
        path('produto/delete/<int:produto_id>/', views.delete_sofa, name='delete_sofa')
        ]
