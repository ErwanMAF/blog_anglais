import os
import json

# Chemin du dossier principal des images (relatif au script ou projet)
images_dir = 'images'
# Extensions d'images supportées
valid_extensions = ('.png', '.jpg', '.jpeg', '.gif')

# Vérifier si le dossier existe
if not os.path.exists(images_dir):
    print(f"Erreur : Le dossier {images_dir} n'existe pas.")
    exit(1)

# Liste pour stocker tous les fichiers images (avec chemin relatif)
image_files = []

# Parcourir récursivement le dossier et ses sous-dossiers
for root, dirs, files in os.walk(images_dir):
    for file in files:
        if file.lower().endswith(valid_extensions):
            # Construire le chemin relatif à partir du dossier images
            relative_path = os.path.relpath(os.path.join(root, file), os.path.dirname(images_dir))
            # Remplacer les barres obliques inversées par des barres obliques
            relative_path = relative_path.replace(os.sep, '/')
            image_files.append(relative_path)

if not image_files:
    print(f"Erreur : Aucun fichier image trouvé dans {images_dir} ou ses sous-dossiers avec les extensions {valid_extensions}.")
    exit(1)

# Créer le fichier JSON
with open('images.json', 'w') as f:
    json.dump({'symbolList': image_files}, f, indent=2)

print(f'images.json généré avec {len(image_files)} images : {image_files}')
