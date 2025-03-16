from django.urls import path
from . import views

urlpatterns = [
    path('dishes/<str:dish>/', views.menu_items, name='menu_items'),  
]
