from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import BlogPosts


def index(request):
    
    blog_title = "Latest Posts"
    post1 = BlogPosts()
    post1.id = 1
    post1.title = "My First Post"
    post1.content = "This is my first post. It's not very long."
    post1.category = "Sports"

    post2 = BlogPosts()
    post2.id = 2
    post2.title = "My Second Post"
    post2.content = "This is my second post."
    post2.category = "Entertainment"

    post3 = BlogPosts()
    post3.id = 3
    post3.title = "Another Post"
    post3.content = "This is another post."
    post3.category = "Technology"
    # print([post.id for post in posts])  # Debugging line

    posts = [post1, post2, post3]

    return render(request, "blog/index.html", {"blog_title":  blog_title, "posts": posts})

def detail(request, post_id):
    return render(request, "blog/detail.html")

def old_url_redirect(request):
    return redirect(reverse('blog:new_url'))

def new_url_view(request):
    return HttpResponse("This is the new URL view.")