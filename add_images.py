import os
racine_script = os.path.dirname(os.path.abspath(__file__))
racine_images = os.path.join(racine_script, "images")
gallery_html = os.path.join(racine_script, "gallery.html")

# Dossiers à exclure qui sont **directement sous** racine_images
dossiers_exclus = {"ico", "random", "gif", "index", "profile"}

DEBUT = "<!-- DEBUT_GALERIE -->"
FIN = "<!-- FIN_GALERIE -->"

blocs_html = []

for dossier_courant, dirs, fichiers in os.walk(racine_images):
    # Exclure les dossiers exclus uniquement à la racine
    if os.path.abspath(dossier_courant) == os.path.abspath(racine_images):
        dirs[:] = [d for d in dirs if d not in dossiers_exclus]

    # Ne pas prendre les fichiers dans le dossier racine
    if os.path.abspath(dossier_courant) == os.path.abspath(racine_images):
        continue  # saute les images du dossier racine

    # Traiter les fichiers dans les sous-dossiers (hors exclus)
    for fichier in fichiers:
        if fichier.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            chemin_complet = os.path.join(dossier_courant, fichier)
            chemin_web = os.path.relpath(chemin_complet, start=os.path.dirname(gallery_html)).replace("\\", "/")
            nom_alt = os.path.splitext(fichier)[0].replace("-", " ").replace("_", " ")
            blocs_html.append(f'''<a href="{chemin_web}" data-lightbox="gallery">
  <img src="{chemin_web}" alt="{nom_alt}">
</a>''')

with open(gallery_html, "r", encoding="utf-8") as f:
    contenu = f.read()

parties = contenu.split(DEBUT)
avant = parties[0]
reste = parties[1].split(FIN)
milieu = "\n".join(blocs_html)
apres = reste[1]

nouveau_contenu = avant + DEBUT + "\n" + milieu + "\n" + FIN + apres

with open(gallery_html, "w", encoding="utf-8") as f:
    f.write(nouveau_contenu)

print("✅ gallery.html mis à jour avec images récursives, exclusions et sans images racine.")
