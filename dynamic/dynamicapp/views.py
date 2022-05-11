from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "index.html")


# code form online

# Create your views here.
def home(request):
    return render(request, "home.html")


# Create your views here.
def added(request):
    return render(request, "added.html")


# "GET" counter method by GET
def counter(request):
    text = request.GET['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})


# "POST" counter method by POST
def other(request):
    text = request.POST['text']
    amount_of_digits = len(text.split())
    return render(request, 'other.html', {'amount': amount_of_digits})


# Create SUM FUNCTION CONVERT STRING  TO INTEGER
def welcome(request):
    t = request.GET['text']
    n=int(t)
    sum=0
    while n>0:
        d=n%10
        sum=sum+d
        n= n//10
    return render(request, "welcome.html", {'sod':sum})


