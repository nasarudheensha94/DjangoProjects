from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required #Perfect logout 0  cookies(views and hod_views)
from app.models import Course,Session_Year,CustomUser,Student,Staff,Subject,Staff_Notification,Staff_leave,Staff_Feedback,Student_Notification,Student_Feedback,Student_leave
from django.contrib import messages

#import pYttsx3
#import webbrowser

@login_required(login_url='/')#import decorators
def HOME(request):
    student_count = Student.objects.all().count()# it will count from Sutdent module and pass to below context dictionary variables
    staff_count = Staff.objects.all().count()
    course_count = Course.objects.all().count()
    subject_count = Subject.objects.all().count()


    student_gender_male = Student.objects.filter(gender = 'Male').count()
    student_gender_female = Student.objects.filter(gender = 'Female').count()




    context = {
        'student_count': student_count,#it will goes to home templates by name
        'course_count':course_count,
        'staff_count':staff_count,
        'subject_count':subject_count,
        'student_gender_female':student_gender_female,
        'student_gender_male':student_gender_male,

    }

    return render(request,'Hod/home.html',context)#this context dictnory will be pass to html templates

@login_required(login_url='/')#Login Required
def ADD_STUDENT(request):
    course = Course.objects.all()
    session_year = Session_Year.objects.all()

    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')

        #student add : user email dupliction to avoid and send message while adding new student
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,"Email Already Taken")
            return redirect("add_student")
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,"This Username Already Taken")
            return redirect("add_student")
        else:
            user = CustomUser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                profile_pic = profile_pic,
                user_type = 3
            )
            user.set_password(password)
            user.save()

            course = Course.objects.get(id=course_id)
            session_year = Session_Year.objects.get(id=session_year_id)

            student = Student(
                admin = user,
                address = address,
                session_year_id = session_year,
                course_id = course,
                gender = gender,
            )
            student.save()
            messages.success(request,user.first_name + "  " + user.last_name + " " + " Added as Student")
            return redirect('add_student')



    context = {
        'course':course,#small letter use
        'session_year':session_year,
    }#Retrieve from Db The Course and session_year
    return render(request,'Hod/add_student.html',context)# context using Retrive from db

@login_required(login_url='/')#Login Required
def VIEW_STUDENT(request):
    student = Student.objects.all()

    #Dictionary creating for template and pass below
    context = {
        'student':student,
    }
    return render(request,'Hod/view_student.html',context)#context dictionary pass here

@login_required(login_url='/')#Login Required
def EDIT_STUDENT(request,id):#edit stduent will based on'id' link in url as str:
    student = Student.objects.filter(id = id)
    course = Course.objects.all()
    session_year = Session_Year.objects.all()
    context = {
        'student':student,
        'course':course,
        'session_year':session_year,

    }
    return render(request,'Hod/edit_student.html',context)

@login_required(login_url='/')#Login Required
def UPDATE_STUDENT(request):
    if request.method == "POST":
        student_id = request.POST.get('student_id')#in user model
        profile_pic = request.FILES.get('profile_pic')#in user model
        first_name = request.POST.get('first_name')#in user model
        last_name = request.POST.get('last_name')#in user model
        email = request.POST.get('email')#in user model
        username = request.POST.get('username')#in user model
        password = request.POST.get('password')#in user model
        address = request.POST.get('address')#in student model
        gender = request.POST.get('gender')#in student model
        course_id = request.POST.get('course_id')#in student model
        session_year_id = request.POST.get('session_year_id')#in student model

        #save updated student in 'user' model
        user = CustomUser.objects.get(id = student_id)

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password != None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        user.save()

        # save updated student in 'user' models
        student = Student.objects.get(admin = student_id)
        student.address = address
        student.gender = gender

        # save updated student in 'student' model
            #'course' & 'sesson' model has created in models.py
        course = Course.objects.get(id = course_id)
        student.course_id = course

        session_year = Session_Year.objects.get(id = session_year_id )
        student.session_year_id = session_year

        student.save()
        messages.success(request,"Record Updated Successfully...!")
        return redirect('view_student')

    return render(request,'Hod/edit_student.html')

