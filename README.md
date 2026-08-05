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
+----------------+
| |
Memory CognODB
Database Cloud

|
v

Metrics Collection

|
v

Reports
(JSON / CSV / Charts)

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

# Project Structure
# Project Structure

```
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

Credentials are loaded using environment variables and are not stored in the repository.

# Installation

Clone the repository:

```bash
git clone https://github.com/usurumarthiroxy123-cpu/cognodb-cloud-benchmark.git

Install dependencies:

pip install -r requirements.txt


# Running Benchmark

Run benchmark execution:

python -m scripts.run_benchmark

Example output:

========== CognODB Cloud Benchmark ==========

Active database: cognodb

Loading dataset...

Nodes loaded: 50000
Relationships loaded: 149998

Running benchmarks...

Results saved to results/benchmark_results.json

# Generate Reports

Generate CSV report and benchmark chart:

python -m scripts.generate_report

Generated files:

results/

├── benchmark_results.json
├── benchmark_results.csv
└── benchmark_chart.png

# Benchmark Results

Current CognODB benchmark results:

Operation	p50 latency (ms)	p95 latency (ms)
1-hop traversal	0.0002	0.0003
2-hop traversal	0.0003	0.0005
3-hop traversal	0.0005	0.0006
Point lookup	0.0001	0.0002
Filtered lookup	3.3062	5.2547
Aggregation	5.0969	8.5522

# Methodology

The benchmark follows:

Same dataset format
Automated execution
Multiple iterations
p50 and p95 latency measurements
Environment-based credentials
Automated report generation

# Analysis

Performance depends on:

Database architecture
Query optimization
Indexing strategy
Network latency
Cloud resource limitations

The benchmark provides transparent measurements rather than declaring a single database as the winner.

# Caveats
Cloud performance may vary due to network conditions.
Free-tier limitations may affect results.
Results represent the tested environment.
Additional database adapters can be added using the existing architecture.

# Future Improvements
Add more graph database platforms
Add automated deployment
Add resource monitoring
Add larger datasets
Add advanced concurrency testing