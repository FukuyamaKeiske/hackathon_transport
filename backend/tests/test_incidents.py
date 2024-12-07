import pytest
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_list_incidents():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/api/v1/incidents/")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_get_incident():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/api/v1/incidents/some_incident_id")
        assert response.status_code == 404  # Замените на существующий ID для успешного теста
