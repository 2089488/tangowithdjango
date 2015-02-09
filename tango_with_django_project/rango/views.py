from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context_dict = {'boldmessage': "I am bold font from the context"}

    return render(request, 'rango/index.html', context_dict)

def about(request):
    return HttpResponse('Rango says: '
                        '<br>"This is the <b>about</b> page<p>'
                        '<a href="/rango">Index</a>')
