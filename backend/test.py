import json
import httpx

async def fetch_cameras(page):
    timeout = httpx.Timeout(10.0)
    async with httpx.AsyncClient(timeout=timeout) as client:
        response = await client.get(f"http://localhost:8000/api/v1/cameras/{page}")
        response.raise_for_status()
        cameras = response.json()
        return cameras

import asyncio
cameras = asyncio.run(fetch_cameras(input("page >>> ")))
print(json.dumps(cameras, indent=4, ensure_ascii=False))
