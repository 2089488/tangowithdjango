from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    return HttpResponse("1, 2, 3, 4, 5, 6,...<br />"
                        "<a href='/counting/reverse'>reverse</a>")

def reverse(request):
    return HttpResponse("... 3, 2, 1<br />"
                        "<a href='/counting/'>back</a>")
