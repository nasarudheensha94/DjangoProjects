from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home', views.home, name="home"),
    path('register',views.registerUser,name='register'),
    path('login', views.loginUser, name="login"),
    path('frontpage',views.frontpage,name='frontpage'),
    path('<slug:slug>/',views.post_detail,name='post_detail')
    #First slug URL and Second Slug Refers from Views.py def post_detail(re***, slug):
]