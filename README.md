# Vehicle Price Prediction Project

## 1. Contexte

Ce projet vise à analyser les facteurs qui influencent le prix des véhicules à partir du dataset **Vehicle-Price.csv**.

L’objectif est double :

- réaliser une **analyse descriptive** pour comprendre les différences de prix entre les véhicules
- construire un **modèle prédictif** capable d’estimer le prix d’un véhicule à partir de ses caractéristiques

Ce projet s’inscrit dans une étude de cas d’analyse de données dans le secteur automobile.

---

# 2. Structure du projet

vehicle_price_project/

data/

raw/ → dataset original

processed/ → données nettoyées

model/

model.pkl → modèle entraîné

columns.pkl → colonnes utilisées

outputs/

metrics.txt → performances du modèle

src/

preprocessing.py → nettoyage des données

train_model.py → entraînement du modèle

evaluate_model.py → évaluation du modèle

---

# 3. Préparation des données

Le dataset contient plusieurs variables décrivant les véhicules :

- marque
- modèle
- année
- carburant
- kilométrage
- transmission
- type de carrosserie
- mode de transmission

Certaines colonnes textuelles très longues ont été supprimées car elles ne sont pas adaptées à un modèle simple :

- name
- description
- trim
- engine
- exterior_color
- interior_color

Les opérations de nettoyage effectuées :

- suppression des lignes sans prix
- remplissage des valeurs manquantes
- suppression des doublons

Les variables numériques manquantes ont été remplacées par la **médiane**, et les variables catégorielles par le **mode**.

---

# 4. Modélisation prédictive

Un modèle de **régression linéaire** a été utilisé pour prédire le prix des véhicules.

Les variables explicatives incluent notamment :

- marque
- modèle
- année
- kilométrage
- carburant
- transmission
- type de carrosserie
- mode de transmission
- nombre de cylindres

Les variables catégorielles ont été transformées avec un **encodage one-hot encoding**.

Les données ont été séparées en :

- **80 % pour l'entraînement**
- **20 % pour le test**

---

# 5. Évaluation du modèle

Les performances du modèle sont évaluées avec trois métriques :

- **MAE (Mean Absolute Error)** : erreur moyenne entre prix réel et prix prédit
- **RMSE (Root Mean Squared Error)** : pénalise davantage les grandes erreurs
- **R² (coefficient de détermination)** : proportion de variance expliquée par le modèle

Les résultats sont enregistrés dans :

outputs/metrics.txt

---

# 6. Utilisation du modèle

Pour reproduire le projet :

### 1. Nettoyer les données

```bash
python src/preprocessing.py
python src/train_model.py
python src/evaluate_model.py
