from django.http import HttpResponse

def home(request):
    # Accessing request attributes
    path = request.path
    scheme = request.scheme
    method = request.method
    address = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']

    # Creating an HTML response
    message = f"""
    <html>
    <head><title>Request Info</title></head>
    <body>
        <h1>Request Details</h1>
        <p><strong>Path:</strong> {path}</p>
        <p><strong>Scheme:</strong> {scheme}</p>
        <p><strong>Method:</strong> {method}</p>
        <p><strong>IP Address:</strong> {address}</p>
        <p><strong>User Agent:</strong> {user_agent}</p>
    </body>
    </html>
    """

    response = HttpResponse(message, content_type="text/html", charset="utf-8")
    
    # Adding custom headers
    response.headers['Age'] = 20
    
    return response
