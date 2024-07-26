from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView


all_posts_registered = Post.objects.all()

def get_date(post):
    return post.date

# Create your views here.


class IndexView(ListView):
    template_name = 'blog/index.html'
    model = Post
    ordering = ['-date']
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


class PostsView(ListView):
    template_name = 'blog/all-posts.html'
    model = Post
    ordering = ['-date']
    context_object_name = 'all_posts'


class PostView(DetailView):
    template_name = 'blog/post-detail.html'
    model = Post

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_tags'] = self.get_object().tags.all()     #type:ignore
        return context