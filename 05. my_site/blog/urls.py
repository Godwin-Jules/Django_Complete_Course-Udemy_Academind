from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blog'),
    path('posts/', views.posts, name='blog-posts'),
    path('posts/<slug>/', views.post, name='blog-post')
]
