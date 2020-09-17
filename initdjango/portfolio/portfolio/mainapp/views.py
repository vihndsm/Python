from django.shortcuts import render
from .models import Portfolio
def index(request):
    port = Portfolio.objects.all()
    return render(request, 'mainapp/index.html', {'portfolio': port})