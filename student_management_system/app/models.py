from django.db import models
from django.contrib.auth.models import AbstractUser #Costomize Admin panel




# Create your models here.


class CustomUser(AbstractUser):
    USER = (
        (1,'HOD'),
        (2, 'STAFF'),
        (3, 'STUDENT'),
    )#Create for 3 type users selection

    user_type = models.CharField(choices=USER,max_length=50,default=1) #user type
    profile_pic = models.ImageField(upload_to='media/profile_pic') # Profile Pic Upload

#Course models
class Course(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name#course will be takes by database


#Session year
class Session_Year(models.Model):
    session_start = models.CharField(max_length=100)
    session_end = models.CharField(max_length=100)

    def __str__(self):
        return self.session_start + " TO " + self.session_end

 #This module retrive into Hod_views.py for students add and views
class Student(models.Model):#id field not mentioned in below Django by default fetchit auto.
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)#there is no profile_mentioned in this class, But profile_pic has provided in CustomUser and it link with students class's 'admin' property .
    address = models.TextField()
    gender = models.CharField(max_length=100)
    course_id =models.ForeignKey(Course,on_delete=models.DO_NOTHING)#here forign-key used from course table and using DO_NOTHING if student delete then course will not delete.
    session_year_id = models.ForeignKey(Session_Year,on_delete=models.DO_NOTHING)#here forign-key used from Session_year
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name


#Staff Database to create
class Staff(models.Model):
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    address = models.TextField(max_length=100)
    gender = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.username


#Subject modle for  Database
class Subject(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


#hod staff Notification Messages db
class Staff_Notification(models.Model):
    staff_id = models.ForeignKey(Staff,on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(null=True,default=0)

    def __str__(self):#if this def __str self not mentioned the it will shows just as object1 object2
        return self.staff_id.admin.first_name #there will pass the first_name of staff from Staff moduel using Custome user module



#STAFF Leave db
class Staff_leave(models.Model):
    staff_id = models.ForeignKey(Staff,on_delete=models.CASCADE)
    data = models.CharField(max_length=150)
    message = models.TextField()
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.staff_id.admin.first_name + self.staff_id.admin.last_name


#Staff Feedback Db
class Staff_Feedback(models.Model):
    staff_id = models.ForeignKey(Staff,on_delete=models.CASCADE)#When the user delelete all his related data will will be remove..!
    feedback = models.TextField()#there is no limit for message length
    feedback_reply = models.TextField() # or youcan use null=true
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.staff_id.admin.first_name + " " + self.staff_id.admin.last_name



#Student Feedback Db
class Student_Notification(models.Model):
    student_id = models.ForeignKey(Student,on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(null=True,default=0)

    def __str__(self):#if this def __str self not mentioned the it will shows just as object1 object2
        return self.student_id.admin.first_name #there will pass the first_name of staff from Staff moduel using Custome user module



#Staff Feedback Db
class Student_Feedback(models.Model):
    student_id = models.ForeignKey(Student,on_delete=models.CASCADE)#When the user delelete all his related data will will be remove..!
    feedback = models.TextField()#there is no limit for message length
    feedback_reply = models.TextField() # or youcan use null=true
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student_id.admin.first_name + " " + self.student_id.admin.last_name


#STUDENT Leave db
class Student_leave(models.Model):
    student_id = models.ForeignKey(Student,on_delete=models.CASCADE)
    data = models.CharField(max_length=150)
    message = models.TextField()
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student_id.admin.first_name + self.student_id.admin.last_name



class Attendance(models.Model):
    subject_id = models.ForeignKey(Subject,on_delete=models.DO_NOTHING)
    attendance_date = models.DateTimeField()
    session_year_id = models.ForeignKey(Session_Year,on_delete= models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject_id.name


class Attendance_Report(models.Model):
    student_id = models.ForeignKey(Student,on_delete=models.DO_NOTHING)
    attendance_id = models.ForeignKey(Attendance,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student_id.admin.first_name