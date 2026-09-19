from typing import Literal
from pydantic import BaseModel, Field


class WhatIfRequest(BaseModel):
    intervention: Literal[
        "diversion",
        "road_closure",
        "lane_addition",
        "connector",
        "turning_lane",
    ]
    road_id: str
    duration_minutes: int = Field(default=60, ge=5, le=240)


class InfrastructureScenarioRequest(BaseModel):
    road_id: str
    change_type: Literal[
        "add_lane",
        "remove_lane",
        "add_connector",
        "turning_lane",
        "capacity_change",
    ]
    value: float = Field(default=1.0, ge=-10, le=10)
