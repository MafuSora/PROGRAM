# 2
from django.urls import path
from . import views
from . import api

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
    path('', views.mafualbum1_page),
    path('mafualbum2/', views.mafualbum2_page),
    path('shop/laptop/list/', views.shop_laptop_list),

    path('api/category/get-all/', api.get_categories),
    path('api/product/get-all/', api.get_products),
    path('api/category/create/', api.create_categories),
    path('api/review/create/', api.create_review),
    path('api/dummy/', api.dummy),
    path('hello/', views.landing_page),
]
