from django.contrib import admin
from rango.models import Category, Page

<<<<<<< HEAD
class PageAdmin(admin.ModelAdmin):
    list_display = ('category','title',  'url')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)


=======
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)

class PageAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'url')

admin.site.register(Page, PageAdmin)
>>>>>>> master
