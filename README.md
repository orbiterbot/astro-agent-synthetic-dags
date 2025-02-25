# Astro Agent Synthetic DAGs

This repository contains synthetic DAG sets for performance testing the Astro Agent.

## Available DAG Sets

### Default DAGs

Simple DAGs with configurable parse delays between 0-0.1 seconds.

- `dag_sets/default/100`: 100 simple DAGs
- `dag_sets/default/1000`: 1000 simple DAGs

## Usage

These DAGs are intended to be used with the Astro Agent performance testing tools.

```bash
# Generate all DAG sets
make perf gendags

# Run performance tests with a specific DAG set
make perf measure --subfolder=default/100
```
