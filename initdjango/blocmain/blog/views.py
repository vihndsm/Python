from django.shortcuts import render

def hello(request):
    n = ['Turat', 'Aito', 'Taalai', 'Kirill', 'Umut']
    return render(request, 'blog/index.html', context={'names': n})
# Create your views here.
