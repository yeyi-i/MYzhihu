from django.db import models


# Create your models here.
class Question(models.Model):
    question_author = models.CharField(max_length=30)
    pub_date = models.DateTimeField('date published')
    question_title = models.TextField()
    question_detail = models.TextField()


class Answer(models.Model):
    Question = models.ForeignKey(Question, on_delete=models.CASCADE)
    Answer_author = models.CharField(max_length=30)
    Answer_text = models.TextField()
