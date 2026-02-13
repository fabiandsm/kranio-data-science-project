import sys
import joblib
import pandas as pd
from pathlib import Path


FEATURES = [
    "age",
    "income",
    "purchase_frequency",
    "avg_ticket",
    "recency_days",
    "online_ratio",
    "annual_spend_est",
    "activity_score",
    "digital_score",
    "customer_score",
]


def predict(input_path: Path, output_path: Path):
    print("Cargando modelo...")

    project_root = Path(__file__).resolve().parents[1]
    model_path = project_root / "outputs" / "models" / "retail_model.joblib"

    model = joblib.load(model_path)

    print("Leyendo datos...")
    df = pd.read_csv(input_path)

    missing = [c for c in FEATURES if c not in df.columns]
    if missing:
        raise ValueError(
            "Faltan columnas necesarias:\n" +
            "\n".join(missing)
        )

    X = df[FEATURES]

    print("Generando predicciones...")
    df["predicted_future_sales"] = model.predict(X)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)

    print(f"Predicciones guardadas en: {output_path}")


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Uso: python src/predict.py <archivo_csv>")
        sys.exit(1)

    input_file = Path(sys.argv[1])

    project_root = Path(__file__).resolve().parents[1]
    output_file = (
        project_root /
        "outputs" /
        "predictions" /
        f"{input_file.stem}_predictions.csv"
    )

    predict(input_file, output_file)
