# OpenRoadVibes  
*A global, open‑source platform for sensing, analyzing, and mapping road roughness using low‑cost ESP32‑based devices.*

---

## 🚗 Overview

OpenRoadVibes is an open‑source project that empowers anyone to measure and visualize road roughness using inexpensive hardware.  
By combining an ESP32 microcontroller, a GPS module, and an accelerometer, the system collects vibration data while driving and converts it into a “roughness score” that can be displayed on a map.

The long‑term vision is a **crowdsourced global roughness map** that highlights smooth and rough roads using a simple color scale (green → red).  
This helps drivers, cyclists, city planners, and researchers understand real‑world road conditions in a transparent, community‑driven way.

OpenRoadVibes is inspired by concepts from the International Roughness Index (IRI), but is **not** intended to be a certified IRI measurement tool.

---

## 🧩 Project Architecture (High‑Level)

OpenRoadVibes consists of four major components:

### **1. Device Firmware (ESP32)**
- Reads accelerometer data at high frequency  
- Reads GPS position and speed  
- Computes rolling vibration metrics (RMS, jerk, etc.)  
- Logs data to SD card or uploads via WiFi  

### **2. Open Data Format**
A standardized, open log schema for roughness data:

