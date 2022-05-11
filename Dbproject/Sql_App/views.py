from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import User
from .forms import StudentRegistration #removed Sql_App.forms



# Create for the rendering base function  (ADD & SHOW)
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)#forms reg
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'addandshow.html',{'form':fm,'stu':stud})
# edit until here

#This function will update or edit record.(UPDATE RECORD)
def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request,'updatestudent.html',{'form': fm})



#This function is used to delete record.(DELETE RECORD)
def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
