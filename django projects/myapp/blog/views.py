from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse


def index(request):
    return HttpResponse("Hello, world. You're at the blog index.")

def detail(request, post_id):
    return HttpResponse(f"You're looking at a blog post.{post_id}")

def old_url_redirect(request):
    return redirect(reverse('blog:new_url'))

def new_url_view(request):
    return HttpResponse("This is the new URL view.")