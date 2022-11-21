from django.urls import path
from . import views


urlpatterns=[
    path('home',views.students_home),
    path('profile',views.stu_profile),
    path('change_password',views.stu_password), 
    path('view_attendance',views.stu_attendance)
]