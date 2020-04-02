import time
from django.shortcuts import render
from .models import Question
from django.contrib import messages
from django.http import HttpResponseRedirect


# Create your views here.
def question(request):
    question_list = Question.objects.all()
    context = {
        'question_list': question_list
    }
    return render(request, 'common/templates/question.html', context)


def question_detail(request, questionId):
    for i in Question.objects.all():
        if questionId == i.question_id:
            print(i)
            question_content = i.objects.all()
    context = {
        'question_content': question_content
    }
    return render(request, 'common/templates/detail.html', context)


def index(request):
    if request.POST:
        Question.objects.create(question_author=request.POST['question_author'],
                                pub_date=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                                question_detail=request.POST['question_detail'],
                                question_title=request.POST['question_title'],
                                question_id=request.POST['question_id'])
        messages.success(request, "输入成功")
        return HttpResponseRedirect('/question/')

    return render(request, 'common/templates/index.html')
