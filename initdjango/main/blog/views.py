from django.shortcuts import render
from models import Post

def hello(request):
    post = Post
    return render(request, 'blog/index.html', context={'names': post})
# Create your views here.
