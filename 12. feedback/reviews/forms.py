from django import forms

class ReviewForm(forms.Form):
    user_name = forms.CharField(label='Your name', max_length=100, error_messages={
        'required': 'Your name must not be empty',
        'max_length': 'Please enter a shorter name!'
    })
    review_text = forms.CharField(label='Your Feedback', widget=forms.Textarea, max_length=250)
    rating = forms.IntegerField(label='Your Rating', min_value=0, max_value=5)
    

"""
    You can override some attributes of or behavior of a form by parsing some arguments to the field constructor
"""