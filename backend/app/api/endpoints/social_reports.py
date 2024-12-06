from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.services.social_media_integration import get_social_reports, add_social_report
from app.db.models.social_reports import SocialReport

router = APIRouter()

@router.get("/", response_model=list[SocialReport])
async def list_social_reports(db: AsyncSession = Depends(get_db)):
    social_reports = await get_social_reports(db)
    return social_reports

@router.post("/", response_model=SocialReport)
async def create_social_report(report_data: dict, db: AsyncSession = Depends(get_db)):
    new_report = await add_social_report(db, report_data)
    return new_report
