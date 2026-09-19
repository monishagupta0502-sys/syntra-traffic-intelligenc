# 🚦 SYNTRA

### Urban Traffic Network Intelligence & Digital Twin Platform

> **Simulate the City Before It Moves.**

SYNTRA is an AI-powered **Urban Traffic Decision Intelligence Platform** that combines traffic forecasting, anomaly detection, incident intelligence, digital-twin simulation, and virtual infrastructure planning.

Instead of simply telling users **"traffic is high,"** SYNTRA helps answer:

* What is happening in the network?
* Why is congestion happening?
* What will happen in the next 15–60 minutes?
* How will congestion propagate?
* What happens if we divert traffic?
* What happens if a road is closed?
* Would adding a lane actually help?
* Could fixing one bottleneck create another?
* How could emergency traffic response be simulated?
* Which infrastructure changes produce measurable improvements?

All interventions are **virtual simulations/advisories** and do not control real-world traffic infrastructure.

---

## 🎯 Problem

Modern traffic systems generate large amounts of data, but identifying **network-wide causes and consequences** remains difficult.

Traditional traffic dashboards primarily show:

> Current traffic → Current congestion

SYNTRA goes further:

> **Observe → Understand → Predict → Simulate → Compare → Redesign**

This allows traffic planners and operators to experiment with interventions inside a **virtual representation of the road network** before considering real-world decisions.

---

# 🧠 Core Concept

SYNTRA is built around a **Traffic Digital Twin**.

The digital twin represents:

* Roads
* Junctions
* Lanes
* Traffic flow
* Vehicle speeds
* Capacity
* Queues
* Bottlenecks
* Incidents
* Network relationships

The system can then replay or simulate different scenarios and compare their outcomes.

### Example

A recurring bottleneck is detected.

SYNTRA can simulate:

```text
BASELINE
   ↓
Current traffic conditions
   ↓
Recurring bottleneck detected
   ↓
Infrastructure scenario
   ↓
Add virtual lane
   ↓
Run simulation
   ↓
Compare Before vs After
   ↓
Check secondary congestion
```

The system does not assume that an intervention is beneficial simply because the target road improves.

It also checks the **network-wide impact**.

---

# 🚀 Key Features

## 1. 🌐 Traffic Digital Twin

A virtual representation of an urban road network.

Displays:

* Road network
* Junctions
* Traffic conditions
* Road capacity
* Vehicle flow
* Average speed
* Queue length
* Network utilization

---

## 2. 📊 Current Traffic Intelligence

Monitor the current state of the network.

Each road can expose:

```text
Road ID
Current Speed
Traffic Flow
Capacity
Utilization
Queue Length
Congestion Level
```

Traffic conditions are visualized directly on the network map.

---

## 3. 🚨 Congestion & Anomaly Detection

Detect abnormal traffic behavior such as:

* Sudden speed drops
* Flow collapse
* Unexpected queue growth
* Road blockage
* Abnormal traffic propagation
* Unusual network behavior

The system compares observed traffic against expected traffic patterns.

---

## 4. 🚑 Incident Intelligence

SYNTRA can identify a **possible traffic incident** from abnormal network behavior.

Example:

```text
Sudden Speed Drop
       +
Flow Reduction
       +
Queue Growth
       +
Propagation to Nearby Roads
       ↓
Possible Incident
```

The system can estimate:

* Incident location
* Confidence
* Affected roads
* Expected impact
* Congestion propagation

> ⚠️ Incident detection is simulated/advisory in the demonstration environment.

---

## 5. 🔮 Traffic Forecasting

Forecast traffic conditions for:

```text
NOW
+15 min
+30 min
+45 min
+60 min
```

The system can forecast:

* Speed
* Flow
* Congestion
* Queue growth
* Potential bottlenecks

This allows operators to act **before congestion becomes severe**.

---

## 6. 🌊 Traffic Ripple & Spillback Prediction

Congestion rarely stays on one road.

SYNTRA models how congestion can propagate through connected roads and junctions.

Example:

```text
Incident
   ↓
Junction A
   ↓
Road B
   ↓
Junction C
   ↓
Road D
   ↓
Network Congestion
```

The system visualizes the expected propagation path.

