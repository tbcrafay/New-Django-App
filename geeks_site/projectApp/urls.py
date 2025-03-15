from django.urls import path
from django.urls import re_path

#now import the views.py file into this code
from . import views
urlpatterns=[
path('',views.index, name='index'),
path('simple/',views.simple_response_view, name="response_view"),
path('single_user/<int:user_id>', views.Single_user, name="single_user"),
re_path(r'^users/(?P<user_ids>[\d,]+)/$', views.multiple_users, name='multiple_users'),
]
