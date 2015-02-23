import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from rango.models import Category, Page


def populate():
<<<<<<< HEAD
    me_cat = add_cat("Mariusz Szmajduch", 777, 77)

    add_page(cat=me_cat,
             title="GitHub",
             url="https://github.com/2089488/tangowithdjango",
             views=122)

    add_page(cat=me_cat,
             title="pythonanywhere",
             url="https://www.pythonanywhere.com/user/2089488/consoles/",
             views=12)
=======

    my_page_cat = add_cat('Mariusz Szmajduch 2089488', 777, 777)

    add_page(cat=my_page_cat,
             title="GitHub repository",
             url="https://github.com/2089488/tangowithdjango",
             views=22)

    add_page(cat=my_page_cat,
             title="pythonanywhere.com",
             url="https://www.pythonanywhere.com/user/2089488/consoles/",
             views=18)
>>>>>>> master

    python_cat = add_cat('Python', 128, 64)

    add_page(cat=python_cat,
        title="Official Python Tutorial",
        url="http://docs.python.org/2/tutorial/",
<<<<<<< HEAD
        views=33)

=======
        views=39)
>>>>>>> master

    add_page(cat=python_cat,
        title="How to Think like a Computer Scientist",
        url="http://www.greenteapress.com/thinkpython/",
<<<<<<< HEAD
        views=25)
=======
        views=8)
>>>>>>> master

    add_page(cat=python_cat,
        title="Learn Python in 10 Minutes",
        url="http://www.korokithakis.net/tutorials/python/",
<<<<<<< HEAD
        views=79)
=======
        views=221)
>>>>>>> master

    django_cat = add_cat("Django", 64, 32)

    add_page(cat=django_cat,
        title="Official Django Tutorial",
        url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/",
<<<<<<< HEAD
        views=41)
=======
        views=84)
>>>>>>> master

    add_page(cat=django_cat,
        title="Django Rocks",
        url="http://www.djangorocks.com/",
<<<<<<< HEAD
        views=17)
=======
        views=46)
>>>>>>> master

    add_page(cat=django_cat,
        title="How to Tango with Django",
        url="http://www.tangowithdjango.com/",
<<<<<<< HEAD
        views=68)

    frame_cat = add_cat("Other Frameworks", 32, 16)


    add_page(cat=frame_cat,
        title="Bottle",
        url="http://bottlepy.org/docs/dev/",
        views=19)
=======
        views=51)

    frame_cat = add_cat("Other Frameworks", 32, 16)

    add_page(cat=frame_cat,
        title="Bottle",
        url="http://bottlepy.org/docs/dev/",
        views=44)
>>>>>>> master

    add_page(cat=frame_cat,
        title="Flask",
        url="http://flask.pocoo.org",
<<<<<<< HEAD
        views=34)
=======
        views=75)
>>>>>>> master

    # Print out what we have added to the user.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))

<<<<<<< HEAD
def add_page(cat, title, url, views=0):
=======
def add_page(cat, title, url, views):
>>>>>>> master
    p = Page.objects.get_or_create(category=cat, title=title, url=url, views=views)[0]
    return p

def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name, views=views, likes=likes)[0]
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()