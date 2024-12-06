from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.cameras import Camera

async def get_cameras(db: AsyncSession):
    result = await db.execute(Camera.__table__.select())
    return result.scalars().all()

async def get_camera_by_id(db: AsyncSession, camera_id: str):
    result = await db.execute(Camera.__table__.select().where(Camera.id == camera_id))
    return result.scalar_one_or_none()

async def add_camera(db: AsyncSession, camera_data: dict):
    new_camera = Camera(
        location=f"POINT({camera_data['longitude']} {camera_data['latitude']})",
        url=camera_data['url'],
        status=camera_data.get('status', True)
    )
    db.add(new_camera)
    await db.commit()
    return new_camera
