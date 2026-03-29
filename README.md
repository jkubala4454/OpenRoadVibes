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
timestamp, latitude, longitude, accel_rms, jerk, vibration_energy, speed


### **3. Server + Processing Pipeline**
- Accepts uploaded logs  
- Snaps GPS points to OpenStreetMap road segments  
- Normalizes roughness values  
- Aggregates scores per road segment  
- Stores results in a database (PostGIS recommended)  

### **4. Map Visualization**
- Generates color‑coded tiles (green → red)  
- Displays roughness overlay on top of OSM  
- Web viewer built with Leaflet or MapLibre  

---

## 🎯 Project Goals

- Build a **low‑cost, open hardware** device for road roughness logging  
- Create a **standardized, open data format** for roughness measurements  
- Develop a **server pipeline** for processing and aggregating crowdsourced data  
- Provide a **public map** showing roughness levels on roads worldwide  
- Encourage community contributions, experimentation, and transparency  

---

## 🛑 What This Project Is *Not*

- Not a certified IRI measurement system  
- Not a replacement for DOT‑grade inertial profilers  
- Not a tool for modifying OpenStreetMap data directly  
- Not a commercial product  

This project focuses on **relative roughness**, not official pavement quality metrics.

---

## 🗺️ Roadmap

### **Phase 1 — Hardware + Firmware**
- ESP32 prototype  
- IMU + GPS data logging  
- Roughness metric computation  
- SD card logging  

### **Phase 2 — Data Format + Tools**
- Define open log schema  
- Create uploader tool  
- Build sample datasets  

### **Phase 3 — Server Pipeline**
- API for data ingestion  
- Road‑segment snapping  
- Roughness aggregation  
- Database schema  

### **Phase 4 — Visualization**
- Tile generation  
- Web map viewer  
- Color‑coded roughness overlay  

### **Phase 5 — Crowdsourcing**
- Contributor onboarding  
- Calibration strategies  
- Community governance  

---

## 🤝 Contributing

Contributions are welcome!  
This project is in early development, and we’re actively shaping:

- Firmware design  
- Data standards  
- Server architecture  
- Visualization tools  

If you’d like to help, please open an issue or start a discussion.

---

## 📄 License

This project is licensed under the **Apache 2.0 License**, which provides:

- Explicit patent protection  
- Clear contributor rights  
- Broad commercial and academic usability  

See the `LICENSE` file for details.

---

## 📬 Contact / Discussion

Questions, ideas, or feedback?  
Open an issue or start a discussion in the GitHub Discussions tab.

---

## ⭐ Acknowledgments

This project builds on concepts from:
- OpenStreetMap  
- Low‑cost IMU research  
- Smartphone‑based roughness studies  
- Community‑driven mapping initiatives  

And on the enthusiasm of contributors who believe in open, accessible sensing.


A standardized, open log schema for roughness data:

