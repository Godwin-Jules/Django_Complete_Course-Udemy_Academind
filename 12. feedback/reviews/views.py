from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .forms import ReviewForm
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView

from .models import Review as rv

# Create your views here.
# CSRF stands for Cross Site Request Forgery

class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, 'reviews/review.html', {'form': form})

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thank-you')
        else:
            return render(request, 'reviews/review.html', {'form': form})

class ThankYouView(TemplateView):
    template_name = 'reviews/thank_you.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['message'] = 'This works!'
        return data
    
class ReviewListView(ListView):
    template_name = 'reviews/review_list.html'
    model = rv
    context_object_name = 'reviews' # by default context_object_name = 'object_list'

    def get_queryset(self):
        context = super().get_queryset()
        reviews_filtered = context.filter(rating__gt = 4)
        return reviews_filtered

class ReviewDetailView(DetailView):
    template_name = 'reviews/review_detail.html'
    model = rv
