from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_login, name='post_login'),
    path('menu', views.post_menu, name='post_menu'),
    path('menu_cliente', views.post_menu_cliente, name='post_menu_cliente'),
]