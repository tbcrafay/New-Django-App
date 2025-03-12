from django.urls import path
#now import the views.py file into this code
from . import views
urlpatterns=[
path('',views.index, name='index'),
path('simple/',views.simple_response_view, name="response_view"),
path('user_identification/<int:user_id>', views.user_id, name="user_id")
]
