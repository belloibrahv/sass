from django.contrib import admin
from django.urls import path

from .views import hello_home_page

urlpatterns = [
    path('', hello_home_page),
    path('admin/', admin.site.urls),
]
