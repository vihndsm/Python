from django.shortcuts import render, get_object_or_404
from .models import *
# from cart.forms import CartAddProductForm
from django.views import View



# def blog(request):
# 	return render(request, 'blog/blog.html')

def blog(request):
	product = Product.objects.all()
	return render(request, 'blog/blog.html', {'blog': blog})	

