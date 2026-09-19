from fastapi import APIRouter

from app.schemas.traffic import WhatIfRequest, InfrastructureScenarioRequest
from app.services.traffic_service import (
    get_current_traffic,
    get_forecast,
    get_incidents,
    get_network_status,
    run_what_if,
    run_infrastructure_scenario,
    get_control_room_summary,
)

api_router = APIRouter()


@api_router.get("/health")
def health():
    return {"status": "ok", "service": "urbanpulse-backend"}


@api_router.get("/network/status")
def network_status():
    return get_network_status()


@api_router.get("/traffic/current")
def current_traffic():
    return get_current_traffic()


@api_router.get("/traffic/forecast")
def traffic_forecast():
    return get_forecast()


@api_router.get("/incidents")
def incidents():
    return get_incidents()


@api_router.post("/simulation/what-if")
def what_if(request: WhatIfRequest):
    return run_what_if(request)


@api_router.post("/infrastructure/scenario")
def infrastructure_scenario(request: InfrastructureScenarioRequest):
    return run_infrastructure_scenario(request)


@api_router.get("/control-room/summary")
def control_room_summary():
    return get_control_room_summary()
