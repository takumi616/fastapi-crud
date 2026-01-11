from enum import Enum
from typing import TYPE_CHECKING
from sqlalchemy import String, Enum as SAEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
import uuid
from sqlalchemy.dialects.postgresql import UUID

from app.models.base import Base


if TYPE_CHECKING:
    from app.models.user import User

# Enum for Task status
class TaskStatus(str, Enum):
    UNCOMPLETED = "uncompleted"
    COMPLETED = "completed"

class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    title: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    status: Mapped[TaskStatus] = mapped_column(
        SAEnum(TaskStatus),
        nullable=False,
    )

    users: Mapped[list["User"]] = relationship(
        secondary="task_users",
        back_populates="tasks",
    )