---

# 🧪 7. What-If Simulation Lab

One of SYNTRA's core features.

Users can test hypothetical interventions without changing the real network.

Possible scenarios:

* 🚧 Close a road
* 🔀 Divert traffic
* ➕ Add a lane
* ➖ Remove a lane
* 🛣️ Change road capacity
* ↪️ Modify turning behavior
* 🔗 Add a connector road
* 🚦 Modify junction configuration

The system runs the scenario inside the digital twin.

---

# 📈 8. Before vs After Analysis

Every simulation can produce a comparison.

| Metric              | Baseline | Scenario | Change |
| ------------------- | -------: | -------: | -----: |
| Average Speed       |  24 km/h |  31 km/h |   +29% |
| Queue Length        |    850 m |    510 m |   -40% |
| Travel Time         |   18 min |   14 min |   -22% |
| Network Utilization |      91% |      78% |   -13% |

The values above are demonstration examples.

The platform uses simulation outputs rather than presenting recommendations as guaranteed real-world outcomes.

---

# 🏗️ 9. Virtual Infrastructure Designer

SYNTRA can be used as a **mini urban infrastructure laboratory**.

Select a recurring bottleneck and experiment with:

```text
Add Lane
     ↓
Modify Turning Lane
     ↓
Increase Capacity
     ↓
Add Connector Road
     ↓
Modify Junction
     ↓
Run Simulation
     ↓
Analyze Network Impact
```

The system also checks for **secondary effects**.

Example:

```text
Target Road
     ↓
Congestion decreases

BUT

Neighboring Road
     ↓
Traffic increases
```

This helps expose unintended network-level consequences.

---

# 🚦 10. Virtual Traffic Control Room

The main operational interface of SYNTRA.

The control room provides:

* Network overview
* Live/demo traffic state
* Incident alerts
* Forecast timeline
* Critical roads
* Bottleneck detection
* Emergency simulation
* Diversion simulation
* What-if scenarios
* Infrastructure simulations

It acts as a **virtual command center** rather than a navigation application.

---

# 🚑 11. Emergency Response Simulation

When a possible accident is detected, SYNTRA can simulate emergency response.

Example workflow:

```text
Possible Accident
       ↓
Determine Incident Location
       ↓
Identify Affected Roads
       ↓
Generate Candidate Routes
       ↓
Simulate Emergency Movement
       ↓
Compare Travel Times
       ↓
Display Emergency Corridor Advisory
```

The platform can display a simulated ambulance route and estimated travel time.

> ⚠️ SYNTRA does **not** dispatch real ambulances or communicate with real emergency services.
> Emergency response is strictly simulated/advisory for demonstration.

---

# 🎬 12. Demo Replay & Reset

SYNTRA includes a controlled demonstration environment.

### Demo flow

```text
Normal Traffic
      ↓
Congestion Appears
      ↓
Possible Incident
      ↓
Alert Generated
      ↓
Traffic Propagation
      ↓
Emergency Simulation
      ↓
Diversion Scenario
      ↓
Before / After Analysis
      ↓
Infrastructure Scenario
      ↓
Network Redesign
```

The demo can be:

* ▶️ Replayed
* ⏸️ Paused
* 🔄 Reset
* 🔁 Re-run from baseline

Resetting restores the original demonstration state.

---

# 🏛️ System Architecture

```text
                    ┌─────────────────────────┐
                    │      SYNTRA FRONTEND    │
                    │                         │
                    │ React + TypeScript      │
                    │ Maps + Charts            │
                    │ Control Room UI          │
                    └────────────┬────────────┘
                                 │
                                 │ REST / WebSocket
                                 ▼
                    ┌─────────────────────────┐
                    │       FASTAPI API       │
                    │                         │
                    │ Traffic Intelligence    │
                    │ Forecasting             │
                    │ Incidents               │
                    │ Simulations             │
                    │ Infrastructure          │
                    └────────────┬────────────┘
                                 │
              ┌──────────────────┼──────────────────┐
              │                  │                  │
              ▼                  ▼                  ▼
       ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
       │ ML ENGINE   │    │ ROAD GRAPH  │    │ SUMO ENGINE │
       │             │    │             │    │             │
       │ Forecasting │    │ OSMnx       │    │ Digital Twin│
       │ Anomaly     │    │ NetworkX    │    │ Simulation  │
       │ Detection   │    │ GeoPandas   │    │ TraCI       │
       └─────────────┘    └─────────────┘    └─────────────┘
              │                  │                  │
              └──────────────────┼──────────────────┘
                                 ▼
                    ┌─────────────────────────┐
                    │ PostgreSQL + PostGIS    │
                    │ Traffic / Network Data  │
                    │ Scenario Data           │
                    └─────────────────────────┘
```

