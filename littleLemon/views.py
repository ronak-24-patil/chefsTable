from django.http import HttpResponse
from datetime import datetime  # Import datetime module

def say_hello(request):
    return HttpResponse("Hello, Welcome to Little Lemon!")

def homepage(request):
    return HttpResponse("Welcome to the Little Lemon Restaurant")

def display_date(request):
    date_joined = datetime.now().year  # Get the current year
    return HttpResponse(f"The current year is {date_joined}")

def menu(request):
    html_content = """
    <html>
    <head>
        <title>Little Lemon Menu</title>
        <style>
            body { font-family: Arial, sans-serif; }
            h1 { color: green; }
            p { font-size: 18px; }
        </style>
    </head>
    <body>
        <h1>Little Lemon Menu</h1>
        <p>Explore our delicious Mediterranean dishes.</p>
    </body>
    </html>
    """
    return HttpResponse(html_content)
