from django.shortcuts import render

# Create your views here.

def LandingPage(request):
    return render(request, "LandingPage/Landing.html")
