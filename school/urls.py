from django.urls import path
from school.views import StudentMarkAPI

urlpatterns = [
    path('API/marks/<int:nid>/', StudentMarkAPI.as_view())
]
