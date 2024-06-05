from django import forms

class ContactForm(forms.Form):
    username = forms.CharField(label='Your Name', max_length=100)