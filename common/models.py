from django.db import models


# Create your models here.
class Question(models.Model):
    question_pubDate = models.DateTimeField('question date published')
    question_title = models.TextField()
    question_detail = models.TextField()
    question_id = models.IntegerField()


class Answer(models.Model):
    Answer = models.ForeignKey(Question, on_delete=models.CASCADE)
    Answer_author = models.CharField(max_length=30)
    Answer_content = models.TextField()
    Answer_pubDate = models.DateTimeField('answer date published')
