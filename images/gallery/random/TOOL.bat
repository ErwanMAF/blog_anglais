@echo off
setlocal enabledelayedexpansion

:: Définir un fichier de sortie
set output_file=fichiers_liste.txt

:: Supprimer le fichier précédent s'il existe
if exist %output_file% del %output_file%

:: Parcourir tous les fichiers dans le dossier courant
for %%f in (*.*) do (
    echo '%%f', >> %output_file%
)

:: Afficher un message de fin
echo Liste des fichiers écrite dans %output_file%.
pause
