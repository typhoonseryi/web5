from django.shortcuts import render
from django.http import HttpResponse 
from django.core.paginator import Paginator
from django.http import Http404


def view1(request):
    questions = Question.objects.new()
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(questions, 10)
    paginator.baseurl = '/?page='
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return render(request, 'base.html', {
           'posts': page.object_list,
           'paginator': paginator, 'page': page,
    })

def view2(request):
    questions = Question.objects.popular()
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(questions, 10)
    paginator.baseurl = '/popular/?page='
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return render(request, 'base.html', {
           'posts': page.object_list,
           'paginator': paginator, 'page': page,
    })

def view3(request, ident):
    try:
        question = Question.objects.get(question_id=ident)
    except Question.DoesNotExist:
        raise Http404
    try:
        answers = Answer.question.filter(question_id=ident)
    except Answer.DoesNotExist:
        answers = None
    return render(request, 'base2.html', {
           'title' : question.title,
           'text' : question.text,
           'answers' : answers,
    })   
    
