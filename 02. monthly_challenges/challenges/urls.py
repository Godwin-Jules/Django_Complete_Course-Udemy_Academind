from . import views
from django.urls import path


urlpatterns = [
    # path("january/", views.january),
    # path("february/", views.february),
    # path("march/", views.march),
    path("<int:month>/", views.monthly_challenges_by_numbers),
    path("<str:month>/", views.monthly_challenge)
]