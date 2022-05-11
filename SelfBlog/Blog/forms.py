from django import forms

from .models import Comment

class CommentForm(forms.ModelForm): #to generates forms.py based on database model
    class Meta:
        model = Comment
        fields = ['name','email','body'] #date_added automaticaly add
