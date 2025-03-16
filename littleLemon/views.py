from django.shortcuts import render
from django.http import HttpResponse

def menu_items(request, dish):
    return HttpResponse(f"Dish: {dish}")
