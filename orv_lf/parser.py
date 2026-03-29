import json
from pathlib import Path
from typing import Iterable, Tuple, Optional

from jsonschema import Draft202012Validator, ValidationError


class ORVLFValidator:
    def __init__(self, schema_path: Path):
        with schema_path.open("r", encoding="utf-8") as f:
            schema = json.load(f)
        self._validator = Draft202012Validator(schema)

    def validate_record(self, record: dict) -> Optional[ValidationError]:
        """
        Validate a single ORV-LF record.

        Returns:
            None if valid, or a ValidationError instance if invalid.
        """
        try:
            self._validator.validate(record)
            return None
        except ValidationError as e:
            return e

    def iter_validate_jsonl(
        self, jsonl_path: Path
    ) -> Iterable[Tuple[int, Optional[ValidationError]]]:
        """
        Validate each line of a JSONL file.

        Yields:
            (line_number, error) where error is None if valid.
        """
        with jsonl_path.open("r", encoding="utf-8") as f:
            for idx, line in enumerate(f, start=1):
                line = line.strip()
                if not line:
                    continue  # skip empty lines
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as e:
                    # Wrap JSON errors in a pseudo-ValidationError-like object
                    class JSONLineError(Exception):
                        pass

                    err = JSONLineError(f"Invalid JSON on line {idx}: {e}")
                    yield idx, err
                    continue

                error = self.validate_record(record)
                yield idx, error
