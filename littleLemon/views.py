from django.http import HttpResponse

def menu_items(request, dish):
    # Dictionary of dishes and their descriptions
    items = {
        'pasta': 'A delicious Italian dish made with noodles and sauce.',
        'falafel': 'A crispy deep-fried ball made from ground chickpeas.',
        'cheesecake': 'A sweet dessert consisting of a creamy cheese filling on a biscuit base.'
    }

    # Get the description of the requested dish, or show "Item not found"
    description = items.get(dish, "Item not found!")

    # Return an HTTP response with the dish name and description
    return HttpResponse(f"<h1>{dish.capitalize()}</h1><p>{description}</p>")
