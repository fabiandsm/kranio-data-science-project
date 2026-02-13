import joblib
import pandas as pd
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score


def train_model(data_path: Path):
    print("Entrenando modelo...")

    df = pd.read_csv(data_path)

    target = "future_sales"

    features = [
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

    X = df[features]
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42,
        n_jobs=-1
    )

    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    mse = mean_squared_error(y_test, preds)
    rmse = mse ** 0.5

    r2 = r2_score(y_test, preds)

    print(f"RMSE: {rmse:.2f}")
    print(f"R2: {r2:.3f}")

    project_root = Path(__file__).resolve().parents[1]
    
    models_path = project_root / "outputs" / "models"
    models_path.mkdir(parents=True, exist_ok=True)

    model_file = models_path / "retail_model.joblib"
    joblib.dump(model, model_file)

    print(f"Modelo guardado en: {model_file}")

    return model


if __name__ == "__main__":
    project_root = Path(__file__).resolve().parents[1]

    data_file = project_root / "data" / "retail_sales_features.csv"

    train_model(data_file)
