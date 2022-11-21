from django.urls import path
from . import views


urlpatterns=[
    path('home',views.school_home),
    path('addstudent',views.school_student),
    path('viewattendance',views.school_attendance),
    path('viewstudent',views.school_view)
]