from django.shortcuts import render
from django.http import HttpResponse

def about(requst):
    return HttpResponse("this is test app")
