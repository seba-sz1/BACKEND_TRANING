from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.models import User
import re
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Define a function for validating an Email
def check_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    # pass the regular expression
    # and the string into the fullmatch() method
    if re.fullmatch(regex, email):
        return True
    else:
        return False


# Create your views here.
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html', {'form': RegisterForm()})
    else:  # POST
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            usernameTaken = User.objects.filter(username=username).exists()
            emailTaken = User.objects.filter(email=email).exists()
            if emailTaken:
                error = 'Email already taken'
            if usernameTaken:
                error = 'Username already taken'
            if not usernameTaken and not emailTaken:
                emailValid = check_email(email)
                if emailValid:
                    try:
                        validate_password(password1)
                    except ValidationError as err:
                        return render(request, 'register.html', {'passwordErrors': err, 'form': RegisterForm()})
                    else:
                        user = User.objects.create_user(username=username, email=email, password=password1)
                        # return render(request,'register.html', {'message':"SUCCESS",'form':RegisterForm()})
                        return redirect('home')
                else:
                    error = "Invalid email, try again"
        else:
            error = "Your passwords are not correct"

        return render(request, 'register.html', {'message': error, 'form': RegisterForm()})


def loginUser(request):
    if request.method == 'GET':
        return render(request, 'loginUser.html', {"form": AuthenticationForm()})
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            usernameExit = User.objects.filter(username=username).exists()
            if usernameExit:
                errorMessage = 'Authentication failed - Incorrect password'
            else:
                errorMessage = f'Acount with username "{username}" does not exist.'
            return render(request, 'loginUser.html', {'Message': errorMessage, "form": AuthenticationForm()})


@login_required
def logoutUser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    return render(request, 'logout.html')
