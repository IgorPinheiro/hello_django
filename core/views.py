from django.shortcuts import render, HttpResponse

# Create your views here.

def Hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos</h1>'.format(nome, idade))
