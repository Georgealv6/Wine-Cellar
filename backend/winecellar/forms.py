from django import forms

class Contactform(forms.Form):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder':'First Name','class':'wine-input'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder':'Last Name','class':'wine-input'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Enter Email Here', 'class':'wine-input'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Your Message','class':'wine-input', 'rows': 5}))