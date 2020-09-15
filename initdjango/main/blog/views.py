from django.shortcuts import render
from .models import Post

def hello(request):
    post = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': post})
# Create your views here.
