from django.shortcuts import render
from .models import BlogPost

# Create your views here.

def home(request):
    posts = BlogPost.objects.all()
    return render(request, 'home.html', {'posts': posts})


def about(request):
    return render(request, 'about.html')

def detail(request, postId):
    post = BlogPost.objects.get(id=postId)
    return render(request, 'detail.html', {'post': post})