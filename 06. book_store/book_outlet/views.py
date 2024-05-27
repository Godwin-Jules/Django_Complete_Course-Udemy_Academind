from django.shortcuts import render, get_object_or_404
from django.db.models import Avg

from .models import Book as b
# Create your views here.

def index(request):
    books = b.objects.all().order_by('-rating')   # By default, the order is 'ascending', to make it 'descending', you just need to add a minus sign before the column name like b.objects.all().order_by('-title')
    num_books = books.count()
    avg_rating = books.aggregate(Avg('rating'))
    return render(request, 'book_outlet/index.html', {
        'books': books,
        'total_number_of_books': num_books,
        'average_rating': avg_rating
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