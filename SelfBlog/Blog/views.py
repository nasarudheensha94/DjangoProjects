from django.shortcuts import render, redirect
from .forms import CommentForm
# Create your views here.
from .models import Post
def frontpage(request):
    posts = Post.objects.all() #post from database

    return render(request,'Blog/frontpage.html',{'posts': posts})



def post_detail(request, slug):#this field will refer to models.py > slug = models.SlugField()
    post = Post.objects.get(slug=slug) #this post will go to the front-end

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail',slug=post.slug)
    else:
        form = CommentForm()

    return render(request, 'Blog/post_detail.html',{'post': post, 'form': form})


