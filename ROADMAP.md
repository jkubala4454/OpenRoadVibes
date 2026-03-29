# OpenRoadVibes Roadmap  
*A living plan for the evolution of the OpenRoadVibes ecosystem.*

This roadmap outlines the major phases, milestones, and long‑term vision for OpenRoadVibes.  
It is intentionally high‑level and will evolve as the community grows.

---

# 🛣️ Phase 1 — Core Hardware + Firmware (MVP)
**Goal:** Build a reliable, low‑cost device that logs road roughness data.

### Milestones
- Select reference hardware (ESP32, GPS, IMU, SD card)
- Implement high‑frequency accelerometer sampling (100–200 Hz)
- Implement GPS reading (1–10 Hz)
- Compute basic roughness metrics:
  - RMS acceleration  
  - Jerk  
  - High‑frequency vibration energy  
- Log data to SD card in the OpenRoadVibes format
- Provide example datasets for testing
- Publish wiring diagrams + firmware documentation

### Deliverables
- `/firmware` reference implementation  
- Hardware BOM + assembly guide  
- Sample log files  

---

# 🧩 Phase 2 — Open Data Format + Tools
**Goal:** Establish a consistent, open standard for roughness data.

### Milestones
- Finalize the OpenRoadVibes Log Format (ORV‑LF)
- Define required + optional fields
- Create a Python CLI tool for:
  - Validating logs  
  - Converting formats  
  - Previewing roughness metrics  
- Publish example datasets and documentation

### Deliverables
- `/data-spec` folder  
- ORV‑LF v1.0 specification  
- CLI validation tool  

---

# 🌐 Phase 3 — Server + Processing Pipeline
**Goal:** Build the backend that transforms raw logs into usable map data.

### Milestones
- Create ingestion API for uploading logs
- Implement GPS → road‑segment snapping (OSM-based)
- Normalize roughness values across devices
- Aggregate roughness per road segment
- Store results in a spatial database (PostGIS recommended)
- Implement device metadata + calibration strategies

### Deliverables
- `/server` backend service  
- Database schema  
- Processing pipeline documentation  

---

# 🗺️ Phase 4 — Map Visualization
**Goal:** Provide a clean, intuitive map showing roughness levels.

### Milestones
- Generate color‑coded tiles (green → red)
- Build a web viewer using Leaflet or MapLibre
- Add filtering options:
  - Date range  
  - Device type  
  - Speed thresholds  
- Add segment‑level detail popups (roughness score, samples, contributors)

### Deliverables
- `/web` map viewer  
- Tile generation pipeline  
- Public demo map  

---

# 🌍 Phase 5 — Crowdsourcing + Community
**Goal:** Enable global participation and ensure data quality.

### Milestones
- Contributor onboarding documentation
- Calibration guidelines for different vehicles
- Device registration + metadata system
- Community governance model
- Public API for accessing aggregated roughness data
- Outreach to makers, cyclists, researchers, and city planners

### Deliverables
- CONTRIBUTING.md  
- Community guidelines  
- Public API documentation  

---

# 🔬 Phase 6 — Advanced Analytics (Future)
**Goal:** Explore deeper insights and more sophisticated roughness metrics.

### Potential Directions
- Quarter‑car simulation for pseudo‑IRI estimation
- Machine‑learning‑based roughness classification
- Pothole detection and event‑based alerts
- Speed‑normalized roughness scoring
- Multi‑sensor fusion (gyroscope, magnetometer)
- Integration with cycling apps or navigation tools

---

# 🧭 Long‑Term Vision
OpenRoadVibes aims to become the **world’s first open, community‑driven road roughness map**, built on:

- Affordable hardware  
- Transparent algorithms  
- Open data  
- Global collaboration  

The project will evolve based on community needs, scientific research, and real‑world use cases.

---

# 📬 Contributing to the Roadmap
This roadmap is a living document.  
If you have ideas, suggestions, or want to champion a feature:

- Open an issue  
- Start a GitHub Discussion  
- Submit a pull request  

Together, we can build a global, open, and accessible understanding of road quality.

