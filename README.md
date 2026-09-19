# UrbanPulse — AI Traffic Decision Intelligence Platform

UrbanPulse is a software-only virtual traffic control room for a Hyderabad-like urban road network.

It does not just predict congestion. It builds a digital twin of the road network, detects abnormal conditions, forecasts what may happen next, and lets operators test simulated interventions before recommending them.

## Core loop

**OBSERVE → UNDERSTAND → PREDICT → RESPOND → SIMULATE → COMPARE → REDESIGN**

## Main features

1. Traffic Digital Twin
2. Congestion & anomaly detection
3. Incident / bottleneck classification
4. 15–60 minute forecasting
5. Spillback & traffic ripple prediction
6. Diversion recommendation
7. What-if traffic simulation
8. Before/after impact analysis
9. Evidence & confidence engine
10. Virtual Infrastructure Designer
11. Virtual Traffic Control Room
12. Simulated emergency intelligence
13. Event/weather/roadwork scenario support

All interventions are advisory/simulated only. No live traffic-signal control, roadside sensor control, GPS-device integration, ambulance dispatch, or municipal infrastructure access is performed.

## Architecture

Frontend (React + TypeScript)
        |
        v
FastAPI backend
        |
        +--> Traffic state engine
        +--> Forecasting
        +--> Anomaly / incident detection
        +--> Recommendation engine
        +--> SUMO simulation
        +--> Infrastructure scenarios
        +--> Evidence/confidence
        |
        v
PostgreSQL/PostGIS + model/scenario files

## Technology

- Frontend: React, TypeScript, Vite, Tailwind CSS, Leaflet
- Backend: Python, FastAPI, Pydantic, Uvicorn
- Data: Pandas, NumPy, GeoPandas
- Network: NetworkX, OSMnx
- ML: scikit-learn, XGBoost
- Simulation: SUMO + TraCI
- Database: PostgreSQL + PostGIS
- Optional: Redis, WebSockets, PyTorch/PyTorch Geometric
- Testing: Pytest, Playwright
- AI narration: OpenAI-compatible API, optional

## Project structure

```text
urbanpulse/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── ml/
│   │   ├── network/
│   │   ├── simulation/
│   │   ├── incidents/
│   │   └── infrastructure/
│   └── tests/
├── frontend/
├── data/
│   ├── raw/
│   ├── processed/
│   └── scenarios/
├── models/
│   ├── forecasting/
│   ├── anomaly/
│   └── incident/
├── simulation/
│   ├── networks/
│   ├── routes/
│   ├── scenarios/
│   ├── configs/
│   └── outputs/
├── scripts/
├── .env.example
├── .gitignore
├── docker-compose.yml
└── README.md
```

## Quick start

### Backend

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

API docs:
`http://localhost:8000/docs`

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Open:
`http://localhost:5173`

### Docker

```bash
docker compose up --build
```

## Environment

Copy:

```bash
cp .env.example .env
```

Never commit `.env`.

## SUMO

Install SUMO separately and set `SUMO_HOME` in `.env`.

The starter project works without SUMO using deterministic demo simulation results. Replace the demo simulator with TraCI/SUMO once the network and demand files are ready.

## API endpoints

- `GET /api/v1/health`
- `GET /api/v1/network/status`
- `GET /api/v1/traffic/current`
- `GET /api/v1/traffic/forecast`
- `GET /api/v1/incidents`
- `POST /api/v1/simulation/what-if`
- `POST /api/v1/infrastructure/scenario`
- `GET /api/v1/control-room/summary`

## Development philosophy

Keep traffic reasoning deterministic and explainable.

The optional LLM layer should narrate structured evidence rather than decide traffic physics.

Every recommendation should contain:

- observed condition
- expected impact
- confidence
- affected roads
- possible side effects
- simulation evidence
- advisory status

## Competition demo

A strong demo flow:

1. Open the virtual control room.
2. Show a congested corridor.
3. Show the detected bottleneck.
4. Show +15/+30/+45/+60 minute forecast.
5. Select **Simulate Diversion**.
6. Compare before/after delay and queue length.
7. Open **Virtual Infrastructure Designer**.
8. Add a virtual lane or connector.
9. Run the scenario.
10. Show network-wide impact and side effects.
11. Return to the control room.

## License

Add the competition/team-specific license before public release.
