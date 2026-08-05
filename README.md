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

The framework currently supports the following database adapters:

| Database | Adapter Status |
|---|---|
| Memory Database | Supported |
| ArangoDB | Supported |
| CognODB Cloud | Supported |

The adapter-based architecture allows additional graph database platforms to be integrated without changing the benchmark execution logic.

---

# Dataset

The benchmark uses a graph dataset based on a public graph dataset.

Dataset:
SNAP soc-Pokec social network dataset

Source:
https://snap.stanford.edu/data/soc-pokec.html

Dataset size used:

| Property | Count |
|---|---:|
| Nodes | 50,000 |
| Relationships | 149,998 |

The same dataset format is used across all benchmark adapters to ensure fair comparison.

---


# Data Loading Method

The benchmark loads the same dataset into each supported database using the corresponding database adapter.

| Database | Load Method |
|---|---|
| Memory Database | In-memory Python graph construction |
| CognODB Cloud | Neo4j Bolt driver using batched Cypher inserts |
| ArangoDB | Python ArangoDB driver |

All benchmark executions use the identical dataset format to ensure consistency across supported databases.

---

# Benchmark Environment

The benchmark was executed under a controlled environment.

Environment details:

| Component | Details |
|---|---|
| Language | Python |
| Database | CognODB Cloud |
| Dataset Type | Public graph dataset (SNAP soc-Pokec sample) |
| Nodes | 50,000 |
| Relationships | 149,998 |

All benchmark workloads use the same dataset format and execution methodology to ensure consistent comparison.

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


# Indexed Properties

The following indexed properties are used for lookup workloads.

| Property | Purpose |
|---|---|
| id | Point lookup |
| type | Filtered lookup |

These properties are used consistently during benchmark execution.

---

# Resource Footprint

Resource usage depends on the database platform.

| Resource | Status |
|---|---|
| Instance Type | CognODB Cloud Free Tier |
| CPU | 0.5 vCPU |
| Memory | 256 MB RAM |
| Storage | 1 GB |

Where platform-specific resource metrics are unavailable, they are reported as **Not observable**.

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
Node load time: ...
Node ingestion: ... nodes/sec

Relationships loaded: 149998
Relationship load time: ...
Relationship ingestion: ... relationships/sec

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

---

# Benchmark Results

Current CognODB benchmark results:

| Operation | p50 latency (ms) | p95 latency (ms) |
|---|---:|---:|
| 1-hop traversal | 0.0003 | 0.0004 |
| 2-hop traversal | 0.0007 | 0.0009 |
| 3-hop traversal | 0.0017 | 0.0019 |
| Point lookup | 0.0002 | 0.0002 |
| Filtered lookup | 2.5094 | 4.3411 |
| Aggregation | 3.9499 | 6.1475 |

Benchmark configuration:

| Parameter | Value |
|---|---|
| Warm-up runs | 10 |
| Measurement iterations | 100 |
| Mixed workload clients | 10 |
| Mixed workload operations | 1000 |
| Mixed workload throughput | 542358.17 queries/sec |


---

# Analysis

The benchmark results demonstrate the performance characteristics of different graph workloads under the tested CognODB Cloud environment.

- Traversal query latency increases with hop depth because deeper traversals require exploring additional relationships in the graph.
- Point lookup operations show low latency because they access specific node identifiers directly.
- Filtered lookup operations require evaluating node properties, which results in higher execution time compared to direct lookups.
- Aggregation queries process multiple graph records to calculate grouped results, leading to higher latency.
- Mixed workload testing measures the ability of the system to handle concurrent operations and reports sustained throughput using queries per second (QPS).

The benchmark focuses on reproducible measurement and transparent reporting. The results should be interpreted within the tested environment and configuration rather than as a universal ranking of graph databases.


---

# Caveats

The benchmark results should be interpreted considering the following limitations:

- Cloud database performance can vary depending on network conditions and service availability.
- Free-tier resources may introduce CPU, memory, or throughput limitations.
- Results represent only the tested environment and benchmark configuration.
- Managed database platforms expose different levels of resource monitoring information.
- Database-specific optimizations were minimized to maintain consistent benchmark methodology.
- Additional database adapters can be integrated in future versions for broader comparison.

---