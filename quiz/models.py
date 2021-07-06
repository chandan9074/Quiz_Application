from django.db import models
from accounts.models import UserProfile
from django.utils.crypto import get_random_string


# Create your models here.
class Quiz(models.Model):
    subject = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_time = models.DateTimeField()
    time_end = models.DateTimeField()
    time_limit = models.DecimalField(max_digits=5, decimal_places=2)
    enrollment_key = models.CharField(max_length=100, blank=True,  unique=True)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    attempt = models.IntegerField(default=0, blank=True)

    def save(self, *args, **kwargs):
        string = self.enrollment_key

        if not string:
            self.enrollment_key = get_random_string(5).lower()
        super(Quiz, self).save(*args, **kwargs)


class Question(models.Model):
    question = models.TextField()
    marks = models.DecimalField(max_digits=5, decimal_places=2)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)


class Option(models.Model):
    option = models.CharField(max_length=500)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


class Answer(models.Model):
    answer = models.CharField(max_length=500)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


class Result(models.Model):
    result = models.DecimalField(max_digits=5, decimal_places=2)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)