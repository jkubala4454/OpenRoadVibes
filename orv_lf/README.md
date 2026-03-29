# ORV‑LF Reference Parser (Python)

The `orv_lf` package provides the official Python reference parser and validator for the **OpenRoadVibes Logging Format (ORV‑LF)**.  
It ensures that ORV‑LF records and datasets conform to the project’s JSON Schema and validation rules.

This package is lightweight, dependency‑minimal, and designed to serve as the canonical implementation for anyone building ORV‑LF tooling in Python.

## Features

- Validates individual ORV‑LF records or entire JSONL datasets
- Uses the official `schema.json` from the project root
- Provides a simple CLI: `orv-validate`
- Produces clear, human‑readable error messages
- Fully type‑annotated and easy to extend

## Installation

From the repository root:

```bash
pip install .
```
This installs the orv_lf package and the orv-validate command.

## Command‑Line Usage
Validate a single JSON record:
```bash
orv-validate examples/full_record.json
```
## Validate a JSONL dataset:
```bash
orv-validate examples/typical.jsonl --jsonl
```
## Python Usage
```python
from pathlib import Path
from orv_lf import ORVLFValidator

validator = ORVLFValidator(Path("schema.json"))
error = validator.validate_record(record)

if error is None:
    print("Record is valid")
else:
    print("Record is invalid:", error)
```
## Project Structure
orv_lf/
├── __init__.py
├── parser.py   # Core validation logic
└── cli.py      # Implementation of the orv-validate CLI

## Contributing
Please see the project‑wide CONTRIBUTING.md for guidelines and development workflow.
