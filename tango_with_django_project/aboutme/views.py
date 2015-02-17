from django.http import HttpResponse

def home(request):
    return HttpResponse("It's just me!<br />"
                        "<a href='/aboutme/myname/'>I am...</a><br />"
                        "<a href='/aboutme/myage/'>I am...</a>")

def myname(request):
    return HttpResponse("Mariusz! Hello :)<br />"
                        "<a href='/aboutme/'>home</a>")

def myage(request):
    return HttpResponse("...150 years old, REALLY! ;)"
                        "<br /><a href='/aboutme/'>home</a>")