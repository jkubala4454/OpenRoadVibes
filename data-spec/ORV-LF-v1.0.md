# OpenRoadVibes Log Format (ORV‑LF) v1.0

## Status
**Version:** 1.0  
**Stability:** Stable  
**Last Updated:** 2026‑03‑29  
**Maintainers:** OpenRoadVibes Core Team  

---

# 1. Purpose

The OpenRoadVibes Log Format (ORV‑LF) defines a consistent, open standard for recording road‑roughness data collected by low‑cost sensing devices.  
It ensures that data from different contributors, vehicles, sensors, and firmware versions can be processed, aggregated, and visualized in a unified way.

This specification is **required** for all devices and tools that produce or consume OpenRoadVibes data.

---

# 2. Design Principles

- **Simple:** Easy to generate on microcontrollers and easy to parse on servers.  
- **Explicit:** All units, fields, and conventions are unambiguous.  
- **Extensible:** Optional fields allow future growth without breaking compatibility.  
- **Robust:** Designed to handle noisy sensors and real‑world driving conditions.  
- **Open:** Fully documented and free to implement.

---

# 3. File Formats

ORV‑LF v1.0 supports three equivalent formats:

### 3.1 CSV (recommended for firmware)
- Human‑readable  
- Easy to generate on ESP32  
- One row per sample  

### 3.2 JSON
- Structured  
- Suitable for uploads or APIs  

### 3.3 JSONL (JSON Lines)
- One JSON object per line  
- Ideal for streaming or large datasets  

All formats must contain the same required fields.

---

# 4. Required Fields

| Field | Type | Units | Description |
|-------|------|--------|-------------|
| `timestamp` | string | ISO 8601 | UTC timestamp of sample |
| `latitude` | float | decimal degrees | GPS latitude |
| `longitude` | float | decimal degrees | GPS longitude |
| `speed` | float | m/s | Ground speed from GPS |
| `accel_rms` | float | m/s² | Rolling RMS of acceleration magnitude |
| `jerk` | float | m/s³ | Derivative of acceleration magnitude |
| `vibration_energy` | float | (m/s²)² | High‑frequency vibration energy |

---

# 5. Optional Fields

| Field | Type | Description |
|-------|------|-------------|
| `device_id` | string | Unique device identifier |
| `vehicle_type` | string | e.g., car, truck, bike |
| `imu_model` | string | e.g., MPU6050, ICM‑20948 |
| `firmware_version` | string | Semantic version |
| `mounting_orientation` | string | e.g., “upright”, “sideways”, “unknown” |
| `sampling_rate_hz` | float | IMU sampling frequency |
| `notes` | string | Free‑text metadata |

Optional fields must not break parsing if omitted.

---

# 6. Field Definitions

## 6.1 timestamp
- Format: `YYYY‑MM‑DDTHH:MM:SS.sssZ`  
- Must be synchronized with GPS time when available.  
- If GPS time is unavailable, device time may be used but must be flagged.

## 6.2 latitude / longitude
- Decimal degrees  
- Must be valid GPS fixes (see validation rules)

## 6.3 speed
- Raw GPS ground speed  
- Must be ≥ 0  
- Samples with speed < 1 m/s should be ignored in roughness analysis

## 6.4 accel_rms

### Acceleration magnitude:
```text
a_mag = sqrt(a_x^2 + a_y^2 + a_z^2)
```
### Rolling RMS:
```text
accel_rms = sqrt( (1/N) * Σ(a_mag_i^2) )
```

## 6.5 jerk
```text
jerk = d(a_mag) / dt
```
## 6.6 vibration_energy
```text
vibration_energy = Σ( a_mag_HF^2 )
```
Where a_mag_HF is the high‑pass‑filtered acceleration magnitude.

# 7. Sampling Requirements

## 7.1 IMU Sampling Rate
- Minimum: **100 Hz**  
- Recommended: **200 Hz**  
- Sampling rate must remain stable within **±5%**  
- Devices should record the actual sampling rate when possible

## 7.2 GPS Sampling Rate
- Minimum: **1 Hz**  
- Recommended: **5–10 Hz**  
- GPS timestamps should be used to synchronize IMU windows when available

## 7.3 Roughness Window
All roughness metrics must be computed over a **fixed 250 ms window**.

For example:
- At 200 Hz → 50 samples  
- At 100 Hz → 25 samples  

This ensures consistency across devices and contributors.

## 7.4 Synchronization Requirements
- IMU and GPS data must be aligned using timestamps  
- If GPS time is unavailable, device time may be used temporarily but must be flagged  
- Drift correction should occur when GPS time becomes available again

