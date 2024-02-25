from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', include("taxApp.urls")),
    path('<int:number>',include("taxApp.urls")),
    path('taxrate/',include("taxApp.urls"))


]

