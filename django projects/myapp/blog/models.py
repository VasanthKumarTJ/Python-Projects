from datetime import datetime
from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name  # This is what will be displayed if you print a Category object
    

class Posts(models.Model):
    title = models.CharField(max_length=100)
    img_url = models.URLField(null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title  # This is what will be displayed if you print a Posts object
    
class About(models.Model):
    content = models.TextField()