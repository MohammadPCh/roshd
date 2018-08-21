from datetime import datetime

from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.
from rest_framework.compat import MaxValueValidator


class Semester(models.Model):
    SEMESTER_CHOICES = (
        ('1', 'Term 1'),
        ('2', 'Term 2'),
    )
    semester = models.CharField(choices=SEMESTER_CHOICES, max_length=1, default=0)
    year = models.CharField(max_length=4, default=datetime.now().year)

    def __str__(self):
        return '{0} {1}'.format(self.year, self.semester)

    class Meta:
        unique_together = (("semester", "year"),)


class Student(models.Model):
    # TODO add validators
    nid = models.CharField(max_length=10, default='', unique=True)
    first_name = models.CharField(max_length=20, default='')
    last_name = models.CharField(max_length=20, null=True)
    father_name = models.CharField(max_length=20)
    address = models.TextField(max_length=100, null=True, blank=True)

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)


class Course(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class ClassRoom(models.Model):
    class_name = models.CharField(max_length=20)
    courses = models.ManyToManyField(Course, related_name='classes', through='OfferedCourse')
    students = models.ManyToManyField(Student, through='ClassRoomEnrollment')

    def __str__(self):
        return self.class_name


class OfferedCourse(models.Model):
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.DO_NOTHING, default=1)

    def __str__(self):
        return '{0} | {1} | {2}'.format(self.semester, self.classroom, self.course)

    class Meta:
        unique_together = (("classroom", "course", "semester"),)


class ClassRoomEnrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='students')
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE, related_name='classrooms')
    semester = models.ForeignKey(Semester, on_delete=models.DO_NOTHING, default=1)

    def __str__(self):
        return '{0} | {1} | {2}'.format(self.semester, self.classroom, self.student)

    class Meta:
        unique_together = (("student", "semester"),)


class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    mark = models.FloatField(max_length=2, validators=[MinValueValidator(0), MaxValueValidator(20)], default=0)

    def __str__(self):
        return '{0} | {1} | {2} | {3}'.format(self.course, self.semester, self.mark, self.student)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.classroom = ClassRoomEnrollment.objects.get(semester=self.semester, student=self.student).classroom
        super(Mark, self).save()

    class Meta:
        unique_together = (("student", "course", "semester"),)
