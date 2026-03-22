from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Boolean

from ..base import Base, TimestampMixin


class NotificationSettings(Base, TimestampMixin):
    __tablename__ = "notification_settings"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        unique=True,
    )
    email_enabled: Mapped[bool] = mapped_column(Boolean, default=True)
    push_enabled: Mapped[bool] = mapped_column(Boolean, default=True)
    in_app_enabled: Mapped[bool] = mapped_column(Boolean, default=True)
    new_subscriber_enabled: Mapped[bool] = mapped_column(Boolean, default=True)
    new_comment_enabled: Mapped[bool] = mapped_column(Boolean, default=True)
    comment_reply_enabled: Mapped[bool] = mapped_column(Boolean, default=True)
    video_like_enabled: Mapped[bool] = mapped_column(Boolean, default=True)

    user: Mapped["User"] = relationship(
        "User",
        back_populates="notification_settings",
    )
