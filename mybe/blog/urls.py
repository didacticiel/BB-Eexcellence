from django.urls import path
from .views import *


app_name = 'blog'

urlpatterns = [

    path('', post_list, name="post_list"),
    path('tag/<slug:tag_slug>/', post_list, name='tag_post_list'),
    path('category/<slug:category>/', post_list, name='category_post_list'),
    path('detail-article/<int:my_id>/', detail, name='detail'),





]