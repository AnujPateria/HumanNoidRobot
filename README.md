# 🤖 Kritrim – AI-Driven Modular Snap-and-Fit Humanoid Robot  

**Team Ourobonics**  
**Track:** Smart India Hackathon 2025 Winner  
**Theme:** AICTE Robotics & Drones Hardware Edition (Open Innovation)   
**Focus:** MSME Empowerment & High-Risk Work Environments  

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue">
  <img src="https://img.shields.io/badge/Gemini%20API-AI%20Brain-purple">
  <img src="https://img.shields.io/badge/Raspberry%20Pi-Embedded%20Control-red">
  <img src="https://img.shields.io/badge/Status-Prototype-success">
</p>


---
<img width="1600" height="719" alt="WhatsApp Image 2025-12-12 at 22 47 57_a05be688" src="https://github.com/user-attachments/assets/9ac542c2-4e57-4c0f-9bf6-a49768d5dfef" />


<!-- <p align="center">
  <img src="https://github.com/user-attachments/assets/60083a79-85d7-4273-b9dd-b457cb99fc75" width="300" alt="Kritrim System Architecture">
</p> -->


---


## 🧠 Project Overview

**Kritrim** is an AI-driven, modular humanoid robot designed with a **snap-and-fit architecture** that allows **tool-free replacement of robot parts by non-technical users**.

The system targets:

- MSMEs suffering from staff shortages and high maintenance costs  
- High-risk environments such as radiology rooms, chemical plants, and industrial zones where human exposure is dangerous  

Unlike existing humanoid robots that are expensive, monolithic, and hard to repair, **Kritrim is**:

- 70–80% cheaper  
- Fully modular  
- Repairable without engineers  
- Scalable across industries  

---

## ❓ Problem Statement

Current humanoid robots face major limitations:

- Very high cost (₹20–60 lakh)  
- Non-modular hardware  
- Long downtime if a single part fails  
- Dependence on skilled technicians  
- Unsafe for hazardous environments  

These limitations make humanoid robots impractical for Indian MSMEs and public-facing or high-risk workplaces.

---

## 💡 Our Solution

Kritrim introduces a **snap-and-fit modular humanoid architecture** where:

- Each body part (arm, head) is an independent module  
- Modules connect using **mechanical locking pins + standardized electrical connectors**  
- Faulty modules can be replaced instantly — **no tools, no engineers**  
- The robot automatically detects and configures new modules  
- Materials can be customized (radiation-safe, chemical-resistant, lightweight)  

---

## 🧩 System Architecture (High-Level)
### 📊 Basic System Diagram

```text
User (Voice / Presence)
        ↓
Sensors (Camera, Mic)
        ↓
Raspberry Pi (Embedded Controller)
        ↓
Gemini API (AI Reasoning & NLP)
        ↓
Command Interpreter
        ↓
Module Manager
        ↓
Robot Modules (Arms, Head, Torso)
        ↓
Sensors → Feedback Loop → Raspberry Pi

```



The **Raspberry Pi** is physically embedded inside the robot and acts as the on-device controller, while the **Gemini API** provides advanced AI intelligence.

---

## ⚙️ How the System Works (End-to-End)

1. User interacts with Kritrim using voice or physical presence  
2. Sensors connected to the Raspberry Pi capture audio/video input  
3. Raspberry Pi preprocesses input and sends it to the Gemini API  
4. Gemini API performs intent recognition, reasoning, and response planning  
5. AI-generated commands are returned to the Raspberry Pi  
6. Raspberry Pi maps commands to specific robot modules  
7. Robot executes actions (movement, speech, guidance)  
8. Sensors continuously provide feedback for adaptive behavior  
9. If a module is removed or replaced, the system auto-reconfigures  

---

## 🧠 Technical Architecture

### Hardware Components

- Raspberry Pi (embedded inside robot)  
- Arduino (motor control)  
- Webcam, microphone, speaker  
- Servo motors (DS60 – 60kg, MG90s)  
- Snap-and-fit mechanical modules  

### Software & AI Stack

- Python  
- Gemini API (AI reasoning, NLP, decision-making)  
- Embedded Linux (Raspberry Pi OS)  
- Speech-to-Text API  
- Robotics control logic  

