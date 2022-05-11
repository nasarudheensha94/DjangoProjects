from django.db import models

# Create your models here.
class Post(models.Model):#For DATABASE Models creating here
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField() #For the Front Page.
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)#Every NEW POST WILL AUTOMATICALY UPDATE

    class Meta():
        ordering = ['-date_added'] #decenting order to get every new post


#Comments Section  Database module create

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']



