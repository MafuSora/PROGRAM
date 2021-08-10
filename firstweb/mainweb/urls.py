# 2
from django.urls import path
from . import views

urlpatterns = [
    path('sapa/<str:nama>/', views.sapa),
    path('shop/', views.shop),
    path('shop/laptop/', views.shop_laptop),
    path('shop/smartphone/', views.shop_smartphone),
    path('shop/console/', views.shop_console),
    path('firstpage/', views.first_page),
    path('secondpage/', views.second_page),
    path('count/<int:angka>/', views.count),
    path('htmlcoba/', views.htmlcoba),
    path('second/', views.second_page),
    path('', views.landing_page),
]
