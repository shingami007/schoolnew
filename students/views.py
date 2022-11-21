from django.shortcuts import render

# Create your views here.

def students_home(request):
    return render(request,'students_templates/home.html')
def stu_profile(request):
    return render(request,'students_templates/profile.html')
def stu_attendance(request):
    return render(request,'students_templates/view_attendance.html')
def stu_password(request):
    return render(request,'students_templates/change_password.html')
