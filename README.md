# 🚀 Mining Vehicle IoT Tracking System

## 📌 Overview
This project implements a GPS-based IoT system designed for mining vehicles to monitor operational efficiency and detect abnormal behavior.

The system tracks vehicle movement in real-time and identifies:
- Route deviation
- Idle behavior
- Simulated high fuel consumption patterns

---

## 🎯 Problem Statement
Mining operations often face challenges such as:
- Excessive idle time leading to fuel wastage
- Vehicles deviating from predefined routes
- Lack of visibility into operational inefficiencies

This project provides a practical IoT-based solution to address these issues using real-time tracking and analytics.

---

## ⚙️ System Architecture

---

## 🧠 Features

- 📍 Real-time vehicle tracking
- 🛣️ Route visualization on map
- ⚠️ Idle detection alerts
- ⚠️ Route deviation detection
- ⛽ Simulated fuel inefficiency detection
- 🌐 Fully deployed cloud-based system

---

## 🛠️ Tech Stack

### Backend
- Python (Flask)
- Flask-CORS

### Frontend
- HTML, JavaScript
- Mapbox GL JS

### Deployment
- Render (Backend hosting)
- Netlify (Frontend hosting)

---

## 📡 Data Flow

1. Simulator generates GPS data (latitude, longitude, speed, timestamp)
2. Data is sent to backend API
3. Backend processes data and applies detection logic
4. Alerts are generated based on conditions
5. Frontend fetches data periodically
6. Map updates vehicle position and alerts in real-time

---

## 🧪 Detection Logic

### Idle Detection
- If speed = 0 → "Idle detected"

### Route Deviation
- If vehicle crosses predefined boundary → "Route deviation"

### Fuel Consumption (Simulated)
Based on:
- Idle time
- Route inefficiency
- Speed variations

---

## 💻 Local Setup

### 1. Start Backend


### 2. Run Simulator


### 3. Open Frontend
Open `index.html` in your browser

---

## 🌐 Live Demo

- **Backend API:**  
  https://mining-iot-project.onrender.com/data

- **Frontend Dashboard:**  
  https://rad-churros-f1477d.netlify.app

---

## ⚠️ Mapbox Token Note

For security reasons, the Mapbox access token is not included in the repository.

To run locally, update:


---

## 🧩 Hardware Integration (Concept)

This implementation uses simulated GPS data.

In real deployment:
- Raspberry Pi will interface with GPS modules
- NMEA data will be parsed at the edge
- Processed data will be sent to backend via HTTP/MQTT

---

## 📈 Scalability

The system can be extended for large-scale deployment:
- Multi-vehicle tracking
- Cloud database integration
- Message brokers (Kafka/MQTT)
- Real-time analytics dashboards

---

## 🔮 Future Improvements

- Real GPS hardware integration
- Fuel sensor integration
- Multi-vehicle dashboard
- Heatmap visualization
- AI-based predictive analysis

---

## 🎥 Demo Video
(Add your Hindi video link here)

---

## 👨‍💻 Author
Aman Kumar  
Mining Engineering | IoT Enthusiast

---

## 📌 Conclusion
This project demonstrates a practical, scalable IoT solution for improving efficiency, safety, and monitoring in mining vehicle operations.
