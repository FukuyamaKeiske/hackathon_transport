import pytest
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_list_social_reports():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/api/v1/social-reports/")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_create_social_report():
    report_data = {
        "timestamp": "2024-01-01T00:00:00Z",
        "longitude": 37.6173,
        "latitude": 55.7558,
        "content": "Test report content",
        "source": "Twitter"
    }
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/api/v1/social-reports/", json=report_data)
        assert response.status_code == 200
        assert response.json()["content"] == report_data["content"]
