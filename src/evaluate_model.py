from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
metrics_path = BASE_DIR / "outputs" / "metrics.txt"

print("Chemin metrics :", metrics_path)
print("Le fichier existe ?", metrics_path.exists())

with open(metrics_path, "r", encoding="utf-8") as f:
    print(f.read())

print("Interprétation :")
print("- Plus le MAE et le RMSE sont faibles, meilleure est la prédiction.")
print("- Plus le R2 est proche de 1, plus le modèle explique le prix.")