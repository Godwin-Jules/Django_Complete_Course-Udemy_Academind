from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Book as b
# Create your views here.

def index(request):
    books = b.objects.all()
    return render(request, 'book_outlet/index.html', {
        'books': books
    })

def book_detail(request, book_slug):
    # try:
    #     book = b.objects.get(pk = book_id)
    # except:
    #     raise Http404()
    book = get_object_or_404(b, slug = book_slug)
    return render(request, 'book_outlet/book_detail.html', {
        'book': book
    })