from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='challenges_index'),
    path('<str:months>/', views.challenge_by_string, name='challenge-by-string'),
    path('<int:months>/', views.challenge_by_number),
]
