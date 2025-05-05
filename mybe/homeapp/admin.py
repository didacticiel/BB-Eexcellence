from django.contrib import admin
from .models import Contact, Labo_langue,Temoignage

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Configuration de l'interface d'administration pour le modèle ContactMessage.
    """
    # Liste des champs à afficher dans la liste des messages
    list_display = ('name', 'email', 'subject', 'created_at')
    # Champ pour filtrer les messages dans la liste
    list_filter = ('created_at',)
    # Champ pour rechercher des messages par nom, email ou sujet
    search_fields = ('name', 'email', 'subject')
    # Nombre de messages à afficher par page dans la liste
    list_per_page = 20
    # Ordre par défaut (ici, tri par date de création décroissante)
    ordering = ('-created_at',)
@admin.register(Temoignage)
class TemoignageAdmin(admin.ModelAdmin):
    # Liste des champs à afficher dans la liste des témoignages
    list_display = ('nom_prenom', 'profession', 'date_creation', 'approuve')

    # Filtres pour faciliter la navigation
    list_filter = ('approuve', 'date_creation')

    # Recherche par nom et prénom ou profession
    search_fields = ('nom_prenom', 'profession')

    # Champs modifiables directement depuis la liste
    list_editable = ('approuve',)

    # Pagination : nombre de témoignages par page
    list_per_page = 20

    # Configuration du formulaire d'édition
    fieldsets = (
        (None, {
            'fields': ('nom_prenom', 'profession', 'message', 'photo')
        }),
        ('Validation', {
            'fields': ('approuve',),
            'classes': ('collapse',),
        }),
    )

    # Affichage des témoignages non approuvés en premier
    def get_ordering(self, request):
        return ['approuve', '-date_creation']
    
    
admin.site.register(Labo_langue)