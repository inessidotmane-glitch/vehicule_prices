from pathlib import Path
import pandas as pd

# Racine du projet
BASE_DIR = Path(__file__).resolve().parent.parent

# Chemins
input_path = BASE_DIR / "data" / "raw" / "Vehicle Price.csv"
output_path = BASE_DIR / "data" / "processed" / "vehicle_clean.csv"

# Lecture du CSV
df = pd.read_csv(input_path)

# Colonnes inutiles pour un premier modèle
cols_to_drop = [
    "name",
    "description",
    "trim",
    "engine",
    "exterior_color",
    "interior_color"
]

df = df.drop(columns=cols_to_drop, errors="ignore")

# On retire les lignes sans target
df = df.dropna(subset=["price"])

# Remplissage des variables numériques
if "mileage" in df.columns:
    df["mileage"] = df["mileage"].fillna(df["mileage"].median())

if "cylinders" in df.columns:
    df["cylinders"] = df["cylinders"].fillna(df["cylinders"].median())

# Remplissage des variables catégorielles
categorical_cols = ["make", "model", "fuel", "transmission", "body", "drivetrain", "doors"]
for col in categorical_cols:
    if col in df.columns and not df[col].mode().empty:
        df[col] = df[col].fillna(df[col].mode()[0])

# Supprimer doublons éventuels
df = df.drop_duplicates()

# Crée le dossier processed s'il n'existe pas
output_path.parent.mkdir(parents=True, exist_ok=True)

# Sauvegarde
df.to_csv(output_path, index=False)

print("Fichier nettoyé créé :", df.shape)
print("Fichier sauvegardé ici :", output_path)