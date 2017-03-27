from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def packages(request):
    return render(request, 'packages.html')


def listen(request):
    return render(request, 'listen.html')


def faq(request):
    return render(request, 'faq.html')


def contact(request):
    return render(request, 'contact.html')


def login(request):
    return render(request, 'login.html')