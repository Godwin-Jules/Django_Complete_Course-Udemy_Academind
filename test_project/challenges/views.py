from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 30 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 30 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 30 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": None,
}
MONTHS = list(monthly_challenges.keys())


# Create your views here.
def index(request):
    return render(request, 'challenges/index.html', {'months': MONTHS})

def challenge_by_string(request, months:str):

    if months.lower() in MONTHS:
        return render(request, 'challenges/challenge.html', {
                            'month': months,
                            'challenge': monthly_challenges[months.lower()],
                        })
    else:
        return render(request, '404.html')

def challenge_by_number(request, months:int):

    if months > len(monthly_challenges):
        return render(request, '404.html')
    
    month = list(monthly_challenges.keys())[months - 1]
    redirect_path = reverse('challenge-string', args=[month])
    return HttpResponseRedirect(redirect_path)