from django.shortcuts import render
from .utilities import genPass


# Create your views here.
def home(request):
    return render(request, 'home.html')


def password(request):
    length = int(request.POST.get('length'))
    numbers = request.POST.get('numbers')
    big = request.POST.get('big')
    special = request.POST.get('specials')
    password = genPass(length, big, numbers, special)

    return render(request, 'password.html', {'password': password})


def about(request):
    return render(request, 'about.html')
