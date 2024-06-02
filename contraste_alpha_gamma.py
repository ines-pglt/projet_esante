import cv2
from PIL import Image
import numpy as np
import ipywidgets as widgets
from IPython.display import display
from io import BytesIO

def log_transform(image_array, alpha):
    c = 255 / np.log(1 + alpha * np.max(image_array))
    log_image = c * (np.log(1 + alpha * image_array))
    log_image = np.array(log_image, dtype=np.uint8)
    return log_image

def apply_negative(image_array):
    return 255 - image_array

def apply_gamma_correction(image_array, gamma):
    inv_gamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** inv_gamma) * 255 for i in np.arange(0, 256)]).astype(np.uint8)
    return cv2.LUT(image_array, table)

def update_image(change=None):
    alpha = alpha_slider.value
    gamma = gamma_slider.value
    log_image_array = log_transform(image_array, alpha)
    if contrast_button.value:
        log_image_array = apply_gamma_correction(log_image_array, gamma)
    if negative_button.value:
        log_image_array = apply_negative(log_image_array)
    log_image = Image.fromarray(log_image_array)
    bio = BytesIO()
    log_image.save(bio, format='PNG')
    log_image_widget.value = bio.getvalue()

# Charger l'image
image_path = 'image.jpg'  # Remplacez par le chemin de votre image
image = Image.open(image_path).convert('L')  # Convertir en niveaux de gris
image_array = np.array(image)

# Initialiser le slider et les boutons
alpha_slider = widgets.FloatSlider(value=1.0, min=0.1, max=10.0, step=0.1, description='Alpha:')
alpha_slider.observe(update_image, names='value')

gamma_slider = widgets.FloatSlider(value=1.0, min=0.1, max=5.0, step=0.1, description='Gamma:')
gamma_slider.observe(update_image, names='value')

contrast_button = widgets.ToggleButton(value=False, description='Gamma Correction')
contrast_button.observe(update_image, names='value')

negative_button = widgets.ToggleButton(value=False, description='Négatif')
negative_button.observe(update_image, names='value')

# Créer un widget d'image
bio = BytesIO()
image.save(bio, format='PNG')
log_image_widget = widgets.Image(value=bio.getvalue(), format='png')

# Afficher le slider, les boutons et l'image
display(alpha_slider, gamma_slider, contrast_button, negative_button, log_image_widget)
