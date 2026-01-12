from sqlalchemy import select
from app.db.session import SessionDep
from app.models.user import User
from app.schemas.user import UserCreateRequest


async def insert_new_user(session: SessionDep, req: UserCreateRequest) -> User:
    user = User(**req.model_dump())
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user

async def select_user_list(session: SessionDep, skip: int = 0, limit: int = 100) -> list[User]:
    statement = select(User).offset(skip).limit(limit)
    result = await session.execute(statement)
    return result.scalars().all()
