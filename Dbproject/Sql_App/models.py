from django.db import models
from django.contrib.auth.hashers import make_password # Import make_password FOR Encription

# Create user to DB.
class User(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

#Encript Password Field
    def save(self, *args, **kwargs):
            self.password = make_password(self.password)
            super(User, self).save(*args, **kwargs)

# if we need to add any new fields write above then add in views.py  and migrate required