from django.shortcuts import render

# Create your views here.
def teachers_home(request):
    return render(request,'customer_templates/home.html')

def view_cart(request):
    return render(request,'customer_templates/cart.html')

def view_order(request):
    return render(request,'customer_templates/order.html')

