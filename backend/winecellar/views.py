from django.shortcuts import render
from .forms import Contactform
from django.core.mail import send_mail

# welcome page

def welcomepage(request):
    return render (request, 'landing/welcome.html')

def homepage(request):
    return render(request, 'landing/home.html')

def contactpage(request):
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
