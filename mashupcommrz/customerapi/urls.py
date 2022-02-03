from django.urls import path
from . import views
urlpatterns = [
     path('registercustomer', views.registercustomer, name='registercustomerapi'),
     path('logincustomer', views.logincustomer, name='logincustomerapi'),
     path('logoutcustomer', views.logoutcustomer, name='logoutcustomerapi'),
     path('listproducts', views.listproducts, name='listproductsapi'), 
     path('productdetails', views.productdetails, name='productdetailsapi'),
     path('addproductcart', views.addproductcart, name='addproductcartapi'),
     path('removeproductfromcart', views.removeproductfromcart, name='removeproductfromcartapi'),
     path('listcustomercart', views.listcustomercart, name='listcustomercartapi'),
     ]

# Authorization:Token 8ac3699f22a7d36a4587b59704f56f23ad108708