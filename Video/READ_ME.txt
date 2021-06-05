Pour l'analyse des données vidéo de la base de données 'Honeybee tracking dataset'
https://groups.oist.jp/bptu/honeybee-tracking-dataset

Etape 1: découper les images en imagette grâce à divide_image.py

Etape 2: labellisation des imagettes grâce au site: https://www.makesense.ai/

Etape 3: Mettre les imagettes labellisées dans un dossier 'image', les labels obtenus dans un dossier 'label'

Etape 4: création de la base de données d'entraînement 'obj' et de validation 'test' grâce à 'repartition_aleatoire.py'. 
Compresser les deux dossier 'obj' et 'test' obtenus.

Etape 5: lancer l'apprentissage ou les prédictions en ouvrant 'FIBEE_video.ipynb' avec Google Colab (pour une utilisation rapide: modifier, paramètres du Notebook, 
et mettre GPU dans la case 'accélérateur matériel'). Recommandé:
Dans votre Drive, créer un dossier 'yolov4'. Dedans, importer les fichiers du dossier Github 'Video'; créer un sous-dossier backup pour 
enregistrer les poids lors de l'apprentissage; images_pred pour mettre les images sur lesquelles on veut faire des prédictions; 
video_pred pour mettre les vidéos sur lesquelles on veut faire des prédictions.

A l'intention des professeurs du pôle projet IENV
Pour avoir les poids de notre modèle (fichiers trop gros pour être stockés sur Github), voir dans Teams. Idem pour notre base de données d'images annotée. 

Si des indications plus précises sont désirées, regardez: https://github.com/theAIGuysCode/YOLOv4-Cloud-Tutorial
Un grand merci d'ailleurs à the AIGuy pour son travail d'explication et de vulgarisation!

