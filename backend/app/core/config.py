import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "UrbanPulse"
    app_env: str = "development"
    debug: bool = True
    backend_host: str = "0.0.0.0"
    backend_port: int = 8000
    frontend_url: str = "http://localhost:5173"
    database_url: str = "postgresql://urbanpulse:urbanpulse@localhost:5432/urbanpulse"
    map_provider: str = "leaflet"
    sumo_binary: str = "sumo"
    sumo_timeout: int = 300
    forecast_horizons: str = "15,30,45,60"
    cors_origins: list[str] = ["http://localhost:5173", "http://localhost:3000"]

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
        case_sensitive=False,
    )


settings = Settings()
