from django.shortcuts import render, redirect, HttpResponseRedirect
from datetime import datetime
from home.models import Contact
from home.models import Product
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
import random


def index(request):
    z = ['mobiles', 'desktop', 'laptops']
    temp = random.randint(0, 2)
    Products = Product.objects.filter(product_cat=z[temp])
    return render(request, 'index.html', {'Products': Products})


def about(request):
    return render(request, 'about.html')


def cart(request):
    return render(request, 'cart.html')


def prodview(request, myid):
    product = Product.objects.filter(product_id=myid)
    return render(request, 'prodview.html', {'products': product[0]})


def prod(request):
    params = {'products': Product.objects.all()}
    return render(request, 'productlist.html', params)



def search(request):
    q = request.GET.get('search')
    print(q)
    params = {'products': Product.objects.filter(product_cat=q)}
    print(params['products'])
    return render(request, 'productlist.html', params)


def loginc(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        pword = request.POST.get('pword')
        user = authenticate(username=name, password=pword)
        if(user is not None):
            login(request, user)
            messages.success(request, 'Logged in Successfully')
            return redirect('/')
    return render(request, 'Login_user.html')


def logins(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        pword = request.POST.get('pword')
        user = authenticate(username=name, password=pword)
        if(user is not None):
            login(request, user)
            messages.success(request, 'Logged in Successfully')
            return redirect('/')
    return render(request, 'Login_seller.html')


def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        pword = request.POST.get('pword')
        rpword = request.POST.get('rpword')
        if(rpword == pword and len(name) < 10 and len(pword) > 6):
            user = User.objects.create_user(name, email, pword)
            user.save()
            messages.success(request, 'Successfully signed up')
            return redirect('/')
        else:
            if(len(name) > 10):
                messages.error(
                    request, 'Username should be less than 10 characters')
            elif(len(pword) < 6):
                messages.error(
                    request, 'Password should contain a minimum of 7 characters')
            else:
                messages.error(request, 'Your account couldn\'t be created')
    return render(request, 'sign-up.html')


def logt(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        desc = request.POST.get("desc")
        if(name.strip() == '' or email.strip() == '' or desc.strip() == ''):
            messages.error(request, 'Document deleted.')
        else:
            contact = Contact(name=name, email=email,
                              desc=desc, date=datetime.today())
            contact.save()
            messages.success(
                request, 'Your form has been successfully recieved')
    return render(request, 'contact.html')
