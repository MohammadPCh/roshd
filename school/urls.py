from django.urls import path
from school.views import StudentMarkAPI, ClassRoomStudentListAPI

urlpatterns = [
    path('API/marks/<int:nid>/', StudentMarkAPI.as_view()),
    path('API/students/<str:name>/<int:year>/', ClassRoomStudentListAPI.as_view()),
]
