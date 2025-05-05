from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    
    
    path('temoignage', temoignage, name="temoignage"),
    path('nos-activites', activite, name="activite"),
    path('nous-contacter', contact, name="contact"),
    path('laboratoir-langue', labo_langue, name="labo_langue"),
    path('faq', faq, name="faq"),
    path('apropos-de-nous', apropos, name="apropos"),
    path('bibliotheques', bilbiotheques, name="bilbiotheques"),
    path('action-socio-sanitaire', action_sociale, name="action_sociale"),
    path('le-social', le_social, name="le_social"),
    


]