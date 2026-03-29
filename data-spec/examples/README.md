# ORV‑LF Example Datasets

This directory contains sample logs used for testing, validation, and demonstration of the OpenRoadVibes Logging Format (ORV‑LF). Each file highlights a different aspect of the specification and is intended to support developers building parsers, validators, ingestion pipelines, and visualization tools.

## File Overview

### `minimal.jsonl`
A compact dataset containing only the **required fields** defined in the ORV‑LF schema.

Use cases:
- Testing strict schema validation
- Ensuring ingestion works with minimal payloads
- Teaching new contributors the core record structure

### `typical.jsonl`
A realistic multi‑record dataset representing what a real device might produce in the field. Includes a mix of required and optional fields.

Use cases:
- Parser development
- Performance testing
- Demonstrating typical ORV‑LF usage

### `full_record.json`
A single record containing **every optional field** defined in the specification.

Use cases:
- Maximum‑schema validation
- UI/UX testing for full metadata display
- Database schema verification

### `invalid.jsonl`
A deliberately malformed dataset that violates ORV‑LF rules (e.g., invalid latitude).

Use cases:
- Negative‑case testing
- Validator development
- CI pipelines that enforce schema correctness

## Notes

- All JSONL files contain **one JSON object per line**.
- No trailing commas or extra whitespace are used.
- These examples are non‑normative but fully aligned with the ORV‑LF specification and `schema.json`.

## Suggested Extensions

Projects may optionally add:
- `stress_test.jsonl` — thousands of synthetic records for load testing
- `mixed_quality.jsonl` — interleaved valid and invalid lines
- `device_specific/` — examples grouped by hardware model or firmware version

These are not required but can be helpful for advanced testing.

