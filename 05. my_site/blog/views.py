from django.shortcuts import render



# Create your views here.


def index(request):
    return render(request, '404.html', {})
    # return render(request, 'blog/index.html', {})

def posts(request):
    return render(request, '404.html', {})
    # return render(request, 'blog/posts', {})

def post(request, slug):
    return render(request, '404.html', {})
    # return render(request, 'blog/post', {})