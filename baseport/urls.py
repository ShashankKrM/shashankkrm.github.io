from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('posts/', views.posts, name = 'posts'),
    path('post/', views.post, name = 'post'),
    path('profile', views.profile, name = 'profile'),
    # path('index', views.index, name = 'index'),
    path('blog', views.blog, name = 'blog'),

    #CRUD URLS
    path('create_post/', views.createPost, name = 'create_post' ),
    path('update_post/', views.updatePost, name = 'update_post' ),

    #EMAIL CONFIGURATION
    path('send_email/', views.sendEmail, name = 'send_email'),
]