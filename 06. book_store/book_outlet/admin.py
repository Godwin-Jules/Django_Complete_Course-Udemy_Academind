from django.contrib import admin
from .models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}     # Permet de de préremplir certaines colonnes lors de l'ajout ou de la modification d'un champ. C'est l'exemple du slug ...
    list_filter = ('author', 'rating')  # Permet de spécifier les options des filtrage des données dans la panel d'admin
    list_display = ('title', 'author')  # Permet de spécifier les colonnes à afficher dans le panel d'admin

admin.site.register(Book, BookAdmin)
# Pour créer un super utilisateur, on exécute la commande suivante dans le terminal : 'py manage.py createsuperuser' et après on remplit les informatinos nécessaires puis valider. Après la création il faudra redémarrer le serveur ...