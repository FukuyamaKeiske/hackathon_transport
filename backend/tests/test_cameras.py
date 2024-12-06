import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_list_cameras():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/api/v1/cameras/")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_create_camera():
    camera_data = {
        "longitude": 37.6173,
        "latitude": 55.7558,
        "url": "http://example.com/camera",
        "status": True
    }
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/api/v1/cameras/", json=camera_data)
        assert response.status_code == 200
        assert response.json()["url"] == camera_data["url"]
