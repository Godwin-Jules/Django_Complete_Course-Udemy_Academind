from django import forms
from .models import Review

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label='Your name', max_length=100, error_messages={
#         'required': 'Your name must not be empty',
#         'max_length': 'Please enter a shorter name!'
#     })
#     review_text = forms.CharField(label='Your Feedback', widget=forms.Textarea, max_length=250)
#     rating = forms.IntegerField(label='Your Rating', min_value=0, max_value=5)
    
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'  # this tells Django to consider all the fields of the model
        # fields = ['user_name', 'review_text', 'rating'] # To specify the fields you want to be visible for the user
        # exclude = {}  # To take into account all fields from the model except the fields in the list
        labels = {
            'user_name' : 'Your Name',
            'review_text' : 'Your Feedback',
            'reting' : 'Your Rating'
        }
        errors_messages = {
            'user_name' : {
                'required' : 'Your name must not be empty',
                'max_length' : 'Please enter a shorter name!'
            }
        }
        widget = {
            # 'review_text' : forms.Textarea
        }


"""
    You can override some attributes of or behavior of a form by parsing some arguments to the field constructor
"""