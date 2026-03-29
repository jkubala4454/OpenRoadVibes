from pathlib import Path

from orv_lf.parser import ORVLFValidator


def test_minimal_record_valid():
    schema = Path("schema.json")
    validator = ORVLFValidator(schema)

    record = {
        "timestamp": "2026-03-29T17:45:10.000Z",
        "latitude": 44.9536,
        "longitude": -93.0899,
        "speed": 10.2,
        "accel_rms": 1.68,
        "jerk": 0.33,
        "vibration_energy": 0.0025,
    }

    error = validator.validate_record(record)
    assert error is None


def test_invalid_latitude():
    schema = Path("schema.json")
    validator = ORVLFValidator(schema)

    record = {
        "timestamp": "2026-03-29T17:45:10.000Z",
        "latitude": 999,
        "longitude": -93.0899,
        "speed": 10.2,
        "accel_rms": 1.68,
        "jerk": 0.33,
        "vibration_energy": 0.0025,
    }

    error = validator.validate_record(record)
    assert error is not None
