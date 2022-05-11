from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .form import RegisterForm

#Specifiy your templates htmls directories
def index(request):
    return render(request, 'App_Bootstrap/index.html', {})

# Create Register form.
def registerUser(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = RegisterForm()
    return render(request, 'App_Bootstrap/register.html', {'form':form})


# Create Login form.
def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Username or Password is Incorrect')
        else:
            messages.error(request, 'Fill out all the fields')

    return render(request, 'App_Bootstrap/login.html', {})


# Create into Home form.
def home(request):
    return render(request, 'App_Bootstrap/home.html', {})

# Create Logout form.
def logoutUser(request):
    logout(request)
    return redirect('index')

#create Post Blog
def post(request):
    return render(request, 'App_Bootstrap/post.html', {})



