from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)

from app.core.security import (
    create_access_token
)


from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Dict

from app.db.session import get_db
from app.db.schemas.users import UserLogin
from app.db.models.users import User

router = APIRouter()

@router.post("/sign-in", response_model=Dict[str, str])
async def sign_up(user: UserLogin, db: AsyncSession = Depends(get_db)):
    tried_token = create_access_token(user.model_dump())
    result = await db.execute(select(User).filter(User.jwt_token == user.model_dump()))

    
    if not result.scalars().first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Такого пользователя не сущетсвует."
        )
    return {"token": tried_token}

