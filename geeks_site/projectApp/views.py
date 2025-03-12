from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

user_data = {
    1: {'name': 'Alice', 'email': 'alice@example.com'},
    2: {'name': 'Bob', 'email': 'bob@example.com'},
    3: {'name': 'Charlie', 'email': 'charlie@example.com'},
}

def index(request):
    return HttpResponse("Hello Geeks this is the app")

def simple_response_view(request):
    return HttpResponse("This is a simple response.")

def user_id (request, user_id):
    user = user_data.get(user_id) #get user data based on user_id
    if user:
        response = f"User ID: {user_id}<br>"
        response += f"Name: {user['name']}<br>"
        response += f"Email: {user['email']}"
        return HttpResponse(response)
    else:
        return HttpResponse("User not found.")