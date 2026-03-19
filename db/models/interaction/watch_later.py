from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from ..base import Base, TimestampMixin


class WatchLater(Base, TimestampMixin):
    __tablename__ = "watch_later"

    video_id: Mapped[int] = mapped_column(
        ForeignKey("videos.id", ondelete="CASCADE"), primary_key=True, nullable=False
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), primary_key=True, nullable=False
    )

    video: Mapped["Video"] = relationship("Video", back_populates="watch_laters")
    user: Mapped["User"] = relationship("User", back_populates="watch_laters")
