from django.shortcuts import render
from .forms import SignUpForm
# from django.http import HttpResponse

def home(request):
    # response = HttpResponse("Welcome to Clucker")
    return render(request, "home.html")

def sign_up(request):
    # response = HttpResponse("Welcome to Clucker")
    form = SignUpForm()
    return render(request, "sign_up.html", {'form': form})