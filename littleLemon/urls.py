from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),  # Root URL (fixes 404 error)
    path('say-hello/', views.say_hello, name='say_hello'),
    path('display-date/', views.display_date, name='display_date'),
    path('menu/', views.menu, name='menu'),
]
