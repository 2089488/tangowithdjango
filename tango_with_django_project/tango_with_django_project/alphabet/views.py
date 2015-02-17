from django.shortcuts import render
from django.http import HttpResponse

def abc(request):
    return HttpResponse("a, b, c, d, ...z<br />"
                        "<a href='/alphabet/reverse'>reverse</a>")

def reverse(request):
    return HttpResponse('z, y, x, ...a <br /><a href="/alphabet/">back</a>')