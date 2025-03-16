from django.http import HttpResponseNotFound
from django.shortcuts import render

def handler404(request, exception):
    return HttpResponseNotFound("<h1>404 - Page Not Found</h1><p>Sorry, the page you requested does not exist.</p>")
