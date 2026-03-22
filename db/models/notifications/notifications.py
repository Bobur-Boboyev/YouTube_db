import enum
from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Enum, TIMESTAMP

from ..base import Base, TimestampMixin


class EntityType(str, enum.Enum):
    POST = "post"
    COMMENT = "comment"
    LIKE = "like"
    FOLLOW = "follow"


class Notification(Base, TimestampMixin):
    __tablename__ = "notifications"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    actor_user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
    )
    entity_type: Mapped[EntityType] = mapped_column(
        Enum(EntityType, name="entity_type_enum"),
        nullable=False,
        index=True,
    )
    entity_id: Mapped[int] = mapped_column(nullable=False, index=True)
    message: Mapped[str] = mapped_column(String, nullable=False)
    read_at: Mapped[datetime | None] = mapped_column(TIMESTAMP, nullable=True)

    user = relationship("User", foreign_keys=[user_id])
    actor = relationship("User", foreign_keys=[actor_user_id])
