from .import views
from django.urls import path

urlpatterns = [
    path('', views.dasborad, name='dasborad'),    
    path('product', views.addproduct, name='product'),
    path('category', views.category, name='category'),
    path('sale', views.saleproduct, name='sale'),
    path('allproduct', views.showproduct, name='allproduct'),
    path('delete/<int:id>', views.deleteproduct),
    path('detail/<int:id>', views.detail_view),
    path('allcate', views.showcategory, name='allcate'),
    path('deletecate/<int:id>', views.deletecate),
    path('edit/<int:id>', views.edit_product),
    path('registerpage', views.register, name='registerpage'),
    path('login', views.sign_in, name='login'),
    path('logout', views.sign_out, name='logout'),
    path('salelist', views.salereport, name='salelist'),



] 