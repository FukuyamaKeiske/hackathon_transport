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


from app.db.session import get_db
from app.db.schemas.users import UserBase
from app.db.models.users import User

router = APIRouter()

@router.post("/sign-up", response_model=UserBase)
async def sign_up(user: UserBase, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).filter(User.email == user.email))
    
    if result.scalars().first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Пользователь с таким адресом электронной почты уже существует."
        )
    new_user = await db.add(User(
        email=user.email,
        jwt_token=create_access_token(user.model_dump())
    ))
    await db.commit()
    await db.refresh(new_user)
    return new_user

