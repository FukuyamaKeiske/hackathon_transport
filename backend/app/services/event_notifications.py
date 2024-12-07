import asyncio
from datetime import datetime, timedelta
import json
import httpx
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.events import Event

async def fetch_holidays_for_month(session, month, year):
    url = f"https://kayaposoft.com/enrico/json/v1.0/?action=getPublicHolidaysForMonth&month={month}&year={year}&country=rus"
    async with session.get(url) as response:
        data = await response.text()
        return json.loads(data)

async def fetch_holidays():
    today = datetime.now()
    current_year = today.year
    current_month = today.month

    tasks = []
    async with httpx.AsyncClient() as session:
        for month in range(current_month, 13):
            tasks.append(fetch_holidays_for_month(session, month, current_year))

        for month in range(1, 13):
            tasks.append(fetch_holidays_for_month(session, month, current_year + 1))

        results = await asyncio.gather(*tasks)

    all_holidays = []
    for monthly_holidays in results:
        for holiday in monthly_holidays:
            name = holiday["localName"]
            if name == "Праздник":
                name = "Праздничный день"
            all_holidays.append({
                "date": datetime(holiday["date"]["year"], holiday["date"]["month"], holiday["date"]["day"]).strftime('%Y-%m-%d'),
                "name": name,
                "type": "holiday"
            })

    # Добавление выходных дней
    start_date = today.replace(day=1)
    end_date = datetime(current_year + 1, 12, 31)
    current_date = start_date

    while current_date <= end_date:
        if current_date.weekday() in [5, 6]:  # Суббота и воскресенье
            all_holidays.append({
                "date": current_date.strftime('%Y-%m-%d'),
                "name": "Выходной",
                "type": "weekend"
            })
        current_date += timedelta(days=1)

    future_holidays = [holiday for holiday in all_holidays if datetime.strptime(holiday["date"], '%Y-%m-%d') >= today]
    future_holidays.sort(key=lambda holiday: holiday["date"])

    return future_holidays

async def get_events(db: AsyncSession):
    # Получаем события из базы данных
    result = await db.execute(Event.__table__.select())
    events = result.scalars().all()

    # Получаем праздники
    holidays = await fetch_holidays()

    # Объединяем события и праздники
    combined_events = []
    for event in events:
        combined_events.append({
            "name": event.name,
            "date": event.date.strftime('%Y-%m-%d'),
            "location": event.location,
            "impact_level": event.impact_level,
            "type": "event"
        })

    for holiday in holidays:
        combined_events.append({
            "name": holiday["name"],
            "date": holiday["date"],
            "location": "Россия",  # Можно изменить на конкретное местоположение
            "impact_level": 0,  # Для праздников можно установить уровень воздействия
            "type": holiday["type"]
        })

    return combined_events

async def add_event(db: AsyncSession, event_data: dict):
    new_event = Event(
        name=event_data['name'],
        date=event_data['date'],
        location=f"POINT({event_data['longitude']} {event_data['latitude']})",
        impact_level=event_data.get('impact_level', 1)
    )
    db.add(new_event)
    await db.commit()
    return new_event
