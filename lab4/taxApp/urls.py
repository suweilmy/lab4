from django.urls import path
from . import views

urlpatterns =[
    path("" , views.index , name = "index"),
    path("<int:number>" , views.calculateTax, name="calcualteTax"),
    path("taxrate/" , views.Tax_Rate,name="Tax Rate")
]