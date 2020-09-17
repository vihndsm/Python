from django.shortcuts import render
from .models import Portfolio


def index(request):
    portfolio = Portfolio.objects.all()
    return render(request, 'mainapp/index.html', {'port': portfolio})


def indexinner(request):
    return render(request, 'mainapp/inner-page.html')