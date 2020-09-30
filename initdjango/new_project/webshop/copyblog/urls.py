from django.urls import path, include
from .views import *
from . import views

app_name = 'blog'



urlpatterns = [
    path('', index),
    path('shop/', views.shop, name='shop'),
    path('my_account/', views.my_account, name='my_account'),
    # path('shopping/', views.shopping, name='shopping'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('', views.blog, name='blog'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('detail/', views.detail, name='detail'),
]