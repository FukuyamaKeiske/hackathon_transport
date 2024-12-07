import pytest
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_list_notifications():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/api/v1/notifications/")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_create_notification():
    notification_data = {
        "timestamp": "2024-01-01T00:00:00Z",
        "driver_id": "some_driver_id",
        "message": "Test notification message"
    }
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/api/v1/notifications/", json=notification_data)
        assert response.status_code == 200
        assert response.json()["message"] == notification_data["message"]
