from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Category, Sold_product,Product

class AddproductForm(forms.ModelForm):
    sku = forms.CharField(widget=forms.TextInput(attrs={"class": "input","type": "text","placeholder": "SKU","class": "form-control",}), label="ຊື່ສິນຄ້າ")
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label="ປະເພດສິນຄ້າ")
    description = forms.CharField(widget=forms.Textarea(attrs={"class": "input","type": "text","placeholder": "SKU","class": "form-control"}), label="ຄຳອະທິບາຍ") 
    price = forms.IntegerField(widget=forms.TextInput(attrs={"class": "input","type": "text","placeholder": "ລາຄາ","class": "form-control"}), label="ລາຄາ")
    available_quantity = forms.IntegerField(widget=forms.TextInput(attrs={"class": "input","type": "text","placeholder": "ຈຳນວນ","class": "form-control"}), label="ຈຳນວນສິນຄ້າ") 
    image = forms.FileField(widget=forms.FileInput(attrs={"class": "input","type": "file","placeholder": "ຮູບພາບ","class": "form-control "}), label="ຮູບພາບ")  

    class Meta:
        model = Product
        fields = ['sku', 'category', 'description', 'price', 'available_quantity', 'image']

class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        
class AddsaleForm(forms.ModelForm):

    product = forms.ModelChoiceField(queryset=Product.objects.all(), label="ລາຍການສິນຄ້າ")
    available_quantity = forms.IntegerField(widget=forms.TextInput(attrs={"class": "input","type": "text","placeholder": "ຈຳນວນ","class": "form-control", "onkeyup": "sum()"}), label="ຈຳນວນສິນຄ້າ")
    price = forms.IntegerField(widget=forms.TextInput(attrs={"class": "input","type": "text","placeholder": "ລາຄາ","class": "form-control", "onkeyup": "sum()"}), label="ລາຄາ")
    total_price = forms.IntegerField(widget=forms.TextInput(attrs={"class": "input","type": "text","id": "txtResult","class": "form-control", "class": "col-2", "placeholder": "ລວມທັ້ງຫມົດ"}), label="ຍອດລວມ")  
    class Meta:
        model = Sold_product
        fields = ['product', 'available_quantity', 'price', 'total_price']
    
class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
          "class": "input",
          "type": "text",
          "placeholder": "ກະລຸນາປ້ອນຊື່ຜູ້ໃຊ້ງານ",
          "class": "form-control"

    }), label="ຊື່ຜູ້ໃຊ້")

    email = forms.EmailField(widget=forms.EmailInput(attrs={
         "class": "input",
          "type": "text",
          "placeholder": "ອີເມວ",
          "class": "form-control"
          
    }), label="ອີເມວ")



    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
         "class": "input",
          "type": "password",
          "placeholder": "ກະລຸນາປ້ອນລະຫັດຜ່ານ",
          "class": "form-control"
          
    }), label="ລະຫັດຜ່ານ")

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
         "class": "input",
          "type": "password",
          "placeholder": "ກະລຸນາປ້ອນລະຫັດຜ່ານອີກຄັ້ງ",
          "class": "form-control"
          
    }), label="ຢື້ນຢັ້ນລະຫັດຜ່ານ")
    class Meta:
        model=User
        fields = ['username','email','password1','password2'] 

class LoginForm(forms.Form):
    username = forms.CharField(max_length=65, label="ຊື່ຜູ້ໃຊ້ງານ")
    password = forms.CharField(max_length=65, widget=forms.PasswordInput, label="ລະຫັດຜ່ານ")
