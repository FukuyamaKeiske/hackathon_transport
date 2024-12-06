import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_list_events():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/api/v1/events/")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_create_event():
    event_data = {
        "name": "Test Event",
        "date": "2024-01-01T00:00:00Z",
        "longitude": 37.6173,
        "latitude": 55.7558,
        "impact_level": 1
    }
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/api/v1/events/", json=event_data)
        assert response.status_code == 200
        assert response.json()["name"] == event_data["name"]
