
from pathlib import Path

import numpy as np
import pandas as pd


def generate_business_data(
    start_date: str = "2025-01-01",
    days: int = 365,
    seed: int = 42,
) -> pd.DataFrame:
    """Generate synthetic daily business performance data."""

    rng = np.random.default_rng(seed)

    dates = pd.date_range(
        start=start_date,
        periods=days,
        freq="D",
    )

    regions = ["North", "South", "East", "West"]
    categories = ["Electronics", "Clothing", "Home", "Grocery"]

    revenue = rng.normal(
        loc=50000,
        scale=12000,
        size=days,
    )

    revenue = np.maximum(revenue, 5000).round(2)

    expenses = (
        revenue * rng.uniform(0.65, 0.95, size=days)
        + rng.normal(0, 1500, size=days)
    )

    expenses = np.maximum(expenses, 1000).round(2)

    customers = rng.integers(
        low=100,
        high=1000,
        size=days,
    )

    daily_profit = np.round(
        revenue - expenses,
        2,
    )

    data = pd.DataFrame(
        {
            "date": dates,
            "revenue": revenue,
            "expenses": expenses,
            "daily_profit": daily_profit,
            "customers": customers,
            "region": rng.choice(regions, size=days),
            "product_category": rng.choice(
                categories,
                size=days,
            ),
        }
    )

    return data


def main() -> None:
    project_root = Path(__file__).resolve().parent.parent
    output_path = project_root / "data" / "business_performance.csv"

    data = generate_business_data()

    data.to_csv(output_path, index=False)

    print(f"Dataset created: {output_path}")
    print(f"Rows: {len(data)}")
    print(f"Columns: {len(data.columns)}")
    print("\nFirst 5 rows:")
    print(data.head())


if __name__ == "__main__":
    main()