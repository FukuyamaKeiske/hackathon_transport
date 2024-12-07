import pytest
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_get_recommendations():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/api/v1/traffic-lights/recommendations")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_change_traffic_light_state():
    light_id = "some_light_id"  # Замените на существующий ID
    new_state = "green"
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.put(f"/api/v1/traffic-lights/{light_id}", json={"new_state": new_state})
        assert response.status_code == 200
        assert response.json()["current_state"] == new_state
