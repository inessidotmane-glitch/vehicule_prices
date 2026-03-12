from pathlib import Path
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

BASE_DIR = Path(__file__).resolve().parent.parent

input_path = BASE_DIR / "data" / "processed" / "vehicle_clean.csv"
model_dir = BASE_DIR / "model"
outputs_dir = BASE_DIR / "outputs"

model_path = model_dir / "model.pkl"
columns_path = model_dir / "columns.pkl"
metrics_path = outputs_dir / "metrics.txt"

model_dir.mkdir(parents=True, exist_ok=True)
outputs_dir.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(input_path)

X = df.drop(columns=["price"])
y = df["price"]

X = pd.get_dummies(X, drop_first=True)

joblib.dump(X.columns.tolist(), columns_path)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred) ** 0.5
r2 = r2_score(y_test, y_pred)

print("MAE :", mae)
print("RMSE :", rmse)
print("R2 :", r2)

joblib.dump(model, model_path)

with open(metrics_path, "w", encoding="utf-8") as f:
    f.write(f"MAE: {mae}\n")
    f.write(f"RMSE: {rmse}\n")
    f.write(f"R2: {r2}\n")

print("Modèle sauvegardé ici :", model_path)
print("Colonnes sauvegardées ici :", columns_path)
print("Métriques sauvegardées ici :", metrics_path)