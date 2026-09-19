import { useEffect, useState } from "react";

const API = "http://localhost:8000/api/v1";

type Road = {
  id: string;
  name: string;
  speed_kmh: number;
  congestion: number;
  queue_m: number;
  status: string;
};

type WhatIf = {
  intervention: string;
  road_id: string;
  duration_minutes: number;
};

export default function App() {
  const [roads, setRoads] = useState<Road[]>([]);
  const [network, setNetwork] = useState<any>({});
  const [forecast, setForecast] = useState<any[]>([]);
  const [selectedRoad, setSelectedRoad] = useState("R002");
  const [scenario, setScenario] = useState("lane_addition");
  const [result, setResult] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  async function load() {
    const [n, t, f] = await Promise.all([
      fetch(`${API}/network/status`).then(r => r.json()),
      fetch(`${API}/traffic/current`).then(r => r.json()),
      fetch(`${API}/traffic/forecast`).then(r => r.json()),
    ]);
    setNetwork(n);
    setRoads(t.roads);
    setForecast(f.horizons);
  }

  useEffect(() => {
    load().catch(console.error);
  }, []);

  async function simulate() {
    setLoading(true);
    try {
      const payload: WhatIf = {
        intervention: scenario,
        road_id: selectedRoad,
        duration_minutes: 60,
      };
      const response = await fetch(`${API}/simulation/what-if`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(payload),
      });
      setResult(await response.json());
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="app">
      <header>
        <div>
          <p className="eyebrow">URBANPULSE • DIGITAL TWIN</p>
          <h1>Virtual Traffic Control Room</h1>
          <p className="muted">Observe → Predict → Simulate → Compare → Redesign</p>
        </div>
        <div className="status">● SIMULATION MODE</div>
      </header>

      <main>
        <section className="metrics">
          <Metric title="Network health" value={`${network.network_health ?? "--"}%`} />
          <Metric title="Active alerts" value={network.active_alerts ?? "--"} />
          <Metric title="Critical segments" value={network.critical_segments ?? "--"} />
          <Metric title="Forecast horizon" value={`${network.forecast_horizon_minutes ?? "--"} min`} />
        </section>

        <section className="grid">
          <div className="panel map-panel">
            <div className="panel-title">
              <span>NETWORK DIGITAL TWIN</span>
              <span className="muted">Current state</span>
            </div>
            <div className="map">
              <div className="road r1"><span>R001</span></div>
              <div className="road r2"><span>R002 • CRITICAL</span></div>
              <div className="road r3"><span>R003</span></div>
              <div className="road r4"><span>R004</span></div>
              <div className="junction">J2</div>
            </div>
          </div>

          <div className="panel">
            <div className="panel-title">
              <span>ROAD CONDITIONS</span>
              <span className="muted">Now</span>
            </div>
            <div className="road-list">
              {roads.map(road => (
                <button
                  key={road.id}
                  className={`road-card ${selectedRoad === road.id ? "selected" : ""}`}
                  onClick={() => setSelectedRoad(road.id)}
                >
                  <div>
                    <strong>{road.name}</strong>
                    <small>{road.id} · {road.status}</small>
                  </div>
                  <div className="road-stats">
                    <b>{road.speed_kmh} km/h</b>
                    <span>Q {road.queue_m}m</span>
                  </div>
                </button>
              ))}
            </div>
          </div>
        </section>

        <section className="grid lower">
          <div className="panel">
            <div className="panel-title">
              <span>FORECAST</span>
              <span className="muted">Congestion index</span>
            </div>
            <div className="forecast">
              {forecast.map(item => (
                <div className="forecast-row" key={item.minutes}>
                  <span>+{item.minutes} min</span>
                  <div className="bar"><i style={{width: `${item.congestion_index * 100}%`}} /></div>
                  <b>{Math.round(item.congestion_index * 100)}%</b>
                  <small>{Math.round(item.confidence * 100)}% conf.</small>
                </div>
              ))}
            </div>
          </div>

          <div className="panel scenario">
            <div className="panel-title">
              <span>WHAT-IF SIMULATOR</span>
              <span className="muted">Advisory only</span>
            </div>

            <label>Target road</label>
            <select value={selectedRoad} onChange={e => setSelectedRoad(e.target.value)}>
              {roads.map(r => <option key={r.id} value={r.id}>{r.id} — {r.name}</option>)}
            </select>

            <label>Intervention</label>
            <select value={scenario} onChange={e => setScenario(e.target.value)}>
              <option value="diversion">Simulate diversion</option>
              <option value="road_closure">Close road</option>
              <option value="lane_addition">Add virtual lane</option>
              <option value="connector">Add connector</option>
              <option value="turning_lane">Add turning lane</option>
            </select>

            <button className="primary" onClick={simulate} disabled={loading}>
              {loading ? "Running digital twin..." : "Run simulation"}
            </button>

            {result && (
              <div className="result">
                <div className="result-grid">
                  <Result title="Delay" before={result.before.avg_delay_seconds} after={result.after.avg_delay_seconds} suffix=" sec" />
                  <Result title="Queue" before={result.before.max_queue_m} after={result.after.max_queue_m} suffix=" m" />
                  <Result title="Throughput" before={result.before.throughput_veh_h} after={result.after.throughput_veh_h} suffix=" veh/h" />
                </div>
                <p className="confidence">Simulation confidence: {Math.round(result.confidence * 100)}%</p>
              </div>
            )}
          </div>
        </section>

        <section className="panel infra">
          <div>
            <p className="eyebrow">FEATURE 10</p>
            <h2>Virtual Infrastructure Designer</h2>
            <p className="muted">Test road-network changes before recommending them in the real world.</p>
          </div>
          <div className="designer-options">
            <button>Add lane</button>
            <button>Add turning lane</button>
            <button>Add connector</button>
            <button>Change capacity</button>
            <button>Close road</button>
          </div>
        </section>
      </main>

      <footer>UrbanPulse • All interventions are simulated/advisory and require human review.</footer>
    </div>
  );
}

function Metric({title, value}: {title: string; value: string | number}) {
  return <div className="metric"><span>{title}</span><strong>{value}</strong></div>;
}

function Result({title, before, after, suffix}: {title: string; before: number; after: number; suffix: string}) {
  const delta = Math.round(((after - before) / before) * 100);
  return (
    <div>
      <span>{title}</span>
      <b>{before}{suffix} → {after}{suffix}</b>
      <small>{delta > 0 ? "+" : ""}{delta}%</small>
    </div>
  );
}
