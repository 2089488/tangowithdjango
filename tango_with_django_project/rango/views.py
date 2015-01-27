from django.http import HttpResponse

def index(request):
    return HttpResponse("""Rango says - "Hey there world!"</br>
    </br>
    <a href="http://127.0.0.1:8000/rango/about">author:</a>""")

def about(request):
    return HttpResponse("""Rango says - "Here is the about page."</br>
    </br>
    This tutorial has been put together by <b>Mariusz Szmajduch, 2089488</b>""")