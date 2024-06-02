
#Image est utilisé pour ouvrir et manipuler les images, tandis que ImageEnhance permet d'améliorer
# la qualité # des images (par exemple, augmenter la luminosité).
from PIL import Image, ImageEnhance, ImageOps
#Cette ligne importe le module pyplot de la bibliothèque matplotlib en le renommant plt.
# pyplot est utilisé pour afficher des graphiques et des images.
import matplotlib.pyplot as plt
#numpy pour les opérations sur les matrices de pixels.
import numpy as np

#*************************************************************************************************#
# Charger l'image
image = Image.open('image.jpeg')
# Afficher l'image
#Cette ligne affiche l'image chargée en utilisant imshow de matplotlib.pyplot
plt.imshow(image)
#Ajouter des axes
plt.axis('on')
#Cette ligne affiche la fenêtre contenant l'image
plt.show()

#*************************************************************************************************#
# Augmenter l'intensité (luminosité) de l'image
# Cette ligne crée un objet Brightness qui peut être utilisé pour ajuster la luminosité de l'image
enhancer = ImageEnhance.Brightness(image)
#Cette ligne ajuste la luminosité de l'image. Le facteur 1.5 signifie que la luminosité est augmentée de 50%
image_enhanced = enhancer.enhance(1.5)  # 1.5 est le facteur d'augmentation de luminosité
# Afficher l'image modifiée
plt.imshow(image_enhanced)
plt.axis('on')
plt.title('Image avec intensité augmentée')
plt.show()
#*************************************************************************************************#
#Diminuer l'intensité
image_reduce = enhancer.enhance(0.7)
plt.imshow(image_reduce)
plt.axis('on')
plt.title('Image avec intensité diminuée')
plt.show()

#*************************************************************************************************#
#Pour obtenir le négatif de l'image, nous devons inverser les valeurs des pixels. Si un pixel a une valeur de (R, G, B),
# nous le convertirons en (255 - R, 255 - G, 255 - B).
# Convertir l'image en négatif
image_negative = ImageOps.invert(image_reduce.convert('RGB'))

# Afficher l'image en négatif
plt.imshow(image_negative)
plt.axis('on')
plt.title('Image en négatif')
plt.show()


#*************************************************************************************************#
#convertire l'image en une matrice de pixels
#np.array(image, dtype=np.float32) : Convertit l'image en une matrice de valeurs de pixels
# avec des valeurs en flottants pour permettre les calculs.
image_array = np.array(image_reduce, dtype=np.float32)

#Appliquer la transformation logarithmique
c = 255 / np.log(1 + np.max(image_array))
log_image_array = c * np.log(1 + image_array)
#    c = 255 / np.log(1 + np.max(image_array)) : Calcule une constante de normalisation pour que les valeurs
#    de pixels restent dans la plage [0, 255].
#log_image_array = c * np.log(1 + image_array) : Applique la transformation logarithmique aux valeurs de pixels.

#Convertir la matrice de valeurs de pixels en image
log_image_array = np.clip(log_image_array, 0, 255).astype(np.uint8)
log_image = Image.fromarray(log_image_array)

plt.imshow(log_image)
plt.axis('on')
plt.title('Image avec contraste logarithmique')
plt.show()