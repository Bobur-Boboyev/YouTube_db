import enum
from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey, Enum, TIMESTAMP, Boolean

from ..base import Base, TimestampMixin


class BanType(str, enum.Enum):
    TEMPORARY = "temporary"
    PERMANENT = "permanent"


class BannedUser(Base, TimestampMixin):
    __tablename__ = "banned_users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    banned_by: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
    )
    reason: Mapped[str | None] = mapped_column(String, nullable=True)
    ban_type: Mapped[BanType] = mapped_column(
        Enum(BanType, name="ban_type_enum"),
        nullable=False,
    )
    expires_at: Mapped[datetime | None] = mapped_column(TIMESTAMP, nullable=True)
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        index=True,
    )

    user = relationship("User", foreign_keys=[user_id])
    moderator = relationship("User", foreign_keys=[banned_by])
