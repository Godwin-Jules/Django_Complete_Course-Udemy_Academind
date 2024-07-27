from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from .models import *
from .forms import CommentForm


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


class PostView(View):

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        return render(request, 'blog/post-detail.html', {
            'post': post,     
            'post_tags': post.tags.all(),
            'comment_form': CommentForm(),
            'comments': post.comments.all().order_by('-id')     #type:ignore
        })
    
    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('blog-post', args=[slug]))

        return render(request, 'blog/post-detail.html', {
            'post': post,
            'post_tags': post.tags.all(),
            'comment_form': comment_form,
            'comments': post.comments.all().order_by('-id')     #type:ignore
        })
