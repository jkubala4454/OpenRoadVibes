# OpenRoadVibes — Firmware

This folder contains the ESP32 firmware responsible for collecting road roughness data.

## Responsibilities
- Reading accelerometer data (IMU)  
- Reading GPS position and speed  
- Computing roughness metrics (RMS, jerk, vibration energy)  
- Logging data to SD card or uploading via WiFi  
- Managing device configuration  

## Structure
Typical contents include:
- Source code (`src/`)  
- PlatformIO or Arduino project files  
- IMU and GPS drivers  
- Configuration files  
- Unit tests (optional)  

## Goals
Provide a reliable, low‑cost reference implementation that anyone can build and extend.
