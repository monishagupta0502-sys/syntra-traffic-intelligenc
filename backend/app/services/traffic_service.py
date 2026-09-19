from app.schemas.traffic import WhatIfRequest, InfrastructureScenarioRequest


def _roads():
    return [
        {
            "id": "R001",
            "name": "North Corridor",
            "speed_kmh": 24,
            "free_flow_kmh": 48,
            "congestion": 0.62,
            "queue_m": 420,
            "status": "congested",
        },
        {
            "id": "R002",
            "name": "Central Junction",
            "speed_kmh": 18,
            "free_flow_kmh": 42,
            "congestion": 0.78,
            "queue_m": 610,
            "status": "critical",
        },
        {
            "id": "R003",
            "name": "East Connector",
            "speed_kmh": 31,
            "free_flow_kmh": 45,
            "congestion": 0.41,
            "queue_m": 180,
            "status": "moderate",
        },
        {
            "id": "R004",
            "name": "South Arterial",
            "speed_kmh": 36,
            "free_flow_kmh": 50,
            "congestion": 0.28,
            "queue_m": 90,
            "status": "normal",
        },
    ]


def get_network_status():
    return {
        "network_health": 72,
        "active_alerts": 3,
        "critical_segments": 1,
        "forecast_horizon_minutes": 60,
        "simulation_mode": "digital_twin",
    }


def get_current_traffic():
    return {"timestamp": "demo", "roads": _roads()}


def get_forecast():
    return {
        "horizons": [
            {"minutes": 15, "congestion_index": 0.66, "confidence": 0.91},
            {"minutes": 30, "congestion_index": 0.71, "confidence": 0.87},
            {"minutes": 45, "congestion_index": 0.74, "confidence": 0.82},
            {"minutes": 60, "congestion_index": 0.77, "confidence": 0.76},
        ]
    }


def get_incidents():
    return [
        {
            "id": "INC-001",
            "type": "incident_like",
            "road_id": "R002",
            "severity": "high",
            "confidence": 0.88,
            "message": "Sharp localized speed drop with downstream queue growth.",
            "simulated": True,
        }
    ]


def run_what_if(request: WhatIfRequest):
    multipliers = {
        "diversion": 0.82,
        "road_closure": 1.24,
        "lane_addition": 0.76,
        "connector": 0.72,
        "turning_lane": 0.86,
    }
    factor = multipliers[request.intervention]

    return {
        "scenario": request.model_dump(),
        "simulation": {
            "engine": "demo-digital-twin",
            "status": "completed",
            "advisory_only": True,
        },
        "before": {
            "avg_delay_seconds": 184,
            "max_queue_m": 610,
            "throughput_veh_h": 2480,
        },
        "after": {
            "avg_delay_seconds": round(184 * factor),
            "max_queue_m": round(610 * factor),
            "throughput_veh_h": round(2480 * (1 + (1 - factor) * 0.22)),
        },
        "side_effects": [
            "Results are demo values until calibrated SUMO demand/network files are supplied."
        ],
        "confidence": 0.74,
    }


def run_infrastructure_scenario(request: InfrastructureScenarioRequest):
    factor = {
        "add_lane": 0.78,
        "remove_lane": 1.22,
        "add_connector": 0.70,
        "turning_lane": 0.84,
        "capacity_change": max(0.55, 1 - request.value * 0.08),
    }[request.change_type]

    return {
        "scenario": request.model_dump(),
        "before": {"avg_speed_kmh": 24, "queue_m": 610, "delay_seconds": 184},
        "after": {
            "avg_speed_kmh": round(24 / factor, 1),
            "queue_m": round(610 * factor),
            "delay_seconds": round(184 * factor),
        },
        "network_side_effect_check": {
            "status": "simulated",
            "secondary_congestion_detected": factor < 0.74,
        },
        "advisory_only": True,
    }


def get_control_room_summary():
    return {
        "network": get_network_status(),
        "top_alerts": get_incidents(),
        "forecast": get_forecast(),
        "recommended_actions": [
            {
                "action": "Simulate diversion around R002",
                "reason": "High congestion and queue growth",
                "confidence": 0.88,
            },
            {
                "action": "Evaluate virtual turning lane at R002",
                "reason": "Recurring junction bottleneck",
                "confidence": 0.76,
            },
        ],
    }
