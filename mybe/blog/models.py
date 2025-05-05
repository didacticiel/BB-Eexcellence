from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')



class Category(models.Model):
    name = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200,db_index=True)

    def __str__(self) -> str:
        return self.name


class Post(models.Model):

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="category_posts",db_index=True)

    SECTION = (

        ('Menu_home','Menu_home'),
        ('Populaire', 'Populaire'),
        ('Politique', 'Politique'),
        ('Societe', 'Societe'),
        ('Culture', 'Culture'),
        ('Sport', 'Sport'),
        ('Economie', 'Economie'),
        ('Sante', 'Sante'),
        ('Education','Education'),
        ('Divertissement','Divertissement'),
        
    )
    title = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200,db_index=True)
    sous_title = models.CharField(max_length=200,db_index=True,blank=True, null=True)
    body = RichTextField()
    image = models.ImageField(upload_to="media",blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=200,db_index=True, default="Bénin Exellence")
    section = models.CharField(choices=SECTION, max_length=20, blank=True, null=True)
    publish = models.DateTimeField(default=timezone.now)

   

    tags = TaggableManager(blank=True) # Tags manager
    
    objects = models.Manager()  # Default manager
    published = PublishedManager()  # Custom manager


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", args=[self.publish.year, self.publish.month, self.publish.day, self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'


class BlockIP(models.Model):
    ip_adress = models.GenericIPAddressField(unique=True)
    blocked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ip_adress