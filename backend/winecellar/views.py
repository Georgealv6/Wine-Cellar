from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.views import LoginView

from .forms import Contactform, SignUpForm, LoginForm

# welcome page

def welcomepage(request):
    return render (request, 'landing/welcome.html')

def homepage(request):
    return render(request, 'landing/home.html')

def AboutUs(request):
    return render(request, 'landing/about.html')

def Blog(request):
    return render(request, 'landing/blog.html')

def Login(request):
    signup_form = SignUpForm
    login_form = LoginForm

    #Sign up submission
    if request.method == "POST" and request.POST.get('form_type') == "signup":
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            login(request, user) # login after sign up
            return redirect("home") 
        else:
            messages.error(request, "Please fix the sign up errors below.")

    # Login submission 
    elif request.method == "POST" and request.POST.get("form_type") == "login":
        login_form = LoginForm(request, data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid login. Please try again.")  
          
    return render(request, 'account/login.html', {"signup_form": signup_form, "login_form": login_form})

def Contact(request):
    submitted = False

    if request.method == 'POST':
        form = Contactform(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            send_mail(
                f"New Contact Message from {name}",
                message,
                email,
                ['your@email.com'],  # Replace with your email
                fail_silently=False,
            )
            return render(request, 'landing/contact.html', {'form': Contactform(), 'submitted': True})
    else:
        form = Contactform()
    

    return render(request, 'landing/contact.html',{'form': form, 'submitted': submitted})
