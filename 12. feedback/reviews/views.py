from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
# CSRF stands for Cross Site Request Forgery

def review(request):
    if request.method == 'POST':
        entered_username = request.POST['name']
        print(entered_username)
        return HttpResponseRedirect('/thank-you/')
    return render(request, 'reviews/review.html')

def thank_you(request):
    return render(request, 'reviews/thank_you.html')