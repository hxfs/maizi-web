# coding=utf-8

from django.shortcuts import render
from django.shortcuts import redirect
from web.models import class_info, Teacher, Plate, Article, Link, Ad
import json
from django.http import HttpResponse
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
# Create your views here.

def Page_get(request, list_obj):
    paginator = Paginator(list_obj, 8)
    try:
        page = int(request.GET.get('page', 1))
        list_obj = paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        list_obj = paginator.page(1)

    return list_obj


def index(request):
    cls_all_info = class_info.objects.all()
    cls_all_info = Page_get(request, cls_all_info)
    teacher_info = Teacher.objects.all()[:4]
    plate_name = []
    article_name = []
    res = Plate.objects.all()[:3]
    for i in res:
        article_list = Article.objects.filter(plate__name=i)[:5]
        plate_name.append(i.name)
        article_name.append(article_list)
    links = Link.objects.all()
    banners = Ad.objects.all()[:3]
    for banner in banners:
        print banner.img_url

    return render(request, 'index.html', locals())


def course(request):
    return render(request, 'course.html')


def play(request):
    return render(request, 'play.html')


def search(request):
    try:
        data = request.GET.get('data')
        print data
        if len(data) > 0:
            res = class_info.objects.filter(cls_name__startswith=data)
            print res
            if len(res) == 0:
                mess = {'messages': 'Nothings'}
                return HttpResponse(json.dumps(mess))
            else:
                a = {}
                for i in range(len(res)):
                    a[i] = res[i].cls_name
                j_a = json.dumps(a)
                return HttpResponse(j_a)
    except Exception as e:
        return HttpResponse("{messages:%s}" % e)


def teacher(request):
    if not request.GET.get('name'):
        return redirect(error)
    name = request.GET.get('name')
    try:
        message = Teacher.objects.filter(username=name)
        class_all = class_info.objects.filter(teacher__username=name)
        if len(message) == 0:
            return redirect(error)
        else:
            message = message[0]
            return render(request, 'teacher.html', locals())
    except Exception as e:
        return HttpResponse(e)
    print message


def article(request):
    teacher_id = request.GET.get('id')
    if not teacher_id:
        return redirect(error)

    art_content = Article.objects.get(pk=teacher_id).content
    return render(request, 'article.html', locals())

def error(request):

    return render(request, 'error.html')
