from PIL import Image
import numpy as np
import ipywidgets as widgets
from IPython.display import display
from io import BytesIO

import matplotlib.pyplot as plt

def log_transform(image_array, alpha):
    c = 255 / np.log(1 + alpha * np.max(image_array))
    log_image = c * (np.log(1 + alpha * image_array))
    log_image = np.array(log_image, dtype=np.uint8)
    return log_image

def apply_negative(image_array):
    return 255 - image_array

def update_image(change=None):
    alpha = alpha_slider.value
    log_image_array = log_transform(image_array, alpha)
    if negative_button.value:
        log_image_array = apply_negative(log_image_array)
    log_image = Image.fromarray(log_image_array)
    bio = BytesIO()
    log_image.save(bio, format='PNG')
    log_image_widget.value = bio.getvalue()

# Charger l'image
image_path = 'image.jpeg'  # Remplacez par le chemin de votre image
image = Image.open(image_path).convert('L')  # Convertir en niveaux de gris
image_array = np.array(image)

# Initialiser le slider et le bouton
alpha_slider = widgets.FloatSlider(value=1.0, min=0.1, max=5.0, step=0.05, description='Alpha:')
alpha_slider.observe(update_image, names='value')

negative_button = widgets.ToggleButton(value=False, description='Négatif')
negative_button.observe(update_image, names='value')

# Créer un widget d'image
bio = BytesIO()
image.save(bio, format='PNG')
log_image_widget = widgets.Image(value=bio.getvalue(), format='png')

# Afficher le slider, le bouton et l'image
display(alpha_slider, negative_button, log_image_widget)


#*************************************************************************************************#

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

def apply_clahe(image_array, clip_limit):
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=(8, 8))
    clahe_image = clahe.apply(image_array)
    return clahe_image

def update_image(change=None):
    alpha = alpha_slider.value
    clip_limit = clip_limit_slider.value
    log_image_array = log_transform(image_array, alpha)
    if contrast_button.value:
        log_image_array = apply_clahe(log_image_array, clip_limit)
    if negative_button.value:
        log_image_array = apply_negative(log_image_array)
    log_image = Image.fromarray(log_image_array)
    bio = BytesIO()
    log_image.save(bio, format='PNG')
    log_image_widget.value = bio.getvalue()

# Charger l'image
image_path = 'image_alex.jpg'  # Remplacez par le chemin de votre image
image = Image.open(image_path).convert('L')  # Convertir en niveaux de gris
image_array = np.array(image)

# Initialiser le slider et les boutons
alpha_slider = widgets.FloatSlider(value=1.0, min=0.1, max=10.0, step=0.1, description='Alpha:')
alpha_slider.observe(update_image, names='value')

clip_limit_slider = widgets.FloatSlider(value=2.0, min=1.0, max=10.0, step=0.1, description='Clip Limit:')
clip_limit_slider.observe(update_image, names='value')

contrast_button = widgets.ToggleButton(value=False, description='CLAHE')
contrast_button.observe(update_image, names='value')

negative_button = widgets.ToggleButton(value=False, description='Négatif')
negative_button.observe(update_image, names='value')

# Créer un widget d'image
bio = BytesIO()
image.save(bio, format='PNG')
log_image_widget = widgets.Image(value=bio.getvalue(), format='png')

# Afficher le slider, les boutons et l'image
display(alpha_slider, clip_limit_slider, contrast_button, negative_button, log_image_widget)

#*************************************************************************************************#
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


#*************************************************************************************************#

import cv2
from PIL import Image
import numpy as np
import ipywidgets as widgets
from IPython.display import display
from io import BytesIO
from skimage.util import img_as_ubyte
from skimage import filters, morphology, segmentation, feature
import matplotlib.pyplot as plt

def log_transform(image_array, alpha):
    c = 255 / np.log(1 + alpha * np.max(image_array))
    log_image = c * (np.log(1 + alpha * image_array))
    log_image = np.array(log_image, dtype=np.uint8)
    return log_image

