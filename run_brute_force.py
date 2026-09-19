
from pathlib import Path

from max_subarray.algorithms.brute_force import (
    brute_force_max_subarray,
)
from max_subarray.ingestion.loaders import (
    load_business_data,
    validate_values,
)


def main() -> None:
    project_root = Path(__file__).resolve().parent

    file_path = (
        project_root
        / "data"
        / "business_performance.csv"
    )

    data = load_business_data(file_path)
    validate_values(data)

    profits = data["daily_profit"].tolist()

    result = brute_force_max_subarray(profits)

    best_period = data.iloc[
        result.start_index : result.end_index + 1
    ]

    print("=" * 60)
    print("BRUTE FORCE MAXIMUM SUBARRAY ANALYSIS")
    print("=" * 60)

    print(f"Start Index: {result.start_index}")
    print(f"End Index: {result.end_index}")
    print(f"Maximum Cumulative Profit: {result.max_sum:,.2f}")
    print(f"Algorithm: {result.algorithm}")
    print(f"Time Complexity: {result.time_complexity}")
    print(f"Space Complexity: {result.space_complexity}")

    print("\nBest Profit Period:")
    print(f"Start Date: {best_period['date'].min().date()}")
    print(f"End Date: {best_period['date'].max().date()}")
    print(f"Number of Days: {len(best_period)}")


if __name__ == "__main__":
    main()







    
from pathlib import Path

from max_subarray.analytics.business_analytics import (
    analyze_max_profit_period,
    save_analysis_report,
)
from max_subarray.ingestion.loaders import (
    load_business_data,
    validate_values,
)


def main() -> None:
    project_root = Path(__file__).resolve().parent

    data_path = (
        project_root
        / "data"
        / "business_performance.csv"
    )

    output_path = (
        project_root
        / "outputs"
        / "brute_force_report.csv"
    )

    data = load_business_data(data_path)
    validate_values(data)

    report = analyze_max_profit_period(data)

    save_analysis_report(report, output_path)

    print(report.to_string(index=False))
    print(f"\nReport saved to: {output_path}")


if __name__ == "__main__":
    main()