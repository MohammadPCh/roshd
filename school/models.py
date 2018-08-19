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
