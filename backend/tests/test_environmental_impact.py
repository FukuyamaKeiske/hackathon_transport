import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_list_environmental_data():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/api/v1/environmental-impact/")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_create_environmental_data():
    environmental_data = {
        "timestamp": "2024-01-01T00:00:00Z",
        "longitude": 37.6173,
        "latitude": 55.7558,
        "emission_level": 50.0
    }
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/api/v1/environmental-impact/", json=environmental_data)
        assert response.status_code == 200
        assert response.json()["emission_level"] == environmental_data["emission_level"]
