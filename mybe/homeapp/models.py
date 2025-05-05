from django.db import models
from ckeditor.fields import RichTextField


class Labo_langue(models.Model):
    name = models.CharField(max_length=200,db_index=True)
    description = RichTextField()


    def __str__(self) -> str:
        return self.name


class Temoignage(models.Model):
    nom_prenom = models.CharField(max_length=100, verbose_name="Nom et Prénom")
    photo = models.ImageField(upload_to='temoignages/photos/', blank=True, null=True, verbose_name="Photo")
    profession = models.CharField(max_length=100, verbose_name="Profession")
    message = models.TextField(verbose_name="Message")
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    approuve = models.BooleanField(default=False, verbose_name="Approuvé")

    def __str__(self):
        return f"Témoignage de {self.nom_prenom}"

    class Meta:
        verbose_name = "Témoignage"
        verbose_name_plural = "Témoignages"

class Contact(models.Model):
    
    name = models.CharField(max_length=100, verbose_name="Nom et Prénom",db_index=True)
    email = models.EmailField(verbose_name="Email",db_index=True)
    subject = models.CharField(max_length=200, verbose_name="Sujet",db_index=True)
    message = models.TextField(verbose_name="Message",db_index=True)
    # Champ pour la date de création (rempli automatiquement)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création",db_index=True)

    def __str__(self):
        """
        Représentation en chaîne de caractères de l'objet.
        """
        return f"Message de {self.name} - {self.subject}"

    class Meta:
        """
        Métadonnées pour le modèle.
        """
        verbose_name = "Message de contact"  # Nom singulier dans l'admin
        verbose_name_plural = "Messages de contact"  # Nom pluriel dans l'admin