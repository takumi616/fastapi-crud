from pydantic import BaseModel, ConfigDict
import uuid

class UserBase(BaseModel):
    name: str

class UserCreateRequest(UserBase):
    pass

class UserUpdateRequest(UserBase):
    pass

class UserResponse(UserBase):
    id: uuid.UUID

    model_config = ConfigDict(from_attributes=True)