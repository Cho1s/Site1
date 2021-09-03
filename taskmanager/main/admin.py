from django.contrib import admin
from .models import *

# Register your models here.
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['title', 'cat']
    prepopulated_fields = {'slug': ('title',)}

class CategorieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Categorie, CategorieAdmin)