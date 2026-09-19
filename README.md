
# Maximum Subarray Intelligence Engine

An algorithmic and business analytics platform that identifies the **maximum-sum contiguous subarray** using multiple algorithms and connects algorithmic results with real-world business performance data.

The project compares Brute Force, Kadane's Algorithm, and Divide and Conquer approaches while providing data validation, business analytics, benchmarking, and an interactive Streamlit dashboard.

---

## Project Overview

Businesses generate time-series data such as revenue, expenses, customer counts, and daily profit. Identifying the most profitable continuous period can support:

- Business performance analysis
- Profitability monitoring
- Revenue trend analysis
- Algorithm performance comparison
- Data quality validation
- Decision-support dashboards

This project applies maximum subarray algorithms to daily business performance data to identify the continuous period with the highest cumulative business performance.

---

## Key Features

- Three maximum subarray algorithms
- Brute Force algorithm
- Kadane's Algorithm
- Divide and Conquer algorithm
- CSV dataset ingestion
- Schema and value validation
- Data cleaning and quality reporting
- Business performance analytics
- Regional and product-category analysis
- Monthly trend analysis
- Algorithm benchmarking
- Automated testing with pytest
- Interactive Streamlit dashboard
- Interactive Plotly visualizations
- CSV export functionality
- Modular `src`-based Python architecture

---

## Algorithms Implemented

| Algorithm | Time Complexity | Space Complexity |
|---|---:|---:|
| Brute Force | O(n²) | O(1) |
| Kadane's Algorithm | O(n) | O(1) |
| Divide and Conquer | O(n log n) | O(log n) |

### Brute Force

Evaluates every possible contiguous subarray and identifies the subarray with the highest sum.

### Kadane's Algorithm

Uses a dynamic programming approach to find the maximum subarray in linear time.

### Divide and Conquer

Divides the array into smaller sections and compares:

1. The best subarray in the left half
2. The best subarray in the right half
3. The best subarray crossing the midpoint

---

## Project Architecture

```text
Business Dataset
       |
       v
Data Ingestion
       |
       v
Schema Validation
       |
       v
Data Cleaning
       |
       v
Business Analytics
       |
       v
Daily Profit Sequence
       |
       +--------------------+
       |                    |
       v                    v
Brute Force          Kadane Algorithm
       |                    |
       +---------+----------+
                 |
                 v
       Divide and Conquer
                 |
                 v
       Algorithm Comparison
                 |
                 v
          Benchmarking
                 |
                 v
       Streamlit Dashboard
```

For detailed architecture, see:

- [Architecture Documentation](docs/architecture.md)
- [Algorithm Complexity](docs/algorithm-complexity.md)
- [Testing Documentation](docs/testing.md)
- [Limitations and Future Improvements](docs/limitations-and-future.md)

---

## Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Plotly |
| Dashboard | Streamlit |
| Testing | Pytest |
| Development Environment | VS Code |
| Version Control | Git and GitHub |
| Documentation | Markdown |

---

## Project Structure

```text
Maximum-Subarray-Intelligence-Engine/
│
├── data/
│   ├── business_performance.csv
│   └── generate_dataset.py
│
├── outputs/
│   ├── analytics_report.csv
│   ├── business_performance_cleaned.csv
│   ├── data_quality_report.csv
│   ├── performance_benchmark.csv
│   └── visualizations/
│
├── src/
│   └── max_subarray/
│       ├── algorithms/
│       │   ├── brute_force.py
│       │   ├── kadane.py
│       │   └── divide_conquer.py
│       │
│       ├── analytics/
│       ├── benchmarking/
│       ├── ingestion/
│       ├── validation/
│       ├── models.py
│       └── comparison.py
│
├── dashboard/
│   └── app.py
│
├── tests/
│   ├── test_all_algorithms.py
│   ├── test_edge_cases.py
│   ├── test_ingestion.py
│   ├── test_validation.py
│   ├── test_benchmark_schema.py
│   └── test_dashboard.py
│
├── docs/
├── screenshots/
├── README.md
├── LICENSE
├── pyproject.toml
└── requirements.txt
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/maximum-subarray-intelligence-engine.git
```

