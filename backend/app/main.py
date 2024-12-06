from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.api.endpoints import (
    traffic_analysis,
    incidents,
    cameras,
    forecasts,
    events,
    traffic_lights,
    effectiveness,
    scenarios,
    social_reports,
    notifications,
    environmental_impact,
    achievements
)
from app.core.config import settings

app = FastAPI(title="Traffic Management System")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Для разработки, изменить на конкретные домены в продакшене
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключение маршрутов
app.include_router(traffic_analysis.router, prefix="/api/v1/traffic-analysis", tags=["Traffic Analysis"])
app.include_router(incidents.router, prefix="/api/v1/incidents", tags=["Incidents"])
app.include_router(cameras.router, prefix="/api/v1/cameras", tags=["Cameras"])
app.include_router(forecasts.router, prefix="/api/v1/forecasts", tags=["Forecasts"])
app.include_router(events.router, prefix="/api/v1/events", tags=["Events"])
app.include_router(traffic_lights.router, prefix="/api/v1/traffic-lights", tags=["Traffic Lights"])
app.include_router(effectiveness.router, prefix="/api/v1/effectiveness", tags=["Effectiveness"])
app.include_router(scenarios.router, prefix="/api/v1/scenarios", tags=["Scenarios"])
app.include_router(social_reports.router, prefix="/api/v1/social-reports", tags=["Social Reports"])
app.include_router(notifications.router, prefix="/api/v1/notifications", tags=["Notifications"])
app.include_router(environmental_impact.router, prefix="/api/v1/environmental-impact", tags=["Environmental Impact"])
app.include_router(achievements.router, prefix="/api/v1/achievements", tags=["Achievements"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
