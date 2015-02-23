from django.http import HttpResponse
from django.shortcuts import render

def home(request):

    context_dict = {
        'my_name' : 'Mariusz',
    }

    return render(request, 'aboutme/justme.html', context_dict)

def myname(request):

    context_dict = {
        'name' : '...friends call me "Pazur" (Talon)',
        'greeting' : 'Hi! Salut! Siema! Sai cien! Tik-tak, tik-tak!',
        'face' : '(:-D)'
    }
    return render(request, 'aboutme/myname.html', context_dict)

def myage(request):

    dict = { 'myCurrentAge' : '153'}

    return render(request, 'aboutme/age.html', dict)

