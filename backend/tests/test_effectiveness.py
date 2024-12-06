import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_list_effectiveness():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/api/v1/effectiveness/")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_create_effectiveness_measure():
    measure_data = {
        "measure_id": "some_measure_id",
        "before": {"data": "before"},
        "after": {"data": "after"},
        "effectiveness_score": 0.85
    }
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/api/v1/effectiveness/", json=measure_data)
        assert response.status_code == 200
        assert response.json()["effectiveness_score"] == measure_data["effectiveness_score"]
