from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from cart.forms import CartAddProductForm
from django.views import View
from blog.models import Blog
from django.core.mail import send_mail
import telebot
from .forms import ApplicationsForm
from django.views.generic import ListView


bot = telebot.TeleBot("1260971143:AAEVskAqdKb_rMMBfST-4WwQsqeOtNiu9Og")


def index(request):
    return render(request, 'shop/index.html')


def my_account(request):
	return render(request, 'shop/account.html')

def shopping(request):
	return render(request, 'cart/shopping-cart.html')

def checkout(request):
	return render(request, 'shop/checkout.html')

def contact(request):
    form = ApplicationsForm()
    return render(request, 'shop/contact.html', {'form': form})


def wishlist(request):
	return render(request, 'shop/wishlist.html')

def detail(request):
	return render(request, 'shop/product-details.html')			

def shop(request):
    product = Product.objects.all()
    cart_product_form = CartAddProductForm()
    context = {'cart_product_form': cart_product_form, 
                'producent': product,   
    }
    return render(request, 'shop/shop.html', context)

def blog(request):
    blog = Blog.objects.all()
    context = {
        'blog': blog,
    }
    return render(request, 'blog/blog.html', context)

class ApplicationsView(View):
    def post(self, request):
        if request.method == 'POST':
            form = ApplicationsForm(request.POST)
            # print(request.POST)
        if form.is_valid():
            form.save()
            mail = form.cleaned_data['mail']
            name = form.cleaned_data['name']
            comment = form.cleaned_data['comment']
            subject = 'Новая заявка!'
            from_email = 'kiroskost@gmail.com'
            to_email = ['kiroskost@gmail.com', 'kirosbush@gmail.com']
            message = 'Новая заявка!' + '\r\n' + '\r\n' + 'Почта: ' + mail + '\r\n' + '\r\n' + 'Имя:' + name + '\r\n' + 'Коммент' + comment
            send_mail(subject, message, from_email, to_email, fail_silently=False)
            bot.send_message(628980737, message)
        return redirect('shop:contact')
