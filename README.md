<p align="center">
  <img src="https://github.com/user-attachments/assets/bbe8c5e8-7ee5-4846-a6eb-50a90900cfa6" 
       alt="Team Ourobonics Winning Moment" width="100%">
</p>

# 🤖 Kritrim: Modular Snap-and-Fit Humanoid Robot

> **Team Ourobonics** | **AICTE Hardware Edition 2025 – Atmanirbhar Bharat**  
> **Problem Statement ID:** ID-25117  
> **Theme:** Robotics & Drones – Indigenous Automation  

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue">
  <img src="https://img.shields.io/badge/LiveKit-RealTime-orange">
  <img src="https://img.shields.io/badge/WebRTC-Enabled-green">
  <img src="https://img.shields.io/badge/Status-Prototype-success">
</p>

---

## 📖 Overview

**Kritrim** is an indigenous humanoid robot built using a **modular snap-and-fit architecture**, allowing any part (arms, head, panels, sensors) to be replaced or repaired **without technical expertise**.

It delivers a **multilingual AI assistant** capable of real-time speech interaction using LiveKit and Speech-to-Text APIs.

This modular, low-cost design makes Kritrim ideal for:

- MSME automation  
- Reception & help-desk workflows  
- Educational robotics labs  
- Rapid prototyping in research  

---

## 🎯 Key Features

### 🔧 **Snap-and-Fit Modular Architecture**
Easily replace or upgrade arms, torso, head unit, or sensors within minutes.

### 🗣️ **Multilingual AI Assistant**
LiveKit-powered real-time speech engine enabling interactions in multiple languages.

### 🤖 **On-Device Motion & Control**
Integrated motion logic for servo actuation and gesture control.

### 💸 **Affordable Indigenous Hardware**
Designed under the Atmanirbhar Bharat initiative using accessible components.

---

## 🛠️ Tech Stack

### **Hardware**
| Component | Description |
|----------|-------------|
| **Processor** | Microcontrollers (Arduino class) |
| **Actuation** | Servo Motors (modular snap-fit) |
| **Sensors** | Camera + Microphone modules |
| **Body** | 3D-printed snap-and-fit chassis |

### **Software**
- **Languages:** Python, C++  
- **Real-Time Engine:** LiveKit  
- **Communication:** WebRTC  
- **Speech Processing:** STT APIs  
- **Robotics Logic:** Motion control, state machine, module mapping  

---

## ⚙️ Architecture

```mermaid
graph TD
    A[Audio/Visual Input] -->|WebRTC Stream| B(Real-Time Engine: LiveKit)
    B -->|Speech-to-Text APIs| C[Processing Layer]
    C -->|Intent + Command| D{Decision Engine}
    D -->|Motion Logic| E[Servo Control]
    D -->|Voice Output| F[Multilingual Response]
    E --> G[Physical Gesture / Movement]
