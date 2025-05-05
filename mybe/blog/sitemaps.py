from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Category, Post

class StaticSitemap(Sitemap):
    def items(self):
        return ['post_list','detail','category_post_list']
    
    def location(self, item):
        return reverse(item)
    
    
class CategorySitemap(Sitemap):
    def items(self):
        return Category.objects.all()  
    
    
class PostpageSitemap(Sitemap):
    def items(self):
        return Post.objects.all()[:100]