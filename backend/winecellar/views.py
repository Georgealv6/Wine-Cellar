from django.shortcuts import render

# welcome page

def welcomepage(request):
    return render (request, 'landing/welcome.html')

def homepage(request):
    return render(request, 'landing/home.html')