---

# 🛠️ Tech Stack

## Frontend

| Technology        | Purpose                      |
| ----------------- | ---------------------------- |
| **React**         | UI framework                 |
| **TypeScript**    | Type-safe development        |
| **Vite**          | Frontend build tool          |
| **Tailwind CSS**  | UI styling                   |
| **Lucide React**  | Interface icons              |
| **Mapbox GL JS**  | Interactive traffic maps     |
| **Leaflet**       | Map fallback                 |
| **Recharts**      | Traffic & forecasting charts |
| **Framer Motion** | UI animations                |

---

## Backend

| Technology   | Purpose           |
| ------------ | ----------------- |
| **Python**   | Core backend & ML |
| **FastAPI**  | REST API          |
| **Pydantic** | Data validation   |
| **Uvicorn**  | API server        |

---

## Data Processing

| Technology    | Purpose                          |
| ------------- | -------------------------------- |
| **Pandas**    | Data processing                  |
| **NumPy**     | Numerical computation            |
| **GeoPandas** | Geospatial data                  |
| **NetworkX**  | Road graph analysis              |
| **OSMnx**     | OpenStreetMap network extraction |

---

## Machine Learning

| Technology             | Purpose                |
| ---------------------- | ---------------------- |
| **Scikit-learn**       | ML & anomaly detection |
| **XGBoost / LightGBM** | Traffic forecasting    |
| **PyTorch**            | Deep learning          |
| **PyTorch Geometric**  | Graph neural networks  |

Possible ML pipeline:

```text
Traffic Data
     ↓
Feature Engineering
     ↓
Baseline Model
     ↓
Anomaly Detection
     ↓
Forecasting
     ↓
Graph-based Propagation
     ↓
Simulation
```

---

## 🚗 Traffic Simulation

### SUMO — Simulation of Urban MObility

SUMO acts as the **digital-twin simulation engine**.

Used for:

* Vehicle simulation
* Road network simulation
* Traffic demand
* Congestion propagation
* Road closures
* Diversions
* Capacity changes
* Infrastructure scenarios
* Emergency route simulation

### TraCI

TraCI connects the Python backend with SUMO.

```text
FastAPI
   ↓
Python Simulation Service
   ↓
TraCI
   ↓
SUMO
   ↓
Simulation Results
   ↓
FastAPI
   ↓
React Dashboard
```

---

## 🗄️ Database

### PostgreSQL

Primary relational database.

### PostGIS

Used for geospatial information such as:

* Roads
* Coordinates
* Junctions
* Network geometry
* Incident locations

For early development:

```text
SQLite
```

can be used before migrating to PostgreSQL/PostGIS.

---

## ⚡ Optional Real-Time Layer

```text
Redis
WebSockets
```

Used for:

* Simulation progress
* Real-time dashboard updates
* Control-room events
* Live scenario status

---

## 🤖 AI Explanation Layer

An LLM can optionally be used for **natural-language explanations**.

For example:

> "Congestion on Road R42 is primarily associated with a capacity bottleneck at Junction J7. The +30 minute simulation indicates queue growth toward Road R51."

The LLM should explain structured outputs from the traffic system.

It should **not** be responsible for traffic physics or generating unsupported traffic recommendations.

---

# 📂 Project Structure

