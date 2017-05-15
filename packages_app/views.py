from django.shortcuts import render

# Create your views here.


def packages(request):
    return render(request, 'packages.html')


def vocalist(request):
    return render(request, 'vocalist.html')


def harpist(request):
    return render(request, 'harpist.html')


def pianist(request):
    return render(request, 'pianist.html')


def ceremony(request):
    return render(request, 'ceremony.html')


def reception(request):
    return render(request, 'reception.html')