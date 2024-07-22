from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReviewForm
from .models import Review

# Create your views here.
# CSRF stands for Cross Site Request Forgery

def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            review = Review(user_name = form['user_name'],
                            review_text = form['review_text'],
                            rating = form['rating'])
            review.save()
            return HttpResponseRedirect('/thank-you')
    else:
        form = ReviewForm()
    return render(request, 'reviews/review.html', {'form': form})

def thank_you(request):
    return render(request, 'reviews/thank_you.html')