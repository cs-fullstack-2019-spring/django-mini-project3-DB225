from django.db import models
from django.utils import timezone


# Create your models here.
class TimeCardModel(models.Model):
    teacher_name = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    subject = models.CharField(max_length=30)
    hours = models.IntegerField()
    date_of_work = models.CharField(max_length=200)
    date_of_entry = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.teacher_name}, {self.date_of_entry}'
