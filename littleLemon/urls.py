from django.urls import path
from . import views  # Import views

urlpatterns = [
    path('', views.homepage, name='homepage'),  # Root URL
    path('say-hello/', views.say_hello, name='say_hello'),
    path('display-date/', views.display_date, name='display_date'),
    path('menu/', views.menu, name='menu'),
]
