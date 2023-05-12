from django.urls import path
from posts.views import *

urlpatterns = [
    path('new/', create_post, name = 'create_post'),
    path('', get_all, name = 'get_all'),
    path('<int:id>/', post_detail, name = 'delete_post'),
    
]