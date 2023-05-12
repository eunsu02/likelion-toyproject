from django.urls import path
from posts.views import *

urlpatterns = [
    path('new/', create_post, name = 'create_post'),
    path('all/', get_all, name = 'get_all'),
    path('<int:id>/', delete_post, name = 'delete_post'),
    
]