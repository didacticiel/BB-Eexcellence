from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Contact,Labo_langue,Temoignage
from django.core.exceptions import ValidationError
from django.contrib import messages

from django.core.files.images import get_image_dimensions
import os



def home(request):
    # Récupérer les témoignages approuvés
    temoignages = Temoignage.objects.filter(approuve=True)
    return render(request, 'homeapp/index.html', {'temoignages': temoignages})

def temoignage(request):
    if request.method == 'POST':
        # Récupérer les données du formulaire
        nom_prenom = request.POST.get('nom_prenom')
        profession = request.POST.get('profession')
        message = request.POST.get('message')
        photo = request.FILES.get('photo')

        # Validation des champs obligatoires
        if not nom_prenom or not profession or not message:
            messages.error(request, 'Tous les champs obligatoires doivent être remplis.')
            return redirect('temoignage')

        # Validation de la photo (si elle est fournie)
        if photo:
            try:
                # Vérifier que le fichier est une image
                width, height = get_image_dimensions(photo)
                if not width or not height:
                    raise ValidationError("Le fichier n'est pas une image valide.")

                # Vérifier la taille du fichier (par exemple, 5 Mo maximum)
                if photo.size > 5 * 1024 * 1024:  # 5 Mo
                    messages.error(request, 'La photo ne doit pas dépasser 5 Mo.')
                    return redirect('temoignage')

                # Vérifier l'extension du fichier
                allowed_extensions = ['.jpg', '.jpeg', '.png', '.gif']
                ext = os.path.splitext(photo.name)[1].lower()
                if ext not in allowed_extensions:
                    messages.error(request, 'Seuls les fichiers JPG, JPEG, PNG et GIF sont autorisés.')
                    return redirect('temoignage')

            except ValidationError as e:
                messages.error(request, f"Erreur lors de la validation de la photo : {str(e)}")
                return redirect('temoignage')
            except Exception as e:
                messages.error(request, f"Une erreur s'est produite lors du traitement de la photo : {str(e)}")
                return redirect('temoignage')

        # Enregistrer le témoignage dans la base de données
        try:
            temoignage = Temoignage(
                nom_prenom=nom_prenom,
                profession=profession,
                message=message,
                photo=photo if photo else None  # Enregistrer la photo uniquement si elle est fournie
            )
            temoignage.full_clean()  # Valider le modèle avant de l'enregistrer
            temoignage.save()

            messages.success(request, 'Merci pour votre témoignage ! Il sera publié après validation.')
            return redirect('temoignage')

        except ValidationError as e:
            messages.error(request, f"Erreur de validation : {str(e)}")
            return redirect('temoignage')
        except Exception as e:
            messages.error(request, f"Une erreur s'est produite : {str(e)}")
            return redirect('temoignage')

    # Si la méthode n'est pas POST, afficher le formulaire
    return render(request, 'homeapp/temoignage.html')


def bilbiotheques(request):
    return render(request, "homeapp/bibliotheques.html")

def action_sociale(request):
    return render(request, "homeapp/action_sociale.html")

def le_social(request):
    return render(request, "homeapp/le_social.html")

def activite(request):
    return render(request, "homeapp/activite.html")

def faq(request):
    return render(request, "homeapp/faq.html")

def labo_langue(request):
    labo_langues = Labo_langue.objects.all()
    return render(request, "homeapp/labo_langue.html", {'labo_langues': labo_langues})

def contact(request):
    if request.method == 'POST':
        # Récupérer les données du formulaire
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Valider les données (exemple simple)
        if name and email and subject and message:
            # Enregistrer les données dans la base de données
            Contact.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            messages.success(request, 'Votre message a été envoyé avec succès !')
            return redirect('contact')  # Redirige vers la même page après envoi
        else:
            messages.error(request, 'Veuillez remplir tous les champs du formulaire.')

    return render(request, 'homeapp/contact.html')

def apropos(request):
    return render(request, "homeapp/apropos.html")