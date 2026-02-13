import pandas as pd
import numpy as np
from pathlib import Path


def generate_dataset(n_customers: int = 5000, seed: int = 42):
    np.random.seed(seed)

    customer_id = np.arange(1, n_customers + 1)

    age = np.random.randint(18, 70, size=n_customers)
    income = np.random.normal(60000, 15000, size=n_customers).clip(20000, 150000)

    purchase_frequency = np.random.poisson(10, size=n_customers)
    avg_ticket = np.random.normal(80, 20, size=n_customers).clip(5, 500)

    recency_days = np.random.randint(1, 365, size=n_customers)

    online_ratio = np.random.uniform(0, 1, size=n_customers)

    future_sales = (
        purchase_frequency * avg_ticket *
        (1 - recency_days / 400) *
        (0.5 + online_ratio)
    )

    future_sales += np.random.normal(0, 100, size=n_customers)
    future_sales = future_sales.clip(0)

    df = pd.DataFrame({
        "customer_id": customer_id,
        "age": age,
        "income": income,
        "purchase_frequency": purchase_frequency,
        "avg_ticket": avg_ticket,
        "recency_days": recency_days,
        "online_ratio": online_ratio,
        "future_sales": future_sales
    })

    project_root = Path(__file__).resolve().parents[1]
    data_path = project_root / "data"
    data_path.mkdir(exist_ok=True)

    output_file = data_path / "retail_sales.csv"
    df.to_csv(output_file, index=False)

    print(f"Dataset generado en: {output_file}")


if __name__ == "__main__":
    generate_dataset()
