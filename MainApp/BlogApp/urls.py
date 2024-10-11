from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('home/', views.home, name = 'home'),
    path('login/', views.user_login, name = 'login'),
    path('logout/', views.user_logout, name = 'logout'),
    path('feed/', views.feed, name = 'feed'),
    path('create-post/', views.create_post, name = 'create-post'),
    
]