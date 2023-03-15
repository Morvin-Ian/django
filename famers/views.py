from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib import auth
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required

from .models import Product, Farmer, Subsidized


def registration(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if password_confirm == password:
            if Farmer.objects.filter(email=email).exists()==False:
                # password = make_password(password)
                Farmer.objects.create_user(username = "None", first_name=first_name, last_name=last_name, phone=phone, email=email, password=password)
                return redirect("farmer-login")
            else:
                messages.error(request, "Email Already Exists")
        else:
            messages.error(request, "Passwords do not match")
    return render(request,'farmers/registration.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user =  Farmer.objects.filter(email=email).first()
        state = Farmer.objects.filter(email=email).exists()
        if state:
            auth.authenticate(user)
            auth.login(request,user)
            print(request.user)
            return redirect('farmer-index', uuid=user.uuid)
        
        else:
            messages.error(request, "Invalid Credentials")
    return render(request,'farmers/login.html')


def index(request, uuid):
    farmer = Farmer.objects.get(uuid=uuid)
    products = Product.objects.filter(farmer=farmer)[:5]
    subsidized_products = Subsidized.objects.all()[:5]


    context = {
        "farmer":farmer,
        "products":products,
        "sub_products":subsidized_products
    }
    return render(request,'farmers/index.html', context)

def post_product(request, uuid):
    farmer = Farmer.objects.get(uuid=uuid)

    if request.method == 'POST':
        title = request.POST.get("title")
        price = request.POST.get("price")
        location = request.POST.get("location")
        description = request.POST.get("description")
        image = request.FILES.get("image")

        Product.objects.create(farmer=farmer, title=title, location=location, price=price, image=image, description=description)
        messages.info(request, "Product Post Succesful")
        return redirect('farmer-index', uuid=farmer.uuid)

    return render(request,'farmers/post-product.html')

def edit_product(request, uuid):
    product = Product.objects.get(uuid=uuid)

    
    if request.method == 'POST':
        product.title = request.POST.get("title")
        product.price = request.POST.get("price")
        product.location = request.POST.get("location")
        product.description = request.POST.get("description")
        product.image = request.FILES.get("image")

        product.save()
        messages.info(request, "Update Succesful")
        return redirect('farmer-index', uuid=product.farmer.uuid)

    context = {
        "product":product
    }

    return render(request,'farmers/edit-product.html', context)

def delete_product(request, uuid):
    product = Product.objects.get(uuid=uuid)
    
    if request.method == 'POST':
        product.delete()
        messages.info(request, "Deletion Succesful")
        return redirect('farmer-index', uuid=product.farmer.uuid)

    context = {
        "product":product
    }

    return render(request,'farmers/delete-product.html', context)


def subsidized_products(request, uuid):
    farmer = Farmer.objects.get(uuid=uuid)
    subsidized_products = Subsidized.objects.all()

    context = {
        "products":subsidized_products

    }

    return render(request, 'farmers/subsidized.html', context)

def subsidized_detail(request, uuid):
    product = Subsidized.objects.get(uuid=uuid)

    context={
        "product":product
    }

    return render(request, "customers/product-details.html", context)

def farmer_products(request, uuid):
    farmer = Farmer.objects.get(uuid=uuid)
    products = Product.objects.filter(farmer=farmer)

    context = {
        "products":products

    }

    return render(request, 'farmers/subsidized.html', context)