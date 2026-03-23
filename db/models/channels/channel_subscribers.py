from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, ForeignKey, Boolean, UniqueConstraint

from ..base import Base, TimestampMixin


class ChannelSubscriber(Base, TimestampMixin):
    __tablename__ = "channel_subscribers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    channel_id: Mapped[int] = mapped_column(
        ForeignKey("channels.id", ondelete="CASCADE"), nullable=False
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    notifications_enabled: Mapped[bool] = mapped_column(
        Boolean, nullable=False, default=False
    )

    __table_args__ = (UniqueConstraint("channel_id", "user_id"), )
