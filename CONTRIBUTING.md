# Contributing to OpenRoadVibes  
Thank you for your interest in contributing!  
OpenRoadVibes is a community‑driven project, and we welcome contributions of all kinds — code, documentation, hardware designs, data, ideas, and feedback.

This document explains how to get involved and how we work together.

---

# 🧭 Ways to Contribute

There are many ways to help move OpenRoadVibes forward:

### **1. Firmware Development**
Improve the ESP32 firmware, add features, optimize performance, or fix bugs.

### **2. Hardware Design**
Help refine wiring diagrams, enclosure designs, PCB layouts, or the bill of materials.

### **3. Data Processing & Server Pipeline**
Work on ingestion, road‑segment snapping, normalization, or database systems.

### **4. Web Visualization**
Improve the map viewer, UI components, tile rendering, or frontend performance.

### **5. Documentation**
Write guides, tutorials, diagrams, or examples to help others get started.

### **6. Testing & Validation**
Collect sample data, test devices, and help validate roughness metrics.

### **7. Community Support**
Answer questions, help newcomers, and participate in discussions.

---

# 📝 Before You Start

### **1. Read the Vision**
Please read `VISION.md` to understand the philosophy and long‑term goals of the project.

### **2. Review the Roadmap**
`ROADMAP.md` outlines the major phases and priorities.

### **3. Check Existing Issues**
Look for open issues before creating new ones.  
If you want to work on something, comment to let others know.

### **4. Ask Questions**
If you're unsure about anything, open a Discussion — we’re friendly!

---

# 🛠️ Development Workflow

### **1. Fork the Repository**
Create your own fork and clone it locally.

### **2. Create a Feature Branch**
Use descriptive names:

 feature/add-gps-parser
 fix/imu-sampling-rate
 docs/update-hardware-guide


### **3. Make Your Changes**
Follow the coding style of the surrounding code.  
Keep commits focused and meaningful.

### **4. Add or Update Documentation**
If your change affects how something works, update the relevant docs.

### **5. Submit a Pull Request**
Include:
- A clear description of the change  
- Why it’s needed  
- Any relevant screenshots, logs, or data  
- Links to related issues  

A maintainer will review your PR and may request changes.

---

# 📦 Project Structure

Here’s a quick overview of the repository layout:

/docs         — Documentation, diagrams, guides
/firmware     — ESP32 firmware
/server       — Backend ingestion + processing pipeline
/web          — Map viewer + frontend
/data-spec    — OpenRoadVibes Log Format (ORV-LF)
/hardware     — Schematics, BOM, enclosure files
/examples     — Sample data + tutorials


---

# 🧪 Testing & Data Quality

OpenRoadVibes relies on high‑quality data.  
When contributing data or firmware changes:

- Ensure GPS timestamps are accurate  
- Avoid stationary logging (it skews roughness metrics)  
- Mount the device securely in your vehicle  
- Document your setup when sharing sample logs  

---

# 🔐 Code of Conduct

We follow the principles of a welcoming, inclusive community.  
Be respectful, constructive, and kind.  
Harassment or discrimination of any kind is not tolerated.

---

# 📄 License

By contributing, you agree that your contributions will be licensed under the **Apache 2.0 License**, the same license that covers the rest of the project.

This ensures:
- Clear contributor rights  
- Patent protection  
- Broad usability for the community  

---

# 🙌 Thank You

Your contributions — big or small — help build a global, open, and accessible understanding of road quality.

We’re excited to have you here.  
Let’s build something meaningful together.
