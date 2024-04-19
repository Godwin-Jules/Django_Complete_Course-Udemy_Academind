from . import views
from django.urls import path


urlpatterns = [
    # path("january/", views.january),
    # path("february/", views.february),
    # path("march/", views.march),
    path("<month>/", views.monthly_challenges)
]