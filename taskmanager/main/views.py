from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    categorie = Categorie.objects.all()
    portfolio = Portfolio.objects.all()
    menu = {
        'ОБО МНЕ': 'about',
        'ВИДЫ': 'type',
        'МОИ РАБОТЫ': 'portfolio',
        'ВИДЕО': 'video',
        'КОНТАКТ': 'contact'
            }
    data = {
        'categorie': categorie,
        'portfolio': portfolio,
        'menu': menu

    }
    return render(request, 'main/index.html', data)