### 2. Move into the Project

```bash
cd maximum-subarray-intelligence-engine
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Environment on Windows

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```powershell
python -m pip install --upgrade pip
python -m pip install -e .
```

If Plotly is not installed:

```powershell
python -m pip install plotly
```

---

## Usage

### Generate the Dataset

```powershell
python data\generate_dataset.py
```

### Run Data Validation

```powershell
python run_validation.py
```

### Run Business Analytics

```powershell
python run_analytics.py
```

### Run Algorithm Benchmarking

```powershell
python run_benchmark.py
```

### Generate Visualizations

```powershell
python visualizations\benchmark_visualization.py
```

### Launch the Streamlit Dashboard

```powershell
python -m streamlit run dashboard\app.py
```

---

## Dashboard

The Streamlit dashboard provides:

- Business performance KPIs
- Date filtering
- Region filtering
- Product-category filtering
- Revenue and profit trends
- Maximum subarray analysis
- Algorithm comparison
- Benchmark visualizations
- Data exploration
- CSV download functionality

### Dashboard Overview

![Dashboard Overview](screenshots/dashboard-overview.png)

### Algorithm Intelligence

![Algorithm Intelligence](screenshots/algorithm-intelligence.png)

### Algorithm Benchmarking

![Benchmarking](screenshots/benchmarking.png)

### Data Explorer

![Data Explorer](screenshots/data-explorer.png)

> Add the screenshots to the `screenshots` folder using the exact filenames shown above.

---

## Testing

The project uses `pytest` for automated testing.

Run all tests:

```powershell
pytest -v
```

Run dashboard syntax validation:

```powershell
python -m py_compile dashboard\app.py
```

The test suite covers:

- Algorithm correctness
- Edge cases
- Empty arrays
- Negative values
- Algorithm result consistency
- Data ingestion
- Data validation
- Benchmark output structure
- Dashboard components

Record your actual test result after running the complete test suite.

---

## Business Interpretation

The engine identifies the continuous period with the highest cumulative value in the selected business metric.

For example, when daily profit is used as the input sequence, the result identifies the contiguous period with the highest cumulative profit.

This can help analysts investigate:

- Periods of sustained profitability
- Business growth phases
- Negative-performance periods
- Regional performance patterns
- Product-category trends

The maximum subarray result is an analytical indicator and should be interpreted together with business context.

---

## Limitations

- The default dataset is synthetic.
- The project does not currently use live business data.
- Results depend on the selected input metric.
- Maximum subarray analysis does not establish causal relationships.
- Benchmark times depend on hardware and system workload.
- Brute Force becomes computationally expensive for large arrays.
- The current model focuses on one-dimensional contiguous sequences.
- The dashboard does not provide predictive business forecasting by default.

---

## Future Improvements

- Add real-world business datasets.
- Support Excel and JSON ingestion.
- Add configurable input metrics.
- Add rolling-window analysis.
- Add anomaly detection.
- Add forecasting models.
- Add automated CI/CD with GitHub Actions.
- Add Docker support.
- Add database integration.
- Add advanced performance profiling.
- Add downloadable PDF reports.
- Add user authentication to the dashboard.
- Add statistical significance analysis for business comparisons.

---

## Learning Outcomes

This project demonstrates practical experience in:

- Data structures and algorithms
- Algorithmic complexity analysis
- Python package development
- Data validation and cleaning
- Business analytics
- Benchmarking
- Automated testing
- Interactive dashboard development
- Software documentation
- GitHub project organization

---

## Author

**S Mohammed Sahil**

M.Sc. Economics and Data Analytics

Interests:

- Data Analytics
- Business Intelligence
- Algorithmic Problem Solving
- Economic Research
- Financial Analytics

---

## License

This project is licensed under the MIT License.