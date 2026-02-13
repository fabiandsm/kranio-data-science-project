import pandas as pd
from pathlib import Path


def build_features(input_path: Path, output_path: Path):
    print("Construyendo features...")

    df = pd.read_csv(input_path)

    # --- gasto anual estimado ---
    df["annual_spend_est"] = (
        df["purchase_frequency"] *
        df["avg_ticket"] * 12
    )

    # --- score de actividad ---
    df["activity_score"] = (
        df["purchase_frequency"] *
        (1 - df["recency_days"] / 365)
    )

    # --- score digital ---
    df["digital_score"] = df["online_ratio"]

    # --- score total cliente ---
    df["customer_score"] = (
        df["activity_score"] * 0.6 +
        df["digital_score"] * 0.4
    )

    # --- segmentación ---
    df["segment"] = pd.qcut(
        df["customer_score"],
        q=4,
        labels=["Low", "Mid", "High", "Top"]
    )

    output_path.parent.mkdir(exist_ok=True)
    df.to_csv(output_path, index=False)

    print(f"Features guardadas en: {output_path}")


if __name__ == "__main__":
    project_root = Path(__file__).resolve().parents[1]

    input_file = project_root / "data" / "retail_sales_clean.csv"
    output_file = project_root / "data" / "retail_sales_features.csv"

    build_features(input_file, output_file)