## 7.5 Data Quality Requirements
- Samples with **speed < 1 m/s** must be ignored by downstream processing  
- IMU saturation events should be flagged  
- Missing GPS fixes should not produce roughness samples  

# 8. Validation Rules

A valid ORV‑LF file must satisfy all of the following requirements.

## 8.1 Required Fields
Every record must include all required fields defined in Section 4:
- `timestamp`
- `latitude`
- `longitude`
- `speed`
- `accel_rms`
- `jerk`
- `vibration_energy`

Missing required fields invalidate the record.

## 8.2 GPS Validity
GPS coordinates must meet the following constraints:
- Latitude must be between **–90 and 90**
- Longitude must be between **–180 and 180**
- If available, HDOP should be **< 5**  
  (Higher values indicate poor GPS quality)

Records with invalid GPS data must be discarded.

## 8.3 Speed Threshold
Samples with **speed < 1 m/s** must not be used for roughness analysis.  
These samples may be logged but must be ignored by downstream processing.

## 8.4 Timestamp Monotonicity
Timestamps must be **non‑decreasing** throughout the file.

If the device temporarily loses time synchronization:
- The record must include a flag (e.g., `gps_lost = true`)
- Processing tools must treat the affected window with reduced confidence

## 8.5 Sampling Consistency
The IMU sampling rate must remain stable within **±5%** of the declared rate.

If the sampling rate drifts outside this range:
- The affected window must be flagged
- Roughness metrics should not be computed for that window

## 8.6 Window Integrity
Roughness metrics (`accel_rms`, `jerk`, `vibration_energy`) must be computed over:
- A **250 ms window**
- Using **complete** IMU samples for that window

Windows with missing IMU samples must be discarded.

## 8.7 Data Type Validation
Each field must match its expected type:
- Floats must be valid numeric values
- Strings must be UTF‑8
- Timestamps must be valid ISO 8601

Invalid types invalidate the record.

## 8.8 No NaN or Infinity
Fields must not contain:
- `NaN`
- `Infinity`
- `-Infinity`

Any such values invalidate the record.

## 8.9 Optional Field Behavior
Optional fields may be omitted entirely.  
If present, they must follow their defined type and format.

# 9. Examples

This section provides reference examples of valid ORV‑LF files in CSV, JSON, and JSONL formats.  
All examples use the required fields defined in Section 4 and follow the validation rules in Section 8.

---

## 9.1 CSV Example

```text
timestamp,latitude,longitude,speed,accel_rms,jerk,vibration_energy,device_id
2026-03-29T17:45:12.123Z,44.9537,-93.0900,12.4,1.82,0.45,0.0032,ORV-001
2026-03-29T17:45:12.373Z,44.9538,-93.0901,12.5,1.79,0.41,0.0030,ORV-001
```
**Notes**
- CSV is the recommended format for firmware devices.
- All required fields appear in each row.
- Optional fields (e.g., `device_id`) may be included.
## 9.2 JSON Example

```json
{
  "timestamp": "2026-03-29T17:45:12.123Z",
  "latitude": 44.9537,
  "longitude": -93.0900,
  "speed": 12.4,
  "accel_rms": 1.82,
  "jerk": 0.45,
  "vibration_energy": 0.0032,
  "device_id": "ORV-001"
}
```
**Notes**
- JSON is ideal for uploads, APIs, and structured storage.
- Field names must match exactly.
- Numeric fields must be valid JSON numbers (no NaN or Infinity).
## 9.3 JSONL Example

```text
{"timestamp":"2026-03-29T17:45:12.123Z","latitude":44.9537,"longitude":-93.0900,"speed":12.4,"accel_rms":1.82,"jerk":0.45,"vibration_energy":0.0032}
{"timestamp":"2026-03-29T17:45:12.373Z","latitude":44.9538,"longitude":-93.0901,"speed":12.5,"accel_rms":1.79,"jerk":0.41,"vibration_energy":0.0030}
```
**Notes**
- JSONL (JSON Lines) is recommended for large datasets or streaming.
- Each line must contain exactly one JSON object.
- No trailing commas or extra whitespace.

## 9.4 Example of a Record With Optional Fields

```json
{
  "timestamp": "2026-03-29T17:45:14.002Z",
  "latitude": 44.9540,
  "longitude": -93.0903,
  "speed": 11.9,
  "accel_rms": 1.75,
  "jerk": 0.39,
  "vibration_energy": 0.0028,
  "device_id": "ORV-002",
  "vehicle_type": "bike",
  "imu_model": "ICM-20948",
  "firmware_version": "1.2.0",
  "sampling_rate_hz": 200
}
```
**Notes**
- Optional fields may appear in any order.
- Optional fields must follow their defined types.
- Omitted optional fields must not break parsing.

