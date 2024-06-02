import cv2
import numpy as np
import matplotlib.pyplot as plt

# Fonction pour afficher l'image et récupérer les coordonnées de la graine au clic
def get_seed_point(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        param.append((y, x))  # Ajouter les coordonnées de la graine

# Fonction de segmentation par région croissante
def region_growing(image, seed, threshold=5):
    h, w = image.shape
    segmented = np.zeros_like(image, dtype=np.uint8)
    visited = np.zeros_like(image, dtype=bool)

    stack = [seed]
    seed_value = image[seed]
    segmented[seed] = 255
    visited[seed] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    while stack:
        x, y = stack.pop()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w and not visited[nx, ny]:
                if abs(int(image[nx, ny]) - int(seed_value)) < threshold:
                    segmented[nx, ny] = 255
                    stack.append((nx, ny))
                visited[nx, ny] = True

    return segmented

# Étape 1 : Importer l'image .jpg
image_path = 'image.jpg'  # Remplacez par le chemin de votre image
image = cv2.imread(image_path)

# Vérifier si l'image a été correctement chargée
if image is None:
    raise ValueError(f"Image at {image_path} could not be loaded.")

# Étape 2 : Convertir l'image en niveaux de gris
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Afficher l'image et demander à l'utilisateur de cliquer pour sélectionner la graine
seed = []
plt.imshow(gray_image, cmap='gray')
plt.title('Image en niveaux de gris')
plt.axis('off')
plt.show()

cv2.setMouseCallback('Image en niveaux de gris', get_seed_point, seed)
cv2.waitKey(0)

# Vérifier si la graine a été sélectionnée
if len(seed) == 0:
    raise ValueError("Aucune graine sélectionnée.")

seed = seed[0]

# Étape 3 : Appliquer la segmentation par région croissante
threshold_value = 5  # Définir le seuil pour l'extension de la région
segmented_image = region_growing(gray_image, seed, threshold_value)

# Étape 4 : Afficher l'image segmentée
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title("Image Originale")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # Convertir BGR en RGB pour l'affichage
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title(f"Image Segmentée avec seuil = {threshold_value}")
plt.imshow(segmented_image, cmap='gray')
plt.axis('off')

plt.show()

