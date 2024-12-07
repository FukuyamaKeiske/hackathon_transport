import pytest
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_list_scenarios():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/api/v1/scenarios/")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_create_scenario():
    scenario_data = {
        "name": "Test Scenario",
        "description": "Description of the test scenario",
        "impact_assessment": {"data": "impact"}
    }
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/api/v1/scenarios/", json=scenario_data)
        assert response.status_code == 200
        assert response.json()["name"] == scenario_data["name"]
