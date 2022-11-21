from django.shortcuts import render

# Create your views here.

def school_home(request):
    return render(request,'schooladmin_templates/home.html')
def school_student(request):
    return render(request,'schooladmin_templates/addstudent.html')
def school_attendance(request):
    return render(request,'schooladmin_templates/view_attendance.html')
def school_view(request):
    return render(request,'schooladmin_templates/view_student.html')

