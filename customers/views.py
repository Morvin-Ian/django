from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

from famers.models import Product

def handler404(request, exception):
    return render(request, 'exceptions/404.html', status=404)

def handler500(request):
    return render(request, 'exceptions/500.html', status=500)

def choose_login(request):
    return render(request,'choose-login.html')

def choose_registration(request):
    return render(request,'choose-register.html')

def registration(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if password_confirm == password:
            if User.objects.filter(email=email).exists()==False:
                User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                return redirect("customer-login")
            else:
                messages.error(request, "Email Already Exists")
        else:
            messages.error(request, "Passwords do not match")
    return render(request,'customers/registration.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')

        else:
            messages.error(request, "Invalid Credentials")

    return render(request,'customers/login.html')

def logout(request):
    if request.method == 'GET':
        auth.logout(request)
        messages.info(request,"Now Logged out")
        return redirect("index")
    return JsonResponse("Logged out",safe=False)

@login_required(login_url='choose-login')

def index(request):
    products = Product.objects.all()[:6]
    context = {
        "products":products
    }
    return render(request,'customers/index.html', context)

def product_detail(request, uuid):
    product = Product.objects.get(uuid=uuid)

    context={
        "product":product
    }

    return render(request, "customers/product-details.html", context)

def shop(request):
    products = Product.objects.all()
    context = {
        "products":products
    }
    return render(request,'customers/shop.html', context)

@login_required(login_url='choose-login')
def cart(request):
    return render(request, 'customers/cart.html')

def add_cart(request):
    return JsonResponse("request", safe=False)

def update_cart(request):
    return JsonResponse("request", safe=False)

def remove_cart(request):
    return JsonResponse("request", safe=False)

