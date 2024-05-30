from django.shortcuts import render
from .models import *


all_posts_registered = Post.objects.all()

def get_date(post):
    return post.date

# Create your views here.


def index(request):
    # sorted_posts = sorted(all_posts_registered, key=get_date)
    # latest_posts = sorted_posts[0:3]
    latest_posts = all_posts_registered.order_by('-date')[:3]
    return render(request, 'blog/index.html', {
        'posts': latest_posts
    })

def posts(request):
    return render(request, 'blog/all-posts.html', {
        'all_posts': all_posts_registered.order_by('-date')
    })

def post(request, slug):
    identified_post = next(post for post in all_posts_registered if post.slug == slug)
    return render(request, 'blog/post-detail.html', {
        'post': identified_post,
        'post_tags': identified_post.tags.all()
    })
