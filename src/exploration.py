from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
file_path = BASE_DIR / "data" / "raw" / "Vehicle Price.csv"

print("Chemin utilisé :", file_path)

df = pd.read_csv(file_path)

print(df.head())
print(df.shape)
print(df.columns)