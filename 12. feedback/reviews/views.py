from typing import Any
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .forms import ReviewForm
from django.views.generic import TemplateView

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
    
class ReviewListView(TemplateView):
    template_name = 'reviews/review_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rev = rv.objects.all()
        context['reviews'] = rev
        return context
    
class ReviewDetailView(TemplateView):
    template_name = 'reviews/review_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review  = rv.objects.get(pk = kwargs['review_id'])
        context['review'] = review
        return context