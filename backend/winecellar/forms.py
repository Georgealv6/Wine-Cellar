from django import forms

class Contactform(forms.Form):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder':'First Name','class':'wine-input','type':'text'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder':'Last Name','class':'wine-input', 'type':'text'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Enter Email Here', 'class':'wine-input','type':'email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Your Message','class':'wine-textarea', 'rows': 5}))

# class SignIn(forms.Form):

# class SignUp(forms.Form):      