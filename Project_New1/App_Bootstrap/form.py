from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):

    class Meta:  #Meta is predefined
        model = User  #Model is Name of database
        fields = ['username', 'email', 'password1', 'password2']