## 9.5 Invalid Example (For Validator Testing)

```text
timestamp,latitude,longitude,speed,accel_rms,jerk,vibration_energy
2026-03-29T17:45:12.123Z,999,-93.0900,12.4,1.82,0.45,0.0032
```
**Notes**
- Latitude `999` is outside the valid range (–90 to 90).
- This record must be rejected by any ORV‑LF validator.
- Invalid examples are useful for testing parsers and automated QA tools.

## 9.6 Multi‑Record Dataset Example

```text
{"timestamp":"2026-03-29T17:45:12.123Z","latitude":44.9537,"longitude":-93.0900,"speed":12.4,"accel_rms":1.82,"jerk":0.45,"vibration_energy":0.0032,"device_id":"ORV-001"}
{"timestamp":"2026-03-29T17:45:12.373Z","latitude":44.9538,"longitude":-93.0901,"speed":12.5,"accel_rms":1.79,"jerk":0.41,"vibration_energy":0.0030,"device_id":"ORV-001"}
{"timestamp":"2026-03-29T17:45:12.623Z","latitude":44.9539,"longitude":-93.0902,"speed":12.6,"accel_rms":1.77,"jerk":0.38,"vibration_energy":0.0029,"device_id":"ORV-001"}
{"timestamp":"2026-03-29T17:45:12.873Z","latitude":44.9540,"longitude":-93.0903,"speed":12.7,"accel_rms":1.74,"jerk":0.36,"vibration_energy":0.0027,"device_id":"ORV-001"}
```
**Notes**
- This example shows a realistic sequence of consecutive samples.
- All required fields are present in each record.
- Timestamps are monotonic and evenly spaced.
- Values fall within valid ranges and follow the sampling and validation rules.
- This format is ideal for testing ingestion pipelines and batch validators.

## 9.7 Minimal Valid Record Example

```json
{
  "timestamp": "2026-03-29T17:45:10.000Z",
  "latitude": 44.9536,
  "longitude": -93.0899,
  "speed": 10.2,
  "accel_rms": 1.68,
  "jerk": 0.33,
  "vibration_energy": 0.0025
}
```
**Notes**
- This is the smallest valid ORV‑LF record containing only required fields.
- All values fall within valid ranges.
- No optional fields are included.
- Useful for testing strict schema validation and minimal ingestion paths.

## 9.8 Fully Populated Record Example

```json
{
  "timestamp": "2026-03-29T17:45:20.500Z",
  "latitude": 44.9542,
  "longitude": -93.0905,
  "speed": 13.1,
  "accel_rms": 1.88,
  "jerk": 0.47,
  "vibration_energy": 0.0034,
  "device_id": "ORV-003",
  "vehicle_type": "scooter",
  "imu_model": "ICM-42688-P",
  "firmware_version": "2.0.1",
  "sampling_rate_hz": 200,
  "hdop": 0.9,
  "gps_lost": false,
  "notes": "Full optional-field example for validator testing",
  "session_id": "SESSION-20260329-01",
  "operator_id": "OP-17",
  "battery_voltage": 11.7,
  "temperature_c": 22.4
}
```
**Notes**
- This example includes every optional field defined in the specification.
- Useful for testing maximum‑schema ingestion, UI rendering, and database migrations.
- All values fall within valid ranges and follow the validation rules.
- Optional fields may appear in any order.

## 10. Versioning

The ORV‑LF specification uses **semantic versioning** to track changes to the data format, validation rules, and optional‑field definitions.

### 10.1 Version Format

Versions follow the pattern:
MAJOR.MINOR.PATCH

- **MAJOR** — Introduces breaking changes that may invalidate older data or require parser updates.
- **MINOR** — Adds new optional fields, clarifies rules, or expands examples without breaking compatibility.
- **PATCH** — Fixes typos, clarifies wording, or updates non‑normative examples.

### 10.2 Backward Compatibility

- All **MINOR** and **PATCH** updates must remain backward‑compatible with existing valid ORV‑LF data.
- **MAJOR** updates may introduce breaking changes but must include a migration guide.

### 10.3 Deprecation Policy

- Optional fields may be marked as **deprecated** in a MINOR release.
- Deprecated fields remain valid for at least one full MAJOR cycle.
- Removal of deprecated fields occurs only in a MAJOR release.

### 10.4 Version Identification

- The specification version is declared in the document header.
- Devices and software **may** include a `spec_version` field in metadata blocks, but this is not required for individual records.

### 10.5 Example

  2.1.0

- **2** — Second major revision of the ORV‑LF specification  
- **1** — Adds new optional fields (e.g., `session_id`, `operator_id`)  
- **0** — No breaking changes; only clarifications and example updates

  
