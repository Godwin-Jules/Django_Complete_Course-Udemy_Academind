from django.http import HttpResponseRedirect
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
    return render(request,
                  'challenges/index.html',
                  {'months': MONTHS})

def challenge_by_string(request, months:str):

    month = months.lower()
    if month in MONTHS:
        challenge = monthly_challenges[month]
        return render(request,
                      'challenges/challenge.html',
                      {
                          'month': month,
                          'challenge': challenge,
                      })
    else:
        return render(request, '404.html')

def challenge_by_number(request, months:int):


    # The first solution
    if months > len(monthly_challenges):
        return render(request, '404.html')
    
    redirect_month = MONTHS[months - 1]  # type: ignore
    redirect_path = reverse('challenge-by-string', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
    # return HttpResponseRedirect(reverse('challenges_index', args=[monthly_challenges[months - 1]])) # type: ignore
    
    # The second solution
    # if months > len(monthly_challenges):
    #     challenge = monthly_challenges[months-1]
    #     month = list(monthly_challenges.keys())
    #     return render(request,
    #                   'challenge.html',
    #                   {
    #                       'month': month,
    #                       'challenge': challenge,
    #                   })
    # else:
    #     return render(request, '404.html')