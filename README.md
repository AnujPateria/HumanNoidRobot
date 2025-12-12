# 🤖 Kritrim: AI-Driven Multilingual Humanoid Robot

> **Team Ourobonics** | **SIH 2025 Grand Finalists**
> ![WhatsApp Image 2025-11-25 at 00 36 26_edaedef1](https://github.com/user-attachments/assets/bbe8c5e8-7ee5-4846-a6eb-50a90900cfa6)

>
> **Theme:** Smart Automation | **Problem Statement ID:** 25117
>
> **Focus:** Swadeshi for Atmanirbhar Bharat - Robotics and Drones

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![ROS](https://img.shields.io/badge/ROS-Noetic-green) ![LiveKit](https://img.shields.io/badge/LiveKit-RealTime-orange) ![Status](https://img.shields.io/badge/Status-Prototype-success)

## 📖 Overview

**Kritrim** is an affordable, emotion-aware humanoid robot designed to empower MSMEs (Micro, Small, and Medium Enterprises) and public service desks.

Unlike existing global solutions that cost between ₹20-60 Lakh, Kritrim provides an **indigenous, modular alternative costing significantly less (approx. ₹5-7 Lakh)**. It is engineered to automate repetitive tasks—such as answering FAQs, providing directions, and greeting visitors—while bridging language barriers through advanced multilingual NLP.

## 🎯 Key Features

* **🗣️ Multilingual Support:** Communicates fluently in English, Hindi, and regional languages to assist diverse demographics.
* **🎭 Emotion AI:** Detects user tone, pitch, and facial expressions to provide empathetic and consistent service.
* **👁️ AI Vision:** Capable of detecting customers and analyzing surroundings for better interaction using Computer Vision.
* **📉 Cost-Effective Hardware:** Built using Raspberry Pi and Arduino, making it accessible for small businesses.
* **📶 Offline Capability:** Designed to function effectively even without consistent internet connectivity.

---



## 🛠️ Tech Stack

### Hardware
| Component | Description |
| :--- | :--- |
| **Core Compute** | Raspberry Pi 4/5 |
| **Control** | Arduino, Servo Motors |
| **Sensors** | HD Cameras (Vision), Array Microphones |

### Software & AI
* **Languages:** Python, C++
* **Robotics Framework:** ROS (Robot Operating System)
* **Computer Vision:** OpenCV, TensorFlow Lite
* **NLP & Voice:** HuggingFace, Vosk / Google Speech-to-Text
* **Real-Time Comms:** LiveKit
* **Cloud/Backend:** AWS, Firebase

---

## ⚙️ Architecture

The system operates on a continuous feedback loop comprising four main stages:

```mermaid
graph TD
    A[Perception] -->|Audio & Visual Data| B(Processing)
    B -->|OpenCV/TF Lite| C{Decision Engine}
    B -->|LiveKit Streaming| C
    C -->|Emotion AI & NLP| D[Action]
    D -->|Servo Actuation| E[Gesture]
    D -->|Audio Playback| F[Response]
