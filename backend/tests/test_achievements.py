import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_list_achievements():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/api/v1/achievements/")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_create_achievement():
    achievement_data = {
        "operator_id": "some_operator_id",
        "achievement_type": "Test Achievement",
        "timestamp": "2024-01-01T00:00:00Z"
    }
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/api/v1/achievements/", json=achievement_data)
        assert response.status_code == 200
        assert response.json()["achievement_type"] == achievement_data["achievement_type"]
