import time
from django.shortcuts import render
from .models import Question
from .models import Answer
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from . import spider


# Create your views here.
def getZHIHU(request):
    if request.POST:
        # 还需要写一个valid function决定url是否是知乎的
        content = spider.main(request.POST['zhihu_url'])

        Question.objects.create(  # question_author=content[question_],
            question_pubDate=content['question_pubDate'],
            question_detail=content['question_detail'],
            question_title=content['question_title'],
            question_id=content['question_id'])

        # Answer.objects.create(
        #     Answer_author=content['answer_author'],
        #     # Answer_content=content['answer_content'],
        #     # Content seems need more work because of type error
        #     Answer_pubDate=content['answer_pubDate']
        # )

        # Answer part needs more work!!!!!

    return HttpResponse(content)


def question(request):
    question_list = Question.objects.all()
    context = {
        'question_list': question_list
    }
    return render(request, 'common/templates/question.html', context)


def question_detail(request, questionId):
    global context
    question_content = Question.objects.all()
    for i in question_content:
        if i.question_id == questionId:  # question_id must have one and only one id, but one question_id may
            # associate with multiple answers which need some work.
            context = {
                'question_content': i
            }
            print(i)
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
