# CognODB Cloud Benchmark Framework

A Python-based benchmarking framework designed to evaluate database operation performance by measuring execution time for common workloads such as insert, read, query, and update operations.

The framework provides a modular architecture that allows different database implementations to be tested using a common benchmarking engine.

---

## Problem Statement

Database performance plays an important role in cloud applications. Developers need a reliable way to measure how efficiently a database handles different workloads.

This project provides a benchmark tool that:

- Loads datasets
- Executes database operations
- Measures execution time
- Generates performance reports
- Supports configurable benchmark workloads

The framework can be extended to benchmark different database systems by replacing the database adapter.

---

# Features

## Benchmark Operations

The framework currently supports:

- Insert performance testing
- Read performance testing
- Query performance testing
- Update performance testing


## Configuration Based Execution

Benchmark settings are managed through YAML configuration.

Example:

```yaml
benchmark:
  dataset: dataset/sample_data.json

  operations:
    - insert
    - read
    - query
    - update