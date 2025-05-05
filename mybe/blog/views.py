import json
import time

from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.decorators.cache import cache_page
from .utils import block_ip
from django.http import HttpResponse
from taggit.models import Tag
from django.db.models import Q  # Pour permettre des recherches sur plusieurs champs



from django.http import HttpResponse, JsonResponse
from django.db.models import Count
from django.http.response import HttpResponseRedirect, StreamingHttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from .models import *
from .forms import CommentForm




# def home(request):
#     return render(request, "blog/index.html")



@cache_page(60 * 15)  # Cache pendant 15 minutes
def post_list(request, category=None, tag_slug=None):
    search_query = request.GET.get('q', '')  # Capture du mot-clé de recherche
    posts = Post.published.all().select_related('category').prefetch_related('tags').order_by('-publish')

    if search_query:
        # Filtrer les posts en fonction du titre, du contenu ou d'autres champs pertinents
        posts = posts.filter(
            Q(title__icontains=search_query) | Q(body__icontains=search_query)
        )
    
    menu_home = Post.objects.filter(section='Menu_home').order_by('-id')[0:1]
    populaire = Post.objects.filter(section='Populaire').order_by('-id')[0:1]
    politique = Post.objects.filter(section='Politique').order_by('-id')[0:1]
    sport = Post.objects.filter(section='Sport').order_by('-id')[0:1]
    
    dernier_posts = Post.published.all().order_by('-publish')[3:6]
    populaires = Post.objects.filter(section='Populaire').order_by('-id')[:3]
    categories = Category.objects.all()
    

    tag = None
    if category:
        category = get_object_or_404(Category, slug=category)
        posts = posts.filter(category=category).order_by("-publish")

    paginator = Paginator(posts, 4)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
        'menu_home': menu_home,
        'populaire': populaire,
        'politique': politique,
        'sport': sport,
        'dernier_posts': dernier_posts,
        'populaires': populaires,
        'page': page,
        'categories': categories,
        'category': category,
        'tag': tag,
        'search_query': search_query,
    }
    return render(request, 'blog/index.html', context)

@cache_page(60 * 15)  # Cache pendant 15 minutes
def detail(request, my_id):
    # Récupération de l'article
    posts = get_object_or_404(Post, id=my_id)

    # Récupération des catégories, articles récents et populaires
    categories = Category.objects.all()
    recent_posts = Post.published.all().order_by('-publish')[:4]
    populaires = Post.objects.filter(section='Populaire').order_by('-id')[:2]

    # Récupération des commentaires actifs
    comments = posts.comments.filter(active=True)

    # Gestion de la soumission des commentaires
    if request.method == 'POST':
        # Extraction des données soumises dans le formulaire
        name = request.POST.get('name')
        email = request.POST.get('email')
        body = request.POST.get('body')

        # Vérification que tous les champs nécessaires sont remplis
        if name and email and body:
            # Création d'un nouvel objet Comment
            new_comment = Comment(
                post=posts,
                name=name,
                email=email,
                body=body
            )
            new_comment.save()
            return redirect('blog:detail', my_id=my_id)

    context = {
        'posts': posts,
        'categories': categories,
        'dernier_posts': recent_posts,
        'populaires': populaires,
        'comments': comments,
    }
    return render(request, 'blog/detail.html', context)

