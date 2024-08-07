from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReviewView.as_view()),
    path('thank-you/', views.ThankYouView.as_view(), name='thank-you'),
    path('reviews/', views.ReviewListView.as_view()),
    path('reviews/favorite/', views.AddFavoriteView.as_view()),
    path('review/<int:pk>/', views.ReviewDetailView.as_view(), name='review-detail'),
]