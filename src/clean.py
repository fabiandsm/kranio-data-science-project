import pandas as pd
from pathlib import Path


def clean_data(input_path: Path, output_path: Path):
    print("Cargando datos...")

    df = pd.read_csv(input_path)

    print("Filas originales:", len(df))

    # --- eliminar duplicados ---
    df = df.drop_duplicates()

    # --- valores negativos imposibles ---
    numeric_cols = [
        "age",
        "income",
        "purchase_frequency",
        "avg_ticket",
        "recency_days",
        "online_ratio",
        "future_sales",
    ]

    for col in numeric_cols:
        df[col] = df[col].clip(lower=0)

    # --- eliminar valores extremos ---
    df = df[df["age"] <= 100]
    df = df[df["online_ratio"] <= 1]

    print("Filas limpias:", len(df))

    output_path.parent.mkdir(exist_ok=True)
    df.to_csv(output_path, index=False)

    print(f"Datos limpios guardados en: {output_path}")


if __name__ == "__main__":
    project_root = Path(__file__).resolve().parents[1]

    input_file = project_root / "data" / "retail_sales.csv"
    output_file = project_root / "data" / "retail_sales_clean.csv"

    clean_data(input_file, output_file)
