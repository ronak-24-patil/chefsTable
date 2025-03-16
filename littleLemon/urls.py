from django.urls import path
from . import views  # Ensure views is imported correctly

urlpatterns = [
    path('dishes/<str:dish>/', views.menu_items, name='menu_items'),  # Ensure menu_items exists
]
