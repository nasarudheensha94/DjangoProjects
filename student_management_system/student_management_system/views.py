from django.shortcuts import render,redirect,HttpResponse
from app.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required #Perfect logout 0  cookies(views and hod_views)
from app.models import CustomUser

def BASE(request):
    return render(request,'base.html')


def LOGIN(request):
    return render(request,'login.html')

#Login Back-end
def doLogin(request):
    if request.method == "POST":
        user = EmailBackEnd.authenticate(request,
                                         username=request.POST.get('email'),
                                         password=request.POST.get('password'),)
        if user!= None:
            login(request, user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('hod_home')
            elif user_type == '2':
                return redirect('staff_home')
            elif user_type == '3':
                return redirect('student_home')
            else:
                messages.error(request,'Email or Password Invalid..!')
                return redirect('login')
        else:
            messages.error(request,'Email or Password Invalid..!')
            return redirect('login')


def doLogout(request):
    logout(request)
    return redirect('login')

#Update Profiles
@login_required(login_url='/')#after upadte password goes to home
def PROFILE(request):
    user = CustomUser.objects.get(id = request.user.id)


    context = {
        "user":user,


    }
    return render(request,'profile.html',context)

@login_required(login_url='/')#after upadte password goes to home
def PROFILE_UPDATE(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
       #email = request.POST.get('email')
        #username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            customuser = CustomUser.objects.get(id = request.user.id)

            customuser.first_name = first_name
            customuser.last_name = last_name

            if password !=None and password != "":
                customuser.set_password(password)
            if profile_pic !=None and profile_pic != "":
                customuser.profile_pic = profile_pic
            customuser.save()
            messages.success(request,"Your Profile Updated Successfully..!")
            return redirect('profile')#after profile update message it will redirect to profile page
        except:
            messages.error(request,'Update Faild')

    return render(request,'profile.html')#profile update wiil post into forms tag in profile.html
