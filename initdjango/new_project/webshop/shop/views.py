from django.shortcuts import render, get_object_or_404
from .models import *
from cart.forms import CartAddProductForm


from django.views import View




def index(request):

    return render(request, 'shop/index.html')


def shop(request):
    return render(request, 'shop/shop.html')


def my_account(request):
	return render(request, 'shop/account.html')

def shopping(request):
	return render(request, 'cart/shopping-cart.html')

def checkout(request):
	return render(request, 'shop/checkout.html')

def contact(request):
	return render(request, 'shop/contact.html')	

def blog(request):
	return render(request, 'shop/blog.html')

def wishlist(request):
	return render(request, 'shop/wishlist.html')

def detail(request):

	# productdetail = get_object_or_404(productdetail, pk=pk)
	# context = {
	# 'productdetail': prod
	# }
	return render(request, 'shop/product-details.html')			

def shop(request):
	product = Product.objects.all()
	return render(request, 'shop/shop.html', {'producent': product})	



def category(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/shop.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_details(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product-details.html', {'product': product,
                                                        'cart_product_form': cart_product_form})
