from django.contrib import admin
from django.urls import path, include

# from .views import poka

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    # path('poka/', poka),
]