def apply_negative(image_array):
    return 255 - image_array

def apply_clahe(image_array, clip_limit):
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=(8, 8))
    clahe_image = clahe.apply(image_array)
    return clahe_image

def apply_gamma_correction(image_array, gamma):
    inv_gamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** inv_gamma) * 255 for i in np.arange(0, 256)]).astype(np.uint8)
    return cv2.LUT(image_array, table)

def apply_threshold(image_array, threshold):
    _, thresh_image = cv2.threshold(image_array, threshold, 255, cv2.THRESH_BINARY)
    return thresh_image

def skull_stripping(image, se_closing, se_erosion, skull_remove_area=2000, show_pipeline=False):
    threshold_value = filters.threshold_otsu(image)
    binary_image = image > threshold_value
    filled_image = morphology.remove_small_holes(binary_image, area_threshold=skull_remove_area)
    eroded_image = morphology.erosion(filled_image, se_erosion)
    skull_stripped_image = np.where(eroded_image, image, 0)
    return img_as_ubyte(skull_stripped_image)

def update_image(change=None):
    alpha = alpha_slider.value
    gamma = gamma_slider.value
    clip_limit = clip_limit_slider.value
    threshold = threshold_slider.value

    log_image_array = log_transform(image_array, alpha)

    if contrast_button.value:
        log_image_array = apply_clahe(log_image_array, clip_limit)
    elif gamma_button.value:
        log_image_array = apply_gamma_correction(log_image_array, gamma)

    if negative_button.value:
        log_image_array = apply_negative(log_image_array)

    if skull_stripping_button.value:
        log_image_array = skull_stripping(log_image_array, se_closing=morphology.disk(30), se_erosion=morphology.disk(16))

    log_image_array = apply_threshold(log_image_array, threshold)

    log_image = Image.fromarray(log_image_array)
    bio = BytesIO()
    log_image.save(bio, format='PNG')
    log_image_widget.value = bio.getvalue()

# Charger l'image
image_path = 'image_alex.jpg'  # Remplacez par le chemin de votre image
image = Image.open(image_path).convert('L')  # Convertir en niveaux de gris
image_array = np.array(image)

# Initialiser le slider et les boutons
alpha_slider = widgets.FloatSlider(value=1.0, min=0.1, max=10.0, step=0.1, description='Alpha:')
alpha_slider.observe(update_image, names='value')

gamma_slider = widgets.FloatSlider(value=1.0, min=0.1, max=5.0, step=0.1, description='Gamma:')
gamma_slider.observe(update_image, names='value')

clip_limit_slider = widgets.FloatSlider(value=2.0, min=1.0, max=10.0, step=0.1, description='Clip Limit:')
clip_limit_slider.observe(update_image, names='value')

threshold_slider = widgets.IntSlider(value=128, min=0, max=255, step=1, description='Threshold:')
threshold_slider.observe(update_image, names='value')

contrast_button = widgets.ToggleButton(value=False, description='CLAHE')
contrast_button.observe(update_image, names='value')

gamma_button = widgets.ToggleButton(value=False, description='Gamma Correction')
gamma_button.observe(update_image, names='value')

negative_button = widgets.ToggleButton(value=False, description='Négatif')
negative_button.observe(update_image, names='value')

skull_stripping_button = widgets.ToggleButton(value=False, description='Skull Stripping')
skull_stripping_button.observe(update_image, names='value')

# Créer un widget d'image
bio = BytesIO()
image.save(bio, format='PNG')
log_image_widget = widgets.Image(value=bio.getvalue(), format='png')

# Afficher le slider, les boutons et l'image
display(alpha_slider, gamma_slider, clip_limit_slider, threshold_slider, contrast_button, gamma_button, negative_button, skull_stripping_button, log_image_widget)




