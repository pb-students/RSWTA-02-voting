from functools import reduce

from django.db import models
from django.utils import timezone
from datetime import timedelta


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - timedelta(days=1)

    def vote_count(self):
        count = 0
        for choice in self.choice_set.all():
            count += choice.votes

        return count

    def choices(self):
        return sorted(self.choice_set.all(), key=lambda x: x.votes, reverse=True)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
