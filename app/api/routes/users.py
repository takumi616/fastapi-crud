from fastapi import APIRouter, status
from app.crud import user as user_crud
from app.db.session import SessionDep
from app.models.user import User
from app.schemas.user import UserCreateRequest, UserResponse, UserUpdateRequest


router = APIRouter(prefix="/users", tags=["users"])

@router.post("", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_new_user(session: SessionDep, req: UserCreateRequest) -> User:
    return await user_crud.insert_new_user(session, req)

@router.get("", response_model=list[UserResponse], status_code=status.HTTP_200_OK)
async def get_user_list(session: SessionDep, skip: int = 0, limit: int = 100) -> list[User]:
    return await user_crud.select_user_list(session, skip, limit)

@router.get("/{id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
async def get_user_by_id(session: SessionDep, id: str) -> User:
    return await user_crud.select_user_by_id(session, id)

@router.put("/{id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
async def update_user(session: SessionDep, id: str, req: UserUpdateRequest) -> User:
    return await user_crud.update_user(session, id, req)