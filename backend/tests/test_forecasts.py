import pytest
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_create_forecasts():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/api/v1/forecasts/")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_list_forecasts():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/api/v1/forecasts/")
        assert response.status_code == 200
        assert isinstance(response.json(), list)
