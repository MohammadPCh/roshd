from django.urls import path
from school.views import *

urlpatterns = [
    path('API/marks/<str:nid>/', StudentMarkAPI.as_view()),
    path('API/students/<str:name>/<int:year>/', ClassRoomStudentListAPI.as_view()),
    path('API/courses/average/<str:name>/<int:year>/', CourseAverageAPI.as_view()),
]