@login_required(login_url='/')#Login Required
def DELETE_STUDENT(request,admin):
    student =CustomUser.objects.get(id = admin)
    student.delete()
    messages.warning(request,'Record DELETED Successfully..!')
    return redirect('view_student')

@login_required(login_url='/')#Login Required
def ADD_COURSE(request):
    if request.method == 'POST':
        course_name = request.POST.get('course_name')

        course = Course(
            name = course_name,
        )
        course.save()
        messages.success(request,'Course Created Successfully..!')
        return redirect('view_course')
    return render(request,'Hod/add_course.html')

@login_required(login_url='/')#Login Required
def VIEW_COURSE(request):
    course = Course.objects.all()
    context = {
        'course':course,
    }
    return render(request,'Hod/view_course.html',context)

@login_required(login_url='/')#Login Required
def EDIT_COURSE(request,id):
    course = Course.objects.get(id = id)

    context = {
        'course':course,
    }
    return render(request,'Hod/edit_course.html',context)

@login_required(login_url='/')#Login Required
def UPDATE_COURSE(request):
    if request.method == "POST":
        name = request.POST.get('name')
        course_id = request.POST.get('course_id')

        course = Course.objects.get(id = course_id)
        course.name = name
        course.save()
        messages.success(request,'Course Successfully Updated..!')
        return redirect('view_course')

    return render(request,'Hod/edit_course.html')

@login_required(login_url='/')#Login Required
def DELETE_COURSE(request,id):
    course = Course.objects.get(id = id)
    course.delete()
    messages.success(request,'Course Deleted Successfully')
    return redirect('view_course')

