from django.shortcuts import render, get_object_or_404
from .models import BlogPost
from django.http import Http404


# Create your views here.

def home(request):
    posts = BlogPost.objects.all()
    return render(request, 'home.html', {'posts': posts})


def about(request):
    return render(request, 'about.html')


def detail(request, postId):
    try:
        post = BlogPost.objects.get(id=postId)
    except BlogPost.DoesNotExist:
        raise Http404("This article does not exist")
    else:
        # post = get_object_or_404(BlogPost, id=postId)
        return render(request, 'detail.html', {'post': post})
