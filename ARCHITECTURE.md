# 🧩 Kritrim – System Architecture

This document describes the **complete architecture** of **Kritrim**, an AI-driven modular snap-and-fit humanoid robot designed for **MSME empowerment** and **high-risk work environments**.

The architecture combines **edge intelligence** and **modular hardware design** to create a scalable, affordable, and maintainable humanoid system.

---

## 🧠 Architectural Overview

Kritrim follows a **hybrid Edge + Cloud architecture**:

- **Edge Layer (On-Robot):**
  - Handles real-time sensing, voice interaction, and actuation
  - Ensures low latency and safe operation
- **Cloud Layer (AI Intelligence):**
  - Performs advanced reasoning, NLP, and conversational intelligence
  - Enables continuous improvement and scalability

The robot is built using a **snap-and-fit modular hardware architecture**, allowing individual parts to be replaced or upgraded without technical expertise.

---

## 🏗️ High-Level Architecture Layers
```
User Interaction Layer
↓
Perception & Sensing Layer
↓
Embedded Control Layer (Raspberry Pi)
↓
AI Reasoning Layer (Gemini API)
↓
Decision & Command Layer
↓
Motion & Actuation Layer
↓
Feedback & Monitoring Loop
```
---


---

## ⚙️ Software Architecture

### 1️⃣ Voice Interaction & Perception Layer

- Captures **audio and video input** from the environment
- Uses microphone and camera mounted on the robot
- Integrated with **LiveKit** for:
  - Real-time audio/video streaming
  - Noise cancellation for industrial environments

---

### 2️⃣ Embedded AI Agent Layer (Edge)

- Runs on **Raspberry Pi**
- Implemented using **Python**
- Responsibilities:
  - Manage LiveKit agent sessions
  - Process real-time audio/video streams
  - Trigger AI requests and receive responses
  - Act as the bridge between AI decisions and robot control

Environment configuration is securely managed using `.env` files.

---

### 3️⃣ AI Reasoning Layer (Cloud)

- Powered by **Google Gemini Realtime API**
- Responsible for:
  - Natural Language Processing (NLP)
  - Context-aware reasoning
  - Intent understanding
  - Voice-based response generation
- AI behavior is configurable via:
  - Model selection
  - Temperature
  - Voice personality

---

### 4️⃣ Decision & Control Logic Layer

- Interprets AI output into actionable commands
- Maps user intent to:
  - Speech responses
- Designed to support:
  - Modular expansion

---

### 5️⃣ Motion & Actuation Layer

- Uses **Arduino** for low-level motor control
- Controls servo motors:
  - DS60 (60kg torque)
  - MG90s
- Separates real-time motor control from AI processing for stability
- Ensures smooth and safe movement execution

---

## 🧱 Hardware Architecture

Kritrim’s hardware is designed as a **set of independent snap-and-fit modules**.

---

### 🔩 Hardware Modules

#### 1️⃣ Central Processing Module (Torso Core)

- Raspberry Pi embedded inside the torso
- Acts as the **main system controller**
- Handles:
  - AI agent execution
  - Network communication
  - Module coordination

---

#### 2️⃣ Sensor & Perception Module (Head)

- Webcam for vision and presence detection
- Microphone for voice input
- Speaker for voice output
- Easily replaceable as a single unit

---

#### 3️⃣ Motion Control Module

- Arduino microcontroller
- Dedicated to motor and servo control
- Receives commands from Raspberry Pi

---

#### 4️⃣ Actuation Modules (Limbs)

- Modular arms and joints
- Driven by servo motors
- Snap-and-fit mechanical attachment
- Standardized electrical connectors
- Each part can be replaced independently

---

#### 5️⃣ Power Management Module

- Dedicated power distribution
- Separates motor power from logic power
- Protects sensitive electronics
- Designed for safe operation in hazardous environments

---

## 🔌 Snap-and-Fit Interface Design

- Mechanical locking pins for physical attachment
- Standardized connectors for power and data
- Tool-free module replacement
- Auto-detection of connected modules during startup

This design drastically reduces downtime and maintenance cost.

---

## 🔄 Hardware–Software Interaction Flow
```
User Voice / Video Input
↓
Sensor Module (Mic / Camera)
↓
Raspberry Pi (AI Agent + LiveKit)
↓
Gemini Realtime API (AI Reasoning)
↓
Intent / Decision Output
↓
Arduino (Motor Control)
↓
Actuation Modules (Movement / Gestures)
↓
Sensors & Feedback → Continuous Loop
```


---



---

## 📡 Communication Architecture

- **LiveKit** handles real-time communication
- **Gemini API** handles AI reasoning
- Secure environment variables via `.env`
- Designed for:
  - Low latency
  - High reliability
  - Scalable deployment

---

## 🛡️ Fault Tolerance & Reliability

- Faulty hardware modules can be isolated
- Robot continues operating with remaining modules
- No full-system shutdown required
- Logs support predictive maintenance

---

## 📈 Scalability Considerations

- Same AI backend can support multiple robots
- Modular hardware enables mass production
- New modules can be added without redesign
- Software architecture supports feature expansion

---

## 🌍 Deployment Flexibility

Kritrim can be configured for:

- MSMEs & reception desks
- Hospitals & radiology rooms
- Chemical plants
- Industrial zones
- Educational institutions
- Public service environments

Material customization allows safe operation in hazardous conditions.

---

## 🚀 Summary

The architecture of Kritrim combines:

- **Modular snap-and-fit hardware**
- **Edge AI for real-time control**
- **Cloud AI for advanced reasoning**
- **Scalability and affordability**

This makes Kritrim a **practical, Indian-centric humanoid robot** aligned with the vision of **Atmanirbhar Bharat** and **Digital India**.
