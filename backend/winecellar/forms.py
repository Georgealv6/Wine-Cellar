from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User

class Contactform(forms.Form):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder':'First Name','class':'wine-input','type':'text'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder':'Last Name','class':'wine-input', 'type':'text'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Enter Email Here', 'class':'wine-input','type':'email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Your Message','class':'wine-textarea', 'rows': 5}))

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username","email","password1","password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

        self.fields["username"].widget.attrs.update({"placeholder": "Name", "class": "wine-input","type": "text",})
        self.fields["email"].widget.attrs.update({"placeholder": "Email","class": "wine-input","type": "email",})
        self.fields["password1"].widget.attrs.update({"placeholder": "Password","class": "wine-input","type": "password",})
        self.fields["password2"].widget.attrs.update({"placeholder": "Confirm Password", "class": "wine-input","type": "password",})

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update({"placeholder": "Username or Email", "class": "wine-input","type": "text" })
        self.fields["password"].widget.attrs.update({"placeholder": "Password", "class": "wine-input","type": "password"})
        
