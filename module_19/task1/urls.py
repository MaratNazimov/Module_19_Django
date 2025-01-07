from django.urls import path
from . import views



urlpatterns = [
    path('main_page/', views.main_page, name='main_page'),
    path('shop/', views.shop, name='shop'),
    path('basket/', views.basket, name='basket'),
    path('base_menu/', views.base_menu, name='base_menu'),
    path('registration_page', views.form_register, name='registration_page'),
    path('bd_buyer/', views.bd_buyer, name='bd_buyer'),
    path('', views.authorization_user, name='authorization_user'),
    path('platform/news/', views.news, name='news'),
]


