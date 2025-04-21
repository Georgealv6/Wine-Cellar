from django.shortcuts import render

# welcome page

def welcomepage(request):
    return render (request, 'landing/welcome.html')
