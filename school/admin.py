from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    pass


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass


@admin.register(OfferedCourse)
class OfferedCourseAdmin(admin.ModelAdmin):
    pass


@admin.register(ClassRoomEnrollment)
class ClassRoomEnrollAdmin(admin.ModelAdmin):
    pass


@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    pass
