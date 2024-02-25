from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("This is a site to calculate tax")

def calculateTax(request,number):
    tax = 15/100
    total = number+(number*tax)
    return HttpResponse(f"the total price = {total}")

def Tax_Rate(request):
    taxrate = 15/100
    return HttpResponse(f"The tax rate = {taxrate * 100}%")
# Create your views here.
