from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('nid', 'first_name', 'last_name',)


@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    pass


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(OfferedCourse)
class OfferedCourseAdmin(admin.ModelAdmin):
    list_display = ('classroom', 'course', 'semester',)


@admin.register(ClassRoomEnrollment)
class ClassRoomEnrollAdmin(admin.ModelAdmin):
    list_display = ('student', 'classroom', 'semester',)


@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ('year', 'semester',)


@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'semester', 'mark')
