from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

user_data = {
    1: {'name': 'Alice', 'email': 'alice@example.com'},
    2: {'name': 'Bob', 'email': 'bob@example.com'},
    3: {'name': 'Charlie', 'email': 'charlie@example.com'},
}

def index(request):
    return render(request, 'my_template.html')

def simple_response_view(request):
    return HttpResponse("This is a simple response.")

def Single_user (request, user_id):
    user = user_data.get(user_id) #get user data based on user_id
    
    context = {
        'user_id' : user_id,
        'user_name' : user['name'],
        'user_email': user['email'],
    }
    return render(request, 'my_template.html', context)
    

def multiple_users(request, user_ids):
    user_ids_list = user_ids.split(',')
    users=[]
    for  user_ids_str in user_ids_list:
        try:
            user_id = int(user_ids_str)
            user = user_data.get(user_id)
            if user:
                users.append({
                    'user_id': user_id,
                    'user_name': user['name'],
                    'user_email': user['email'],
                })
            else:
                users.append({
                    'user_id': user_id,
                    'error': 'User not found.',
                })
        except ValueError:
            users.append({'error': f'Invalid user ID: {user_id_str}'})
    context = {'users': users}
    return render(request, 'my_template.html', context) 
            
        
   
    