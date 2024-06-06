from django import forms

class ReviewForm(forms.Form):
    user_name = forms.CharField(label='Your name', max_length=100, error_messages={
        'required': 'Your name must not be empty',
        'max_length': 'Please enter a shorter name!'
    })
"""
    You can override some attributes of or behavior of a form by parsing some arguments to the field constructor
"""