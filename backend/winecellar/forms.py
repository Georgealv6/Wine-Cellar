from django import forms

class Contactform(forms.From):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder':'First Name'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder':'Last Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Enter Email Here'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Your Message'}))