from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .forms import ReviewForm
from .models import Review as rv

# Create your views here.
# CSRF stands for Cross Site Request Forgery

class ReviewView(CreateView):
    model = rv  # so you don't wanna create a form class any more or you can point form_class to the form class as well
                # but you must know something, if you don't use the form_class this CreateView can't let configure the
                # labels for example ... but will use the default configuration for creating a form in Django
    form_class = ReviewForm
    template_name = 'reviews/review.html'
    success_url = '/thank-you'

    def form_valid(self, form):     # You must override this method to specify what you want the view to do after the valid form is submitted
        form.save()
        return super().form_valid(form)
    

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
        return context


class ReviewDetailView(DetailView):
    template_name = 'reviews/review_detail.html'
    model = rv

class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST['review_id']
        favorite_review = rv.objects.get(pk=review_id)
        request.session['favorite_review'] = favorite_review
        return HttpResponseRedirect('/review/' + review_id)