
from pathlib import Path

from max_subarray.ingestion.loaders import (
    load_business_data,
    validate_values,
)


def main() -> None:
    project_root = Path(__file__).resolve().parent
    file_path = project_root / "data" / "business_performance.csv"

    data = load_business_data(file_path)
    validate_values(data)

    print("=" * 50)
    print("MAXIMUM SUBARRAY INTELLIGENCE ENGINE")
    print("=" * 50)

    print(f"Dataset rows: {len(data)}")
    print(f"Dataset columns: {len(data.columns)}")
    print(f"Total revenue: {data['revenue'].sum():,.2f}")
    print(f"Total expenses: {data['expenses'].sum():,.2f}")
    print(f"Total profit: {data['daily_profit'].sum():,.2f}")
    print(f"Average daily profit: {data['daily_profit'].mean():,.2f}")


if __name__ == "__main__":
    main()