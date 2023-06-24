from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Index Page...')


def home(request):
    return HttpResponse('Home Page')


def balance(request):
    return HttpResponse('Balance Page')


def payment(request):
    return HttpResponse('Payment Page')
# Create your views here.
