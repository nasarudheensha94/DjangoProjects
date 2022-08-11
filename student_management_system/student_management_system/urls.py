
from django.contrib import admin
from django.urls import path
from django.conf import settings  # import setting
from django.conf.urls.static import  static

from .import views,Hod_views,Staff_views,Student_views

urlpatterns = [
        path('admin/', admin.site.urls),
        path('base/', views.BASE,name='base'),


        # Login and Logout Path
        path('',views.LOGIN,name='login'),
        path('doLogin',views.doLogin,name='doLogin'),
        path('doLogout',views.doLogout,name='logout'),

        #Profile Update
        path('profile',views.PROFILE, name='profile'),
        path('profile/update',views.PROFILE_UPDATE, name='profile_update'),


        #This is HOD panel url
        path('Hod/Home',Hod_views.HOME,name='hod_home'),
        path('Hod/Student/Add',Hod_views.ADD_STUDENT,name='add_student'),
        path('Hod/Student/View',Hod_views.VIEW_STUDENT,name='view_student'),
        path('Hod/Student/Edit/<str:id>',Hod_views.EDIT_STUDENT,name='edit_student'),#<str:id> for get id to edit
        path('Hod/Student/Update',Hod_views.UPDATE_STUDENT,name='update_student'),#hidden id required
        path('Hod/Student/Delete/<str:admin>',Hod_views.DELETE_STUDENT,name='delete_student'),

        #Add Staff views
        path('Hod/Staff/Add',Hod_views.ADD_STAFF,name='add_staff'),
        path('Hod/Staff/View',Hod_views.VIEW_STAFF,name='view_staff'),
        path('Hod/Staff/Edit/<str:id>',Hod_views.EDIT_STAFF,name='edit_staff'),#<str:id> for get id to edit
        path('Hod/Staff/Update',Hod_views.UPDATE_STAFF,name='update_staff'),#hiddne id requred
        path('Hod/Staff/Delete/<str:admin>',Hod_views.DELETE_STAFF,name='delete_staff'),#here will send admin id to delete staff


        #add course in HOD
        path('Hod/course/Add',Hod_views.ADD_COURSE,name='add_course'),
        path('Hod/course/View',Hod_views.VIEW_COURSE,name='view_course'),
        path('Hod/course/Edit/<str:id>',Hod_views.EDIT_COURSE,name='edit_course'),#<str:id> for get id to edit
        path('Hod/course/Update',Hod_views.UPDATE_COURSE,name='update_course'),#hidden id required
        path('Hod/course/Delete/<str:id>',Hod_views.DELETE_COURSE,name='delete_course'),

        #Add subject session
        path('Hod/Subject/Add',Hod_views.ADD_SUBJECT,name='add_subject'),
        path('Hod/Subject/View',Hod_views.VIEW_SUBJECT,name='view_subject'),
        path('Hod/Subject/Edit/<str:id>',Hod_views.EDIT_SUBJECT,name='edit_subject'),
        path('Hod/Subject/Update', Hod_views.UPDATE_SUBJECT, name='update_subject'),
        path('Hod/Subject/Delete/<str:id>', Hod_views.DELETE_SUBJECT, name='delete_subject'),

        # Add session
        path('Hod/Session/Add', Hod_views.ADD_SESSION, name='add_session'),
        path('Hod/Session/View', Hod_views.VIEW_SESSION, name='view_session'),
        path('Hod/Session/Edit/<str:id>', Hod_views.EDIT_SESSION, name='edit_session'),
        path('Hod/Session/Update', Hod_views.UPDATE_SESSION, name='update_session'),
        path('Hod/Session/Delete/<str:id>', Hod_views.DELETE_SESSION, name='delete_session'),

        #Hod Notification for Staff and Students
        path('Hod/Staff/Send_Notification',Hod_views.STAFF_SEND_NOTIFICATION,name='staff_send_notification'),
        path('Hod/Staff/Save_Notification',Hod_views.SAVE_STAFF_NOTIFICATION,name='save_staff_notification'),

        #Student  Notification and Leave Approve and disapprove from HOD
        path('Hod/Student/Send_Notification',Hod_views.STUDENT_SEND_NOTIFICATION,name='student_send_notification'),
        path('Hod/Student/Save_Notification',Hod_views.SAVE_STUDENT_NOTIFICATION,name='save_student_notification'),

        #student Leave Approve and disapprove
        path('Hod/Student/Leave_view',Hod_views.STUDENT_LEAVE_VIEW,name='student_leave_view'),
        path('Hod/Student/approve_leave/<str:id>', Hod_views.STUDENT_APPROVE_LEAVE,name='student_approve_leave'),
        path('Hod/Student/disapprove_leave/<str:id>', Hod_views.STUDENT_DISAPPROVE_LEAVE,name='student_disapprove_leave'),

                      #Hod Staff Leave
        path('Hod/Staff/Leave_view', Hod_views.STAFF_LEAVE_VIEW,name='staff_leave_view'),
        path('Hod/Staff/approve_leave/<str:id>', Hod_views.STAFF_APPROVE_LEAVE,name='staff_approve_leave'),
        path('Hod/Staff/disapprove_leave/<str:id>', Hod_views.STAFF_DISAPPROVE_LEAVE, name='staff_disapprove_leave'),
         # Hod Staff Feedback
        path('Hod/Staff/feedback', Hod_views.STAFF_FEEDBACK, name='staff_feedback_reply'),
        path('Hod/Staff/feedback/save', Hod_views.STAFF_FEEDBACK_SAVE, name='staff_feedback_reply_save'),
        # Hod Student Feedback
        path('Hod/Student/feedback', Hod_views.STUDENT_FEEDBACK, name='get_student_feedback'),
        path('Hod/Student/feedback/reply/save', Hod_views.REPLY_STUDENT_FEEDBACK, name='reply_student_feedback'),

                      #This is STAFF Url
        path('Staff/Home',Staff_views.HOME,name='staff_home'),#this url goes to redirect views staff_home
        path('Staff/Notifications',Staff_views.NOTIFICATIONS,name = 'notifications'),
        path('Staff/mark_as_done/<str:status>', Staff_views.STAFF_NOTIFICATION_MARK_AS_DONE, name='staff_notification_mark_as_done'),
        path('Staff/Apply_leave',Staff_views.STAFF_APPLY_LEAVE,name = 'staff_apply_leave'),
        path('Staff/Apply_leave_save',Staff_views.STAFF_APPLY_LEAVE_SAVE,name = 'staff_apply_leave_save'),
        path('Staff/Feedback',Staff_views.STAFF_FEEDBACK,name = 'staff_feedback'),
        path('Staff/Feedback/Save',Staff_views.STAFF_FEEDBACK_SAVE,name = 'staff_feedback_save'),

        #Staff Take Attendance
        path('Staff/Take_Attendance',Staff_views.STAFF_TAKE_ATTENDANCE,name='staff_take_attendance'),
        path('Staff/Save_Attendance', Staff_views.STAFF_SAVE_ATTENDANCE, name='staff_save_attendance'),
        path('Staff/View_Attendance', Staff_views.STAFF_VIEW_ATTENDANCE, name='staff_view_attendance'),

                      #STUDENT URLS
        path('Student/Home',Student_views.Home,name='student_home'),
        path('Student/Notifications',Student_views.STUDENT_NOTIFICATION,name='student_notification'),
        path('Student/mark_as_done/<str:status>', Student_views.STUDENT_NOTIFICATION_MARK_AS_DONE,name='student_notification_mark_as_done'),
        path('Student/feedback',Student_views.STUDENT_FEEDBACK, name='student_feedback'),
        path('Student/feedback/save',Student_views.STUDENT_FEEDBACK_SAVE,name = 'student_feedback_save'),
        path('Student/apply_for_leave',Student_views.STUDENT_LEAVE,name='student_leave'),
        path('Student/leave_save',Student_views.STUDENT_LEAVE_SAVE,name='student_leave_save'),

              ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)  # MEDIA FILES settings
