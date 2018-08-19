from datetime import datetime
from django.db import models


# Create your models here.
class Semester(models.Model):
    SEMESTER_CHOICES = (
        ('1', 'Term 1'),
        ('2', 'Term 2'),
    )
    semester = models.CharField(choices=SEMESTER_CHOICES, max_length=1, default=0)
    year = models.CharField(max_length=4, default=datetime.now().year)


class Student(models.Model):
    # TODO add validators
    nid = models.CharField(max_length=10, default='')
    first_name = models.CharField(max_length=20, default='')
    last_name = models.CharField(max_length=20, null=True)
    father_name = models.CharField(max_length=20)
    address = models.TextField(max_length=100, null=True, blank=True)