```text
syntra/
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── maps/
│   │   ├── charts/
│   │   ├── control-room/
│   │   ├── services/
│   │   └── data/
│   │
│   ├── package.json
│   └── vite.config.ts
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── ml/
│   │   ├── network/
│   │   ├── simulation/
│   │   ├── incidents/
│   │   └── infrastructure/
│   │
│   ├── tests/
│   └── requirements.txt
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── scenarios/
│
├── models/
│   ├── forecasting/
│   ├── anomaly/
│   └── incident/
│
├── simulation/
│   ├── networks/
│   ├── routes/
│   ├── scenarios/
│   ├── configs/
│   └── outputs/
│
├── notebooks/
│
├── scripts/
│
├── docker-compose.yml
├── .env.example
├── .gitignore
└── README.md
```

---

# 🔌 API Structure

| Endpoint                            | Purpose                    |
| ----------------------------------- | -------------------------- |
| `GET /api/network`                  | Get road network           |
| `GET /api/traffic/current`          | Current traffic state      |
| `GET /api/traffic/forecast`         | Traffic forecast           |
| `GET /api/incidents`                | Active incidents           |
| `GET /api/bottlenecks`              | Recurring bottlenecks      |
| `POST /api/diversions/simulate`     | Simulate diversion         |
| `POST /api/simulation/run`          | Run traffic scenario       |
| `POST /api/infrastructure/simulate` | Test infrastructure change |
| `GET /api/scenarios`                | Scenario library           |
| `POST /api/scenarios`               | Create scenario            |
| `GET /api/control-room/status`      | Control-room state         |

---

# 📊 Data Pipeline

```text
Traffic Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ├──────────────► Anomaly Detection
      │
      ├──────────────► Incident Detection
      │
      └──────────────► Forecasting
                              │
                              ▼
                       Network State
                              │
                              ▼
                      Digital Twin / SUMO
                              │
                  ┌───────────┴───────────┐
                  ▼                       ▼
            What-If Scenario       Infrastructure
                  │                  Scenario
                  └───────────┬───────────┘
                              ▼
                       Simulation Results
                              │
                              ▼
                       Before / After
                              │
                              ▼
                       Decision Support
```

---

# 🧪 Example Scenario

### Scenario: Road Incident

```text
18:42
Normal traffic
```

↓

```text
18:45
Sudden speed reduction detected
```

↓

```text
18:46
Flow collapse + queue growth
```

↓

```text
18:47
Possible incident detected
```

↓

```text
18:48
Affected roads identified
```

↓

```text
18:49
15–60 minute congestion forecast
```

↓

```text
18:50
Emergency response simulation
```

↓

```text
18:52
Diversion scenario simulated
```

↓

```text
18:55
Before vs After comparison
```

↓

```text
19:00
Infrastructure scenario tested
```

This turns SYNTRA from a simple traffic dashboard into a **decision-support and simulation platform**.

---

# 📈 Evaluation

SYNTRA can be evaluated using:

### Forecasting

* MAE
* RMSE
* MAPE

### Anomaly Detection

* Precision
* Recall
* F1-score
* Detection latency

### Incident Detection

* Detection accuracy
* False-positive rate
* Detection latency

### Simulation

* Average travel time
* Average speed
* Queue length
* Vehicle-hours
* Network throughput
* Congestion duration

### Infrastructure Scenarios

Compare:

```text
Baseline Network
       VS
Modified Network
```

across historical or simulated traffic demand.

---

# 🧩 Dataset Strategy

The project can combine multiple data sources.

### Primary Dataset

Competition/organizer-provided traffic dataset.

### Supporting Data

Potential sources include:

* Public traffic time-series datasets
* SUMO scenarios
* OpenStreetMap road networks
* Traffic anomaly datasets
* Incident datasets
* Traffic signal datasets
* Weather/event information where available

The final system should clearly distinguish:

```text
REAL DATA
SYNTHETIC DATA
SIMULATED DATA
DEMO DATA
```

---

# 🔐 Environment Variables

Create a `.env` file based on:

```text
.env.example
```

Important variables include:

```env
APP_ENV=development
BACKEND_PORT=8000

DATABASE_URL=postgresql://...

MAPBOX_ACCESS_TOKEN=...

SUMO_HOME=/path/to/sumo
SUMO_BINARY=sumo

LLM_PROVIDER=openai
LLM_API_KEY=...
LLM_MODEL=...

WEBSOCKET_ENABLED=true

EMERGENCY_SIMULATION_ENABLED=true
```

⚠️ **Never commit your real `.env` file or API keys to GitHub.**

