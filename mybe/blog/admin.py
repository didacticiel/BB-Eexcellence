from typing import List
from django.contrib import admin


from .models import *





@admin.register(Post)
class PostAmdin(admin.ModelAdmin):
    list_display = ('title', 'created', 'publish', 'author')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'body')
    ordering = ('author', 'publish')
    list_filter = ('author', 'created', 'publish')
    


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')  # Colonnes affichées dans la liste
    list_filter = ('active', 'created', 'post')  # Filtres disponibles
    search_fields = ('name', 'email', 'body')  # Champs de recherche
    actions = ['approve_comments']  # Actions personnalisées

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
    approve_comments.short_description = "Approuver les commentaires sélectionnés"




admin.site.register(Category)