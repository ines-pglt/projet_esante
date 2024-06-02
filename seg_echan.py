import cv2
import matplotlib.pyplot as plt

# Étape 1 : Importer l'image .jpg
image_path = 'image_alex.jpg'  # Remplacez par le chemin de votre image
image = cv2.imread(image_path)

# Vérifier si l'image a été correctement chargée
if image is None:
    raise ValueError(f"Image at {image_path} could not be loaded.")

# Étape 2 : Convertir l'image en niveaux de gris
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Affichage initial de l'image et de l'histogramme
plt.figure(figsize=(15, 5))

plt.subplot(1, 2, 1)
plt.title("Image en niveaux de gris")
plt.imshow(gray_image, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Histogramme")
plt.hist(gray_image.ravel(), bins=256, range=[0, 256])
plt.xlabel('Intensité')
plt.ylabel('Nombre de pixels')

plt.show()

# Boucle interactive pour choisir et appliquer le seuil
while True:
    # Étape 3 : Demander à l'utilisateur de saisir un seuil d'intensité
    threshold_value = input("Entrez le seuil d'intensité pour le seuillage (0-255) ou 'exit' pour quitter : ")

    if threshold_value.lower() == 'exit':
        break

    try:
        threshold_value = int(threshold_value)
        if 0 <= threshold_value <= 255:
            # Étape 4 : Appliquer le seuillage
            _, segmented_image = cv2.threshold(gray_image, threshold_value, 255, cv2.THRESH_BINARY)

            # Étape 5 : Afficher l'image segmentée
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
        else:
            print("Veuillez entrer une valeur entre 0 et 255.")
    except ValueError:
        print("Veuillez entrer une valeur numérique valide ou 'exit' pour quitter.")
