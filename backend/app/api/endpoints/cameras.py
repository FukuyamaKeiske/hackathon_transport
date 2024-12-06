from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.services.camera_management import get_cameras, get_camera_by_id, add_camera
from app.db.models.cameras import Camera

router = APIRouter()

@router.get("/", response_model=list[Camera])
async def list_cameras(db: AsyncSession = Depends(get_db)):
    cameras = await get_cameras(db)
    return cameras

@router.get("/{camera_id}", response_model=Camera)
async def read_camera(camera_id: str, db: AsyncSession = Depends(get_db)):
    camera = await get_camera_by_id(db, camera_id)
    if camera is None:
        raise HTTPException(status_code=404, detail="Camera not found")
    return camera

@router.post("/", response_model=Camera)
async def create_camera(camera_data: dict, db: AsyncSession = Depends(get_db)):
    new_camera = await add_camera(db, camera_data)
    return new_camera
