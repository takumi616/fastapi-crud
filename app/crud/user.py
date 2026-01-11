from app.db.session import SessionDep
from app.models.user import User
from app.schemas.user import UserCreateRequest


async def insert_new_user(session: SessionDep, req: UserCreateRequest) -> User:
    user = User(**req.model_dump())
    session.add(user)

    await session.commit()
    await session.refresh(user)

    return user
    

    
