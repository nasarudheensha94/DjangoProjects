from django.http import HttpResponse
from django.shortcuts import render


# Create MY First Views here.
def index(request):
    name = "Nasarudheensha"  # How to add the value/variable  in to the file
    return render(request, "index.html", {'name': name})  # key and Value


def home(request):
    company = "Shan"  # How to add the value/variable  in to the file
    return render(request, "home.html", {'company': company})  # key and Value


def About(request):
    return render(request, "About.html")

# Create your views here.
