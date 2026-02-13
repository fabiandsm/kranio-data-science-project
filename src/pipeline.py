import argparse
from pathlib import Path

from generate_data import generate_dataset
from clean import clean_data
from features import build_features
from train import train_model
from predict import predict


def run_all(project_root):
    print("=== PIPELINE RETAIL ML ===")

    data_path = project_root / "data"

    raw_file = data_path / "retail_sales.csv"
    clean_file = data_path / "retail_sales_clean.csv"
    features_file = data_path / "retail_sales_features.csv"
    predictions_file = data_path / "retail_sales_predictions.csv"

    print("\n[1/5] Generando datos...")
    generate_dataset()

    print("\n[2/5] Limpieza...")
    clean_data(raw_file, clean_file)

    print("\n[3/5] Creando features...")
    build_features(clean_file, features_file)

    print("\n[4/5] Entrenando modelo...")
    train_model(features_file)

    print("\n[5/5] Generando predicciones...")
    predict(features_file, predictions_file)

    print("\n✅ Pipeline completo ejecutado.")


def main():
    parser = argparse.ArgumentParser(description="Retail ML Pipeline")

    parser.add_argument(
        "step",
        choices=["generate", "clean", "features", "train", "predict", "run-all"],
        help="Paso del pipeline a ejecutar",
    )

    parser.add_argument("--input", help="Archivo de entrada para predict")

    args = parser.parse_args()

    project_root = Path(__file__).resolve().parents[1]
    data_path = project_root / "data"

    raw_file = data_path / "retail_sales.csv"
    clean_file = data_path / "retail_sales_clean.csv"
    features_file = data_path / "retail_sales_features.csv"

    if args.step == "generate":
        generate_dataset()

    elif args.step == "clean":
        clean_data(raw_file, clean_file)

    elif args.step == "features":
        build_features(clean_file, features_file)

    elif args.step == "train":
        train_model(features_file)

    elif args.step == "predict":
        if not args.input:
            raise ValueError("Debes pasar --input archivo.csv")

        input_file = Path(args.input)

        output_file = (
            project_root
            / "outputs"
            / "predictions"
            / f"{input_file.stem}_predictions.csv"
        )

        predict(input_file, output_file)

    elif args.step == "run-all":
        run_all(project_root)


if __name__ == "__main__":
    main()
