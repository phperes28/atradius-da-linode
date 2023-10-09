from django.contrib import admin
from . import models
from import_export.admin import ImportExportActionModelAdmin
# from .models import Author, Book,Buyer,BookInstance, Genre, Language

# Register your models here.
# admin.site.register(models.BuyerDB)
# admin.site.register(Book)
# admin.site.register(BookInstance)
# admin.site.register(Buyer)
# admin.site.register(Genre)
# admin.site.register(Language)

class BuyerDBAdmin(ImportExportActionModelAdmin,admin.ModelAdmin ):
    ...
admin.site.register(models.BuyerDB,BuyerDBAdmin)

