from django.shortcuts import render


# Create your views here.


def packages(request):
    return render(request, 'packages.html')


def ceremony(request):
    return render(request, 'ceremony.html')


def reception(request):
    return render(request, 'reception.html')
