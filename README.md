🤖 Kritrim: Modular Snap-and-Fit Humanoid Robot

Team Ourobonics | AICTE Hardware Edition 2025 – Atmanirbhar Bharat
Problem Statement ID: ID-25117
Theme: Robotics & Drones – Indigenous Automation

📖 Overview

Kritrim is an indigenous humanoid robot designed using a modular snap-and-fit architecture, enabling rapid part replacement, repair, and customization without requiring technical expertise.

Built with the goal of contributing to Atmanirbhar Bharat, Kritrim is a cost-effective, scalable hardware platform that supports multilingual assistance through a real-time communication engine.

This design makes it ideal for:

Educational labs

MSME automation

Reception & help-desk workflows

Robotics research and rapid prototyping

🎯 Key Features

🧩 Snap-and-Fit Modular Body
Replace or upgrade components (arms, head, sensors, panels) quickly with zero technical skills.

🗣️ Multilingual Assistant (LiveKit)
Responds and interacts in multiple languages using a real-time voice module.

🎙️ Natural Human Interaction
Real-time speech processing and dynamic response generation.

⚙️ Low-Cost Indigenous Hardware
Built with easily available components for affordability and maintainability.

🔧 Repair-Friendly Design
Anyone can detach and replace faulty parts in minutes.

🛠️ Tech Stack
Hardware
Component	Description
Processing	Microcontrollers (Arduino Class)
Actuation	Servo Motors (modular fit)
Sensors	Cameras, Microphone modules
Chassis	3D-printed modular snap-fit parts
Software

Languages: Python, C++

Real-Time Engine: LiveKit

Communication: WebRTC

Speech Processing: Speech-to-Text APIs

Robotics Logic: Motion control, module mapping, state machine

⚙️ Architecture

Updated to match the resume (LiveKit + STT + Motion logic):

graph TD
    A[Audio/Visual Input] -->|WebRTC Stream| B(Real-Time Engine: LiveKit)
    B -->|Speech-to-Text APIs| C[Processing Layer]
    C -->|Intent + Command| D{Decision Engine}
    D -->|Motion Logic| E[Servo Control]
    D -->|Voice Response| F[Audio Output]
    E --> G[Physical Gesture / Movement]
    F --> H[Multilingual Response]

