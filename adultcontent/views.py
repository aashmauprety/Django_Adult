from django.shortcuts import render
from django.http import HttpResponse
from . import adultcheck

def home(request):
    return render(request, 'adultcontent/home.html')

def check(request):
    text1 = format(request.POST["text1"])
    result = adultcheck.contains_abusive(text1)
    censor = adultcheck.censor(text1)
    return render(request, 'adultcontent/check.html', { 'output':result, 'censor': censor})

