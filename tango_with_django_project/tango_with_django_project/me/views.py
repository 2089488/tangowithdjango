from django.http import HttpResponse

def info(request):
    return HttpResponse("This is about me..."
                        "<br /><a href='/me/name'>my name</a><br />"
                        "<a href='/me/age'>my age:</a>")

def name(request):
    return HttpResponse("Mariusz :)<br />"
                        "<a href='/me/'>home</a>")

def age(request):
    return HttpResponse("150! I swear!<br /><a href='/me/'>home</a>")
