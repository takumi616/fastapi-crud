from sqlalchemy import select
from app.db.session import SessionDep
from app.models.user import User
from app.schemas.user import UserCreateRequest, UserUpdateRequest


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

async def select_user_by_id(session: SessionDep, id: str) -> User:
    statement = select(User).where(User.id == id)
    result = await session.execute(statement)
    return result.scalars().first()

async def update_user(session: SessionDep, id: str, req: UserUpdateRequest) -> User:
    statement = select(User).where(User.id == id)
    result = await session.execute(statement)
    user = result.scalars().first()

    update_dict = req.model_dump(exclude_unset=True)

    for key, value in update_dict.items():
        setattr(user, key, value)

    session.add(user)
    await session.commit()
    await session.refresh(user)

    return user
    
    
    