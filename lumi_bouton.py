
#***************************************** Intensité Bouton ********************************************************#
import ipywidgets as widgets
from IPython.display import display
from PIL import Image, ImageEnhance
from io import BytesIO

# Fonction pour mettre à jour la luminosité
def update_brightness(change):
    global brightness_factor
    brightened_image = enhancer.enhance(brightness_factor)

    # Convertir l'image en format affichable dans Jupyter
    bio = BytesIO()
    brightened_image.save(bio, format="PNG")
    image_widget.value = bio.getvalue()

# Fonction pour augmenter la luminosité
def increase_brightness(b):
    global brightness_factor
    brightness_factor += 0.05
    update_brightness(None)

# Fonction pour diminuer la luminosité
def decrease_brightness(b):
    global brightness_factor
    brightness_factor -= 0.05
    update_brightness(None)

# Charger l'image
file_path = "image.jpeg"  # Remplacez par le chemin de votre image
image = Image.open(file_path)

# Créer un objet ImageEnhance
enhancer = ImageEnhance.Brightness(image)

# Initialiser le facteur de luminosité
brightness_factor = 1.0

# Créer un widget d'image
bio = BytesIO()
image.save(bio, format="PNG")
image_widget = widgets.Image(value=bio.getvalue(), format='png')

# Créer des boutons pour ajuster la luminosité
increase_button = widgets.Button(description="Increase Brightness")
decrease_button = widgets.Button(description="Decrease Brightness")

# Associer les boutons aux fonctions
increase_button.on_click(increase_brightness)
decrease_button.on_click(decrease_brightness)

# Afficher l'image initiale et les boutons
display(image_widget, increase_button, decrease_button)

# Appel initial pour afficher l'image avec la luminosité de base
update_brightness(None)

