from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from .models import Posts, About
from django.http import Http404
from django.core.paginator import Paginator
from .forms import ContactForm
# static demo data

# posts = [
#     {'id': 1, 'title': "My First Post", 'content': "This is my first post. It's not very long.", 'category': "Sports"},
#     {'id': 2, 'title': "My Second Post", 'content': "This is my second post.", 'category': "Entertainment"},
#     {'id': 3, 'title': "Another Post", 'content': "This is another post.", 'category': "Technology"}
# ]

def index(request):
    blog_title = "Latest Posts"
    all_posts = Posts.objects.all()

    # pagination
    paginator = Paginator(all_posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "blog/index.html", {"blog_title":  blog_title, "page_obj": page_obj})

def detail(request, slug):
    """
    # get static data post by id
    # post = next(( item for item in posts if item['id'] == int(post_id)), None)
    """

    # get post by id from database
    try:
        post = Posts.objects.get(slug=slug)
        related_posts = Posts.objects.filter(category=post.category).exclude(pk=post.id)
    except Posts.DoesNotExist:
        raise Http404("Post not found.", status=404)
    # logger = logging.getLogger("TESTING")
    # logger.debug(f'Post ID: {post}')
    return render(request, "blog/detail.html", {"post": post, "related_posts": related_posts})

def old_url_redirect(request):
    return redirect(reverse('blog:new_url'))

def new_url_view(request):
    return HttpResponse("This is the new URL view.")

def contact_view(request):
    if request.method == "POST":
        # handle form submission
        form = ContactForm(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if form.is_valid():
            # process the data in form.cleaned_data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Here you would typically send the email or save the data to the database
            # For now, we'll just redirect to a thank you page
            success_message = "Thank you for your message!"
            return render(request, "blog/contact.html", {"form": form, "success_message": success_message})
        else:
            pass    
        return render(request, "blog/contact.html", {"form": form, "name": name, "email": email, "message": message})
    return render(request, "blog/contact.html")

def about_view(request):
    about_content = About.objects.first().content
    return render(request, "blog/about.html", {"about_content": about_content})