@login_required(login_url='/')#Login Required
def ADD_STAFF(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        # email and username duplication checking...
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email is already in registerd..!')
            return redirect('add_staff')
        # email and username duplication checking...
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username already in registerd..!')
            return redirect('add_staff')

        else:
            user = CustomUser(first_name=first_name, last_name=last_name, email=email,username=username, profile_pic=profile_pic,
                              user_type=2)
            user.set_password(password)
            user.save()

            staff = Staff(
                admin=user,
                address=address,
                gender=gender,
            )
            staff.save()
            messages.success(request, 'Staff Successfully Added..!')
            return redirect('view_staff')


    return render(request,'Hod/add_staff.html')

@login_required(login_url='/')#Login Required
def VIEW_STAFF(request):
    staff = Staff.objects.all()

    context = {
        'staff':staff,

    }

    return render(request,'Hod/view_staff.html',context)

@login_required(login_url='/')#Login Required
def EDIT_STAFF(request,id):#<str:id> send id to edit staff
    staff = Staff.objects.get(id = id)

    context = {
        'staff':staff,
    }
    return render(request,'Hod/edit_staff.html',context)

@login_required(login_url='/')#Login Required
def UPDATE_STAFF(request):
    if request.method == 'POST':
        staff_id = request.POST.get('staff_id')
        profile_pic = request.FILES.get('profile_pic')#in Customuser model
        first_name = request.POST.get('first_name')#in Customuser model
        last_name = request.POST.get('last_name')#in Customuser model
        email = request.POST.get('email')#in Customuser model
        username = request.POST.get('username')#in Customuser model
        password = request.POST.get('password')#in Customuser model
        address = request.POST.get('address')#in staff model
        gender = request.POST.get('gender')#in staff model

        user = CustomUser.objects.get(id = staff_id)
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email

        if password != None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        user.save()

        staff = Staff.objects.get(admin = staff_id)
        staff.gender = gender
        staff.address = address

        staff.save()
        messages.success(request,"Staff data Successfully Updated")
        return redirect('view_staff')

    return render(request,'Hod/edit_staff.html')

@login_required(login_url='/')#Login Required
def DELETE_STAFF(request,admin):# id from admin for delete staff
    staff = CustomUser.objects.get(id = admin)
    staff.delete()
    messages.success(request,"Staff Record Deleted Successfully..!")

    return redirect('view_staff')#here redirct for delete

 #ADD subject session
@login_required(login_url='/')  # Login Required
def ADD_SUBJECT(request):
    course = Course.objects.all()
    staff = Staff.objects.all()

    if request.method == 'POST':
        subject_name = request.POST.get('subject_name')
        course_id = request.POST.get('course_id')
        staff_id = request.POST.get('staff_id')

        course = Course.objects.get(id = course_id)
        staff = Staff.objects.get(id = staff_id)

        subject = Subject(
            name = subject_name,
            course = course,
            staff = staff,
        )
        subject.save()
        messages.success(request,'Subjects Are Added Successfull...!')
        return redirect('add_subject')




    context = {
        'course':course,
        'staff':staff,

    }

    return render(request,'Hod/add_subject.html',context)

@login_required(login_url='/')#Login Required
def VIEW_SUBJECT(request):
    subject = Subject.objects.all()

    context = {
        'subject':subject,
    }

    return render(request,'Hod/view_subject.html',context)

@login_required(login_url='/')#Login Required
def EDIT_SUBJECT(request,id):
    subject = Subject.objects.get(id = id)
    course = Course.objects.all()
    staff = Staff.objects.all()

    context = {

        'subject':subject,
        'course':course,
        'staff':staff,
    }
    return render(request,'Hod/edit_subject.html',context)

@login_required(login_url='/')#Login Required
def UPDATE_SUBJECT(request):
    if request.method == 'POST':
        subject_id = request.POST.get('subject_id')
        subject_name = request.POST.get('subject_name')
        course_id  = request.POST.get('course_id')
        staff_id = request.POST.get('staff_id')

        course = Course.objects.get(id = course_id)
        staff = Staff.objects.get(id = staff_id)

        subject = Subject(
            id = subject_id,
            name = subject_name,
            course = course,
            staff = staff,

        )
        subject.save()
        messages.success(request,"Subject Updated Successfully...!")
        return redirect('view_subject')

@login_required(login_url='/')#Login Required
def DELETE_SUBJECT(request,id):
    subject = Subject.objects.filter(id = id)
    subject.delete()
    messages.success(request,"Subject successfully Deleted...!")
    return redirect('view_subject')

@login_required(login_url='/')#Login Required
def ADD_SESSION(request):
    if request.method == 'POST':
        session_year_start = request.POST.get('session_year_start')
        session_year_end = request.POST.get('session_year_end')

        session = Session_Year(
            session_start = session_year_start,
            session_end = session_year_end,
        )
        session.save()
        messages.success(request,"Session Added Successfully...!")
        return redirect('view_session')

    return render(request,'Hod/add_session.html')

@login_required(login_url='/')#Login Required
def VIEW_SESSION(request):
    session = Session_Year.objects.all()

    context = {
        'session':session,
    }


    return render(request,'Hod/view_session.html',context)

@login_required(login_url='/')#Login Required
def EDIT_SESSION(request,id):
    session = Session_Year.objects.filter(id = id)

    context = {
        'session':session,
    }

    return render(request,'Hod/edit_session.html',context)

@login_required(login_url='/')#Login Required
def UPDATE_SESSION(request):
    if request.method == 'POST':
        session_id = request.POST.get('session_id')#edit_session input field for update
        session_year_start = request.POST.get('session_year_start')
        session_year_end = request.POST.get('session_year_end')


        session = Session_Year(
            id = session_id,
            session_start = session_year_start,
            session_end = session_year_end,

        )
        session.save()
        messages.success(request,"Session Updated Successfully...!")
        return redirect('view_session')#no need render

@login_required(login_url='/')#Login Required
def DELETE_SESSION(request,id):
    session = Session_Year.objects.get(id = id)
    session.delete()
    messages.success(request,"Session Deleted Successfully..!")
    return redirect('view_session')

@login_required(login_url='/')#Login Required
def STAFF_SEND_NOTIFICATION(request):
    staff =Staff.objects.all()
    see_notification = Staff_Notification.objects.all().order_by('-id')[0:10]
    staff_id = Staff.objects.all()

    context = {
        'staff':staff,
        'see_notification':see_notification,
        'staff_id':staff_id,


    }

    return render(request,'Hod/staff_notification.html',context)

@login_required(login_url='/')#Login Required
def SAVE_STAFF_NOTIFICATION(request):
    if request.method == 'POST':
        staff_id = request.POST.get('staff_id')
        message = request.POST.get('message')

        staff = Staff.objects.get(admin = staff_id)
        notification = Staff_Notification(
            staff_id = staff,
            message = message,
        )
        notification.save()
        messages.success(request,"Staff Notification send Successfully...!")
        return redirect('staff_send_notification')

@login_required(login_url='/')#Login Required


def STAFF_LEAVE_VIEW(request):
    staff_leave = Staff_leave.objects.all()

    context = {
        'staff_leave':staff_leave,

    }

    return render(request,'Hod/staff_leave.html',context)


@login_required(login_url='/')#Login Required
def STAFF_APPROVE_LEAVE(request,id):#id get from model
    leave = Staff_leave.objects.get(id = id)
    leave.status = 1 # 1=Approve
    leave.save()
    return redirect('staff_leave_view')

@login_required(login_url='/')#Login Required
def STAFF_DISAPPROVE_LEAVE(request,id):
    leave = Staff_leave.objects.get(id = id)
    leave.status = 2 # 2=Disapprove
    leave.save()
    return redirect('staff_leave_view')

#Student Leave View and related
@login_required(login_url='/')#Login Required
def STUDENT_LEAVE_VIEW(request):
    student_leave = Student_leave.objects.all()

    context = {
        'student_leave': student_leave,

    }
    return render(request,'Hod/student_leave.html',context)



def STUDENT_APPROVE_LEAVE(request,id):
    leave = Student_leave.objects.get(id = id)
    leave.status = 1
    leave.save()
    return redirect('student_leave_view')


def STUDENT_DISAPPROVE_LEAVE(request,id):
    leave = Student_leave.objects.get(id = id)
    leave.status = 2
    leave.save()
    return redirect('student_leave_view')



@login_required(login_url='/')#Login Required
def STAFF_FEEDBACK(request):
    feedback = Staff_Feedback.objects.all()
    feedback_history = Staff_Feedback.objects.all().order_by('-id')[0:10]

    context = {
        'feedback':feedback,
        'feedback_history': feedback_history,

    }

    return render(request,'Hod/staff_feedback.html',context)

@login_required(login_url='/')#Login Required
def STAFF_FEEDBACK_SAVE(request):
    if request.method == "POST":
        feedback_id = request.POST.get('feedback_id')
        feedback_reply = request.POST.get('feedback_reply')

        feedback = Staff_Feedback.objects.get(id = feedback_id )
        feedback.feedback_reply = feedback_reply
        feedback.status = 1
        feedback.save()
        messages.success(request, 'Your feedback Reply has been Send to Staff...!')
    return redirect('staff_feedback_reply')


@login_required(login_url='/')#Login Required
def STUDENT_FEEDBACK(request):
    feedback = Student_Feedback.objects.all()
    feedback_history = Student_Feedback.objects.all().order_by('-id')[0:5] #last five feedbacks will shows

    context = {
        'feedback':feedback,
        'feedback_history':feedback_history,

    }
    return render(request,'Hod/student_feedback.html',context)

@login_required(login_url='/')#Login Required
def REPLY_STUDENT_FEEDBACK(request):
    if request.method == "POST":
        feedback_id = request.POST.get('feedback_id')#student_feedback.html LINE 143 >feedback-id
        feedback_reply = request.POST.get('feedback_reply')#student_feedback.html LINE 144 >feedback-reply

        feedback = Student_Feedback.objects.get(id=feedback_id)
        feedback.feedback_reply = feedback_reply
        feedback.status = 1
        feedback.save()
        messages.success(request, 'Your feedback Reply has been Send to Student...!')
    return redirect('get_student_feedback')

#Student Send Notifications
@login_required(login_url='/')#Login Required
def STUDENT_SEND_NOTIFICATION(request):
    student = Student.objects.all()
    notification = Student_Notification.objects.all().order_by('-id')[0:10]
    student_id = Student.objects.all()

    context = {
        'student':student,
        'notification':notification,
        'student_id':student_id,
    }

    return render(request,'Hod/student_notification.html',context)

@login_required(login_url='/')#Login Required
def SAVE_STUDENT_NOTIFICATION(request):
    if request.method == "POST":
        message = request.POST.get('message')
        student_id = request.POST.get('student_id')

        student = Student.objects.get(admin = student_id)

        stud_notification = Student_Notification(
            student_id = student,
            message = message,
        )
        stud_notification.save()
        messages.success(request,"Student Notification send Successfully...!")
    return redirect('student_send_notification')

