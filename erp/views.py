from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import  login_required
from django.contrib.auth.models import User
from .models import Sold_product, Product, Category
from .forms import AddCategoryForm, AddproductForm, AddsaleForm, RegisterForm, LoginForm

import requests
import json
# Create your views here.
@login_required(login_url='login')
def dasborad(request):
    total_product = Product.objects.count()
    total_oder = Sold_product.objects.count()
    return render(request, 'dashboard.html', {'tt_pro': total_product, 'tt_order': total_oder})
@login_required(login_url='/')
def addproduct(request):
    if request.method == 'POST':
        form = AddproductForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.owner = request.user
            form.save()
            messages.success(request, "ເພີ່ມສະນຄ້າສຳເລັດ")
            return redirect('product')
    else:
        form = AddproductForm()
        return render(request, 'stock.html', {'forms': form})
    
@login_required(login_url='/')
def showproduct(request):
    showdata = Product.objects.all().order_by('-created')
    return render(request, 'allstock.html', {'data': showdata})

@login_required(login_url='/')
def deleteproduct(request, id):
    prod = Product.objects.get(id=id)
    prod.delete()
    return redirect('allproduct')

@login_required(login_url='/')
def detail_view(request, id):
    context = Product.objects.get(id = id)
    return render(request, "detail_view.html", {'data':context})

@login_required(login_url='/')
def edit_product(request, id):
    form = get_object_or_404(Product, id=id)
    if request.method == 'GET':
        form = {'form': AddproductForm(instance=form), 'id': id}
        return render(request,'editproduct.html',form)   
    elif request.method == 'POST':
        form = AddproductForm(request.POST, request.FILES, instance=form)
        if form.is_valid():
            form.save()
            messages.success(request, 'ອັບເດດສພເລັດ')
            return redirect('allproduct')
        

@login_required(login_url='/')
def category(request):
    if request.method == 'POST':
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "ປ້ອນປະເພດສິນຄ້າສຳເລັດ")
            return redirect('category')      
    else:
        form = AddCategoryForm()
    return render(request, 'category.html', {'forms': form})


@login_required(login_url='/')
def showcategory(request):
    showdata = Category.objects.all()
    return render(request, 'categorylist.html', {'data': showdata})

@login_required(login_url='/')
def deletecate(request, id):
    cate = Category.objects.get(id=id)
    cate.delete()
    messages.error(request, "ລຶບສຳເລັດ")
    return redirect('allcate')

@login_required(login_url='/')
def saleproduct(request):
    if request.method == 'POST':
        form = AddsaleForm(request.POST)
        if form.is_valid():
            owner = request.user
            product = form.cleaned_data['product']
            available_quantity = form.cleaned_data['available_quantity']
            price = form.cleaned_data['price']
            total_price = form.cleaned_data['total_price']
            if product.available_quantity >= available_quantity:
                order = Sold_product(owner=owner, product=product, available_quantity=available_quantity, price=price,  total_price=total_price)
                order.save()
                product.available_quantity -= available_quantity
                product.save()
                messages.success(request, "ຂ່າຍສຳເລັດ")
                return redirect('sale')
            else:
                messages.warning(request, "ສິນຄ້າບໍພໍ")
                return render(request, 'sale.html', {'saleform': form})
    else:
        form = AddsaleForm()
        return render(request, 'sale.html', {'saleform': form})
@login_required(login_url='/')    
def salereport(requests):
    form = Sold_product.objects.all()
    return render(requests, 'salelist.html', {'form': form})
    
def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'register.html', { 'form': form})
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'ທ່ານສະໝັກສະມາຊິກສຳເລັດ.')
            login(request, user)
            return redirect('dasborad')
        else:
            return render(request, 'register.html', {'form': form})

def sign_in(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request,'login.html', {'form': form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password=form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                messages.success(request,f'ຍິນດີຕ້ອນຮັບ: {username.title()}')
                return redirect('dasborad')
                # either form not valid or user is not authenticated
        messages.error(request,f'Invalid username or password')
        return render(request,'login.html',{'form': form})
  
def sign_out(request):
    logout(request)
    messages.success(request,'ທ່ານ ໄດ້ອອກຈາກລະບົບແລ້ວ.')
    return redirect('/')  


