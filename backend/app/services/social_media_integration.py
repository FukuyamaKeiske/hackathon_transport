from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.social_reports import SocialReport

async def get_social_reports(db: AsyncSession):
    result = await db.execute(SocialReport.__table__.select())
    return result.scalars().all()

async def add_social_report(db: AsyncSession, report_data: dict):
    new_report = SocialReport(
        timestamp=report_data['timestamp'],
        location=f"POINT({report_data['longitude']} {report_data['latitude']})",
        content=report_data['content'],
        source=report_data['source']
    )
    db.add(new_report)
    await db.commit()
    return new_report
