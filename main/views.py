from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        "title": 'Mel.ua - Головна сторінка',
        "content": 'страница HOME'
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        "title": 'Mel.ua - Про Нас',
        "content": "doskalike.com.ua – надійний виробник якісної рекламної "
                   "продукції України. Розвиток кав'ярні, ресторану, бару,"
                   " нічного клубу, невеликої приватної пекарні неможливий без "
                   "грамотної побудови маркетингової стратегії. "
                   "Інтернет-магазин «DOSKALIKE» виробляє та реалізує "
                   "найефективніші інструменти реклами для подібного бізнесу – "
                   "крейдяні штендери, дошки меню, лайтбокси, вивіски, підставки, "
                   "та багато іншої продукції для внутрішньої та зовнішьої реклами"
    }
    return render(request, 'main/about.html', context)
