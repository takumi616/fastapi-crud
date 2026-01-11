from fastapi import APIRouter, status
from app.crud import user as user_crud
from app.db.session import SessionDep
from app.schemas.user import UserCreateRequest, UserResponse


router = APIRouter(prefix="/users", tags=["users"])

@router.post("", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_new_user(session: SessionDep, req: UserCreateRequest) -> UserCreateRequest:
    user = await user_crud.insert_new_user(session, req)
    return user