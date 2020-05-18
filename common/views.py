import time
from django.shortcuts import render
from .models import Question
from .models import Answer
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.http import HttpResponse
from . import spider
import json


# Create your views here.
def getZHIHU(request):
    content = json.loads(request.body)

    if content['url'] is not "":
        # 还需要写一个valid function决定url是否是知乎的
        content = spider.main(content['url'])

        # check if database contain same question!
        Quest_id = Question.objects.filter(question_id=content['question_id']).values('question_id')
        if not Quest_id:
            Question.objects.create(  # question_author=content[question_],
                question_pubDate=content['question_pubDate'],
                question_detail=content['question_detail'],
                question_title=content['question_title'],
                question_id=content['question_id'])
        else:
            print("数据库已经存在相同的问题！")

        # check if database contain same answer!
        Ans_id = Answer.objects.filter(Answer_id=content['answer_id']).values('Answer_id')
        if not Ans_id:
            Answer.objects.create(
                Answer_id=content['answer_id'],
                Answer_author=content['answer_author'],
                Answer_content=content['answer_content'],
                Answer_pubDate=content['answer_pubDate'],
                Question=Question.objects.get(question_id=content['question_id'])
            )
        else:
            print("数据库已经存在相同的答案！")

        return JsonResponse({'success': True})

    elif content['url'] is "":
        Res = {'success': None}
        print("requesting nothing.")
        return JsonResponse(Res)

    else:
        R = {'success': False}
        print("Opps, something went wrong!")
        return JsonResponse(R)


def question(request):
    question_list = Question.objects.all()
    context = {
        'question_list': question_list
    }
    return render(request, 'common/templates/question.html', context)


# TODO : 需要增加回答的显示！
def question_detail(request, questionId):
    global context
    question_content = Question.objects.all()
    for q in question_content:
        if q.question_id == questionId:  # question_id must have one and only one id, but one question_id may
            # associate with multiple answers which need some work.
            context = {
                'question_content': q
            }

            break

    answer_content = Answer.objects.all()
    for a in answer_content:
        if a.Question_id == questionId:
            context['answer_content'] = a.Answer_content
            context['answer_author'] = a.Answer_author

            break

    return render(request, 'common/templates/detail.html', context)


def index(request):
    if request.POST:
        Question.objects.create(  # question_author=request.POST['question_author'],
            question_pubDate=time.strftime("%Y-%m-%d %H:%M", time.localtime()),
            question_detail=request.POST['question_detail'],
            question_title=request.POST['question_title'],
            question_id=request.POST['question_id'])
        messages.success(request, "输入成功")
        return HttpResponseRedirect('/question/')

    return render(request, 'common/templates/index.html')
