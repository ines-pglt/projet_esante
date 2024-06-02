#'ipywidjet' permet de visulaliser le résultat dans le notbook jupyter en créant des widjet interactif
import ipywidgets as widgets
from IPython.display import display#permet d'afficher par la suite des widjet
from PIL import Image, ImageEnhance#pour l'affichage d'image
from io import BytesIO# pour gérer les flux de données en mémoire, utile pour convertir les images
# en un format affichable

#*************************** Début de la fonction ***************************************
def update_brightness(change):#on définit une fonction qui a comme argument change et qui
    # donc sera rapellée à chaque fois que que la valeur de slide (intensité demandée) est modifiée
    factor = change['new'] #extraire la nouvelle variable et la stocker dans la variable factor
    brightened_image = enhancer.enhance(factor)# on ajouste la luminosité de l'image
    #enhancer est un objet ImageEnhance.Brightness, et enhance applique le facteur de luminosité

    # Convertir l'image en format affichable dans Jupyter
    bio = BytesIO()#Crée un objet BytesIO qui agira comme un tampon en mémoire pour stocker l'image modifiée.
    brightened_image.save(bio, format="PNG")# Sauvegarde l'image modifiée dans le tampon bio au format PNG
    image_widget.value = bio.getvalue()#Met à jour la valeur du widget d'image
#*************************** Fin de la fonction ***************************************

# Charger l'image
image = "image.jpeg"  # Spécifie le chemin de l'image à charger
image_upload = Image.open(image) #Ouvre l'image spécifiée par file_path et la stocke dans la variable image

# Créer un objet ImageEnhance
enhancer = ImageEnhance.Brightness(image_upload)

# Créer un widget d'image
bio = BytesIO() #Crée un objet BytesIO qui agira comme un tampon en mémoire pour stocker l'image modifiée.
image_upload.save(bio, format="PNG")
image_widget = widgets.Image(value=bio.getvalue(), format='png')

# Créer un slider pour ajuster la luminosité
slider = widgets.FloatSlider(value=1.0, min=0.1, max=3.0, step=0.05, description='Brightness:')
slider.observe(update_brightness, names='value')

# Afficher l'image initiale et le slider
display(slider, image_widget)