---

## ⚙️ Edge AI + Cloud Intelligence

Kritrim uses a **hybrid intelligence model**:

- Raspberry Pi handles real-time control and safety-critical actions  
- Gemini API provides advanced reasoning and language understanding  
- Low-latency execution happens locally  
- Cloud AI improves adaptability and intelligence  

This ensures **reliability, scalability, and responsiveness**.

---

## 📈 Scalability & Failure Handling

### Handling Growth

- Modular hardware enables mass production  
- Same robot platform adapts across industries  
- New modules can be added without redesign  

### Fault Tolerance

- Faulty modules are isolated automatically  
- Robot continues operating with remaining modules  
- Only the damaged module needs replacement  
- Logs enable predictive maintenance  

### Cost & Maintenance Advantage

- No full-robot replacement  
- Minimal downtime  
- Affordable for MSMEs  

---

## 🌍 Impact & Use Cases

### High-Risk Environments

- Radiology rooms  
- Chemical plants  
- Industrial zones  

### Service Environments

- MSMEs & reception desks  
- Hospitals  
- Libraries & public offices  
- Educational institutions  

### Key Benefits

- Improved human safety  
- Reduced operational cost  
- Increased efficiency  
- Adaptability across sectors  

---

## 👥 Team Contributions

### **Anuj Pateria**

- Led the **software development and AI integration**
- Designed and implemented the **voice assistant system**
- Integrated the AI assistant with **Raspberry Pi (embedded controller)**
- Handled **Python-based logic**, AI workflows, and on-device processing
- Managed overall **software architecture and system integration**
- Maintained documentation and GitHub repository structure

---

### **Shams Parvez**

- Worked on the **robot hardware architecture**
- Contributed to the **modular snap-and-fit design logic**
- Assisted in defining **robot movement and control flow**
- Helped align mechanical design with system requirements
- Supported overall architecture planning and validation

---

### **Shubham**

- Co-developed the **robot control logic**
- Worked on **modular system behavior and fault-handling logic**
- Assisted in defining **module interaction and coordination**
- Contributed to **end-to-end workflow design**
- Supported integration between hardware and software components

---

### **Baksheesh Singh**

- Led **research and analysis** related to humanoid and modular robotics
- Studied **existing systems, limitations, and innovation gaps**
- Contributed to **problem validation and use-case research**
- Assisted in documentation, references, and feasibility analysis
- Supported exceptional and miscellaneous project requirements

---

### 🤝 Team Collaboration

- All four members contributed **equally** to ideation, discussions, and decision-making
- The project was developed through **collaborative planning and execution**
- Each member played a critical role in making the system functional and scalable

---

## 📁 Repository Structure
```
HumanNoidRobot/
│
├── VideoExplanation
│   └── VideoExplanationLink
│   
├── docs/
│   └── system_architecture.png
│
├── research/
│   └── modular_robotics_notes.md
│
├── FlowChart/
│   ├── Phase1_HardwareDesign.md
│   └── Phase2_SoftwareDecisionTiming.md
│
├── src/
│   ├── assistant/
│   │   ├── main.py              # Voice assistant (Gemini + LiveKit)
│   │   ├── prompts.py           # AGENT_INSTRUCTION, SESSION_INSTRUCTION
│   │   └── requirements.txt     # livekit, google, python-dotenv
│   │
│   └── control/
│       └── robot_control.py     # Motor & module control logic (future)
│
├── README.md
├── ARCHITECTURE.md
├── SCALABILITY.md
└── TEAM.md

```

---

## 📚 Research & References

- Modularity in humanoid robot design (IEEE)  
- Advancements in humanoid robots – comprehensive review  
- India humanoid robot market outlook (2024–2030)  
- Studies on modular and distributed robotic systems  

---

## 🚀 Conclusion

Kritrim is a **practical, scalable, and Indian-centric humanoid robot** designed for real-world deployment.

By combining **modular hardware**, **snap-and-fit repairability**, **embedded edge control**, and **Gemini-powered AI**, Kritrim directly supports the vision of **Atmanirbhar Bharat** and **Digital India**.




