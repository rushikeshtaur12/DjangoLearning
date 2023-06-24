from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    dict = {'insert_me': 'Hello EveryOne'}
    return render(request, 'myapp/home.html', context=dict)


def comment(request):
    dict = {'insert_me': 'Comment Section'}
    return render(request, 'myapp/comments.html', context=dict)


def like(request):
    dict = {'insert_me': 'Like Section'}
    return render(request, 'myapp/comments.html', context=dict)


def story(request):
    dict = {'insert_me': 'Story Section'}
    return render(request, 'myapp/comments.html', context=dict)

# Create your views here.
