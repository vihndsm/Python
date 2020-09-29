from django.urls import path, include
from .views import *
from . import views

app_name = 'shop'

urlpatterns = [
    path('', index),
    path('shop/', views.shop, name='shop'),
    path('my_account/', views.my_account, name='my_account'),
    path('shopping/', views.shopping, name='shopping'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('product/', views.product, name='product'),
    path('<slug:category_slug>/', views.shopping, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_details, name='product_detail'),
]