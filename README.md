# CognODB Cloud Benchmark Framework

A Python-based graph database benchmarking framework designed to evaluate cloud graph database performance using reproducible workloads.

The framework provides a modular adapter-based architecture that allows different database implementations to be tested using a common benchmarking engine.

---

# Objective

The objective of this project is to benchmark graph database performance by measuring common graph workloads such as:

- Graph traversal queries
- Point lookups
- Filtered lookups
- Aggregation queries
- Mixed workload performance

The benchmark focuses on:

- Reproducible execution
- Automated measurement
- Percentile-based latency reporting
- Extensible database adapter design

---

# Architecture

```text
Dataset
   |
   v
Graph Loader
   |
   v
Benchmark Runner
   |
   v
Database Adapter Layer
   |
   +-----------------------+
   |                       |
   v                       v
Memory Database     CognODB Cloud Database
                            |
                            v
                   Metrics Collection
                            |
                            v
              Reports (JSON / CSV / Charts)
```

---
# Features

## Graph Workloads

The framework supports:

### Traversal Queries

- 1-hop traversal
- 2-hop traversal
- 3-hop traversal

Measured metrics:

- p50 latency
- p95 latency

---

### Lookup Queries

Supported operations:

- Point lookup
- Filtered lookup

Measured metrics:

- p50 latency
- p95 latency

---

### Aggregation Queries

Supports count/group style graph operations.

Measured metrics:

- p50 latency
- p95 latency

---

### Mixed Workload

Measures:

- Concurrent operations
- Queries per second (QPS)

---

# Supported Databases

| Database | Status |
|---|---|
| Memory Database | Supported |
| ArangoDB | Supported |
| CognODB Cloud | Supported |

The adapter architecture allows additional graph databases to be integrated without changing benchmark logic.

---

# Dataset

The benchmark uses a graph dataset containing:

| Property | Count |
|---|---:|
| Nodes | 50,000 |
| Relationships | 149,998 |

The dataset is loaded through automated graph loaders.

All benchmark operations use the same dataset format to maintain consistency.

---

# Benchmark Environment

The benchmark was executed under a controlled environment.

Environment details:

| Component | Details |
|---|---|
| Language | Python |
| Database | CognODB Cloud |
| Dataset Type | Synthetic graph dataset |
| Nodes | 50,000 |
| Relationships | 149,998 |

All databases are tested using the same dataset format and benchmark workloads to ensure consistent comparison.

---

# Benchmark Execution Methodology

The benchmark follows:

- Dataset loading before execution
- Warm-up execution before measurements
- Multiple benchmark iterations
- p50 and p95 latency calculation
- Automated result collection
- JSON, CSV, and chart report generation

---

# Resource Monitoring

Resource usage depends on the database platform and cloud environment.

The current benchmark focuses on query performance metrics:
- Latency
- Throughput
- Query execution time

Database-specific resource metrics can be added in future versions.

---

# Project Structure

```text
cognodb-cloud-benchmark/

├── adapters/
│   ├── adapter_factory.py
│   ├── cognodb_adapter.py
│   └── arangodb_adapter.py
│
├── benchmarks/
│   └── benchmark_runner.py
│
├── loaders/
│   └── graph_loader.py
│
├── metrics/
│   └── load_metrics.py
│
├── scripts/
│   ├── run_benchmark.py
│   └── generate_report.py
│
├── config/
│   └── config.yaml
│
├── results/
│   ├── benchmark_results.json
│   ├── benchmark_results.csv
│   └── benchmark_chart.png
│
└── requirements.txt
```

---

# Environment Configuration

Create a `.env` file in the project root:

```env
COGNODB_URI=your_connection_uri
COGNODB_USERNAME=cognodb
COGNODB_PASSWORD=your_password_here
```

Credentials are loaded using environment variables and are not stored in the repository.

---

# Installation

Clone the repository:

```bash
git clone https://github.com/usurumarthiroxy123-cpu/cognodb-cloud-benchmark.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Running Benchmark

Run benchmark execution:

```bash
python -m scripts.run_benchmark
```

Example output:

```text
========== CognODB Cloud Benchmark ==========

Active database: cognodb

Loading dataset...

Nodes loaded: 50000
Relationships loaded: 149998

Running benchmarks...

Results saved to results/benchmark_results.json
```

---

# Generate Reports

Generate CSV report and benchmark chart:

```bash
python -m scripts.generate_report
```

Generated files:

```text
results/

├── benchmark_results.json
├── benchmark_results.csv
└── benchmark_chart.png
```