---

# 💻 Local Development

## 1. Clone

```bash
git clone https://github.com/YOUR_USERNAME/syntra-traffic-intelligence.git

cd syntra
```

---

## 2. Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend:

```text
http://localhost:5173
```

---

## 3. Backend

```bash
cd backend

python3 -m venv .venv

source .venv/bin/activate

python3 -m pip install -r requirements.txt

uvicorn app.main:app --reload
```

Backend:

```text
http://localhost:8000
```

API documentation:

```text
http://localhost:8000/docs
```

---

# 🚗 SUMO Setup

Install SUMO and configure:

```env
SUMO_HOME=/path/to/sumo
SUMO_BINARY=sumo
SUMO_GUI_BINARY=sumo-gui
```

Verify:

```bash
sumo --version
```

For visual simulation:

```bash
sumo-gui
```

---

# 🐳 Docker

The project can optionally be run using Docker Compose.

```bash
docker compose up --build
```

Services:

```text
Frontend
Backend
PostgreSQL
PostGIS
Redis
```

---

# 🛡️ Safety & Scope

SYNTRA is designed as a **decision-support and simulation platform**.

It does not:

* Control real traffic signals
* Dispatch real ambulances
* Modify real roads
* Access roadside infrastructure
* Claim simulated incidents are real
* Automatically execute physical interventions

All emergency and traffic-management actions are:

> **SIMULATED / ADVISORY ONLY**

---

# 🗺️ Development Roadmap

## Phase 1 — Foundation

* [x] Frontend control room
* [x] Network visualization
* [x] Mock traffic data
* [x] Incident interface
* [x] Forecast interface
* [x] What-if interface
* [x] Infrastructure designer
* [x] Demo reset/replay

## Phase 2 — Data Intelligence

* [ ] Dataset integration
* [ ] Data preprocessing
* [ ] Traffic baseline modeling
* [ ] Anomaly detection
* [ ] Incident classification

## Phase 3 — Forecasting

* [ ] 15-minute prediction
* [ ] 30-minute prediction
* [ ] 45-minute prediction
* [ ] 60-minute prediction
* [ ] Spillback prediction

## Phase 4 — Digital Twin

* [ ] OSM road extraction
* [ ] SUMO network generation
* [ ] Traffic demand generation
* [ ] SUMO calibration
* [ ] TraCI integration

## Phase 5 — What-If Intelligence

* [ ] Diversion simulation
* [ ] Road closure simulation
* [ ] Lane modification
* [ ] Capacity modification
* [ ] Junction scenarios
* [ ] Infrastructure simulation

## Phase 6 — Decision Intelligence

* [ ] Evidence packets
* [ ] Confidence estimation
* [ ] Network-wide impact analysis
* [ ] Emergency response simulation
* [ ] Virtual control room integration

---

# ⭐ Why SYNTRA?

Traditional traffic systems often answer:

> **"Where is the traffic?"**

SYNTRA aims to answer:

> **"Why is the network behaving this way, what happens next, and what happens if we change it?"**

The central idea is:

```text
OBSERVE
   ↓
UNDERSTAND
   ↓
PREDICT
   ↓
SIMULATE
   ↓
COMPARE
   ↓
REDESIGN
```

---

# 🏆 Project Vision

SYNTRA aims to become a **virtual laboratory for urban mobility** where traffic operators, planners, and researchers can test interventions before implementing them in the real world.

Instead of experimenting on a real city:

```text
Real City
    │
    │ Traffic Data
    ▼
 SYNTRA DIGITAL TWIN
    │
    ├── Predict
    ├── Detect
    ├── Simulate
    ├── Compare
    └── Redesign
            │
            ▼
     Better-informed decisions
```

---

## 💡 One-Line Pitch

> **SYNTRA is a virtual traffic control room that doesn't just predict congestion—it lets cities simulate interventions and redesign their road networks before making real-world decisions.**

---

## 📜 License

This project is currently intended for **educational, research, and hackathon purposes**.

Add the final project license here when the repository licensing decision is made.

---

## 👥 Team

Built by the Team Fusion.

**Project:** Urban Traffic Network Intelligence & Digital Twin Platform

**Theme:** Smart Cities 
