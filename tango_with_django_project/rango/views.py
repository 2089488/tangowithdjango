from django.http import HttpResponse

def index(request):
    return HttpResponse('Rango says "Hey there world!"<p>'
                        '<a href="/rango/about">about</a>')

def about(request):
    return HttpResponse('Rango says: '
                        '<br>"This is the <b>about</b> page<p>'
                        '<a href="/rango">Index</a>')
