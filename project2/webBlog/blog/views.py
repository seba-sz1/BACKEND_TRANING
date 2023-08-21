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
    post = get_object_or_404(BlogPost, id=postId)

    if 'recently_read' in request.session:
        request.session['recently_read'].append([post.id, post.title])
        for (id, title) in request.session.get('recently_read'):
            if post.id == id:
                request.session['recently_read'].remove([id, title])

        request.session['recently_read'].insert(0,[post.id, post.title])    # add id and title in first place
        if len(request.session['recently_read']) > 4:
            request.session['recently_read'].pop()

    else:
        request.session['recently_read'] = [[post.id, post.title]]


    request.session.modified = True # potwierdzenie zmodyfikowania sesji
    
    return render(request, 'detail.html', {'post': post, 'recently_read': request.session['recently_read'][1:]})
