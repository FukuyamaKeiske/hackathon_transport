from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.services.camera_management import get_cameras_data
from pydantic import BaseModel
from typing import List

router = APIRouter()

class CameraResponse(BaseModel):
    name: str
    live_url: str
    geo: str
    description: str

@router.get("/{page}", response_model=List[CameraResponse])
async def list_cameras(page: str, db: AsyncSession = Depends(get_db)):
    cameras = await get_cameras_data(page)
    return cameras
