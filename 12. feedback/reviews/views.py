from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReviewForm
from .models import Review

# Create your views here.
# CSRF stands for Cross Site Request Forgery

def review(request):
    if request.method == 'POST':
        existing_model = Review.objects.get(pk=1)
        form = ReviewForm(request.POST, instance = existing_model)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thank-you')
    else:
        form = ReviewForm()
    return render(request, 'reviews/review.html', {'form': form})

def thank_you(request):
    return render(request, 'reviews/thank_you.html')