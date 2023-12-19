from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import *


def add_fun(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        
        print(name, description)

        News.objects.create(name=name, description=description, image=image)
        return HttpResponse('Changes saved successfully')

    return render(request, 'index.html')

def read_fun(request) :
    all_news = News.objects.all()
    return render(request, 'news_print.html', {'all_news' : all_news})
    # return HttpResponse('wecome to read func')


def del_fun(request, news_id):
    del_news =  News.objects.get(id = news_id)
    del_news.delete()
    return redirect('/read_fun')
    


def update_fun(request, news_id) :
    update_news = News.objects.get(id = news_id)
    if request.method == 'POST' :
        name = request.POST.get('name')
        description = request.POST.get('description')

        update_news.name = name
        update_news.description = description
        update_news.save()


        return redirect('/read_fun')
    return render(request, 'update_news.html', {'update_news' : update_news})



