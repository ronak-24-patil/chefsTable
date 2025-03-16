from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),  # URL for the request-response demo
]
