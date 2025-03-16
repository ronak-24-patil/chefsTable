from django.http import HttpResponse
import datetime

def homepage(request):
    return HttpResponse("<h1>Welcome to Little Lemon</h1><p>This is the homepage.</p>")

# View 1: Return "Hello World"
def say_hello(request):
    return HttpResponse("Hello World")

# View 2: Return "Welcome to Little Lemon"
def homepage(request):
    return HttpResponse("Welcome to Little Lemon")

# View 3: Display the current year using the datetime module
def display_date(request):
    date_joined = datetime.datetime.now().year
    return HttpResponse(f"Current Year: {date_joined}")

# View 4: Return a simple HTML page with styling
def menu(request):
    html_content = """
    <html>
    <head><title>Menu</title></head>
    <body style="background-color:lightblue; text-align:center;">
        <h1 style="color:green;">Welcome to Our Menu</h1>
        <p>Enjoy delicious meals at Little Lemon!</p>
    </body>
    </html>
    """
    return HttpResponse(html_content)
