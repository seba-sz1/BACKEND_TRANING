from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')

def password(request):
    return render(request, 'password.html')
