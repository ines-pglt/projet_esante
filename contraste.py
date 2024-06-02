#******************************************* Contraste Barre ************************************************#
import cv2
import numpy as np
import ipywidgets as widgets
from IPython.display import display

def log_transform(image, alpha):
    c = 255 / np.log(1 + alpha * np.max(image))
    log_image = c * (np.log(1 + alpha * image))
    log_image = np.array(log_image, dtype=np.uint8)
    return log_image

def update_image(change):
    alpha = change['new']
    log_image = log_transform(image, alpha)
    # Convertir l'image pour l'afficher dans un widget
    _, buffer = cv2.imencode('.png', log_image)
    log_image_widget.value = buffer.tobytes()

# Charger l'image
image_path = 'image.jpeg'  # Remplacez par le chemin de votre image
image = cv2.imread(image_path, 0)  # Charger l'image en niveaux de gris

# Initialiser le slider
alpha_slider = widgets.FloatSlider(value=1.0, min=0.1, max=10.0, step=0.1, description='Alpha:')
alpha_slider.observe(update_image, names='value')

# Afficher l'image initiale
_, buffer = cv2.imencode('.png', image)
log_image_widget = widgets.Image(value=buffer.tobytes(), format='png')

display(alpha_slider, log_image_widget)
