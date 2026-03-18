from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import (
    BigInteger,
    ForeignKey,
    Integer,
    Index,
    TIMESTAMP,
    UniqueConstraint,
)

from ..base import Base, TimestampMixin


class WatchHistory(Base, TimestampMixin):
    __tablename__ = "watch_history"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
    )
    video_id: Mapped[int] = mapped_column(
        ForeignKey("videos.id", ondelete="CASCADE"),
        nullable=False,
    )
    watched_seconds: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    progress_seconds: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    last_watched_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, nullable=False, default=datetime.utcnow
    )
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, nullable=False, default=datetime.utcnow
    )

    user = relationship("User", back_populates="watch_history")
    video = relationship("Video", back_populates="watch_history")

    __table_args__ = (
        UniqueConstraint("user_id", "video_id", name="unique_watch_history"),
        Index("idx_watch_history_user", "user_id"),
        Index("idx_watch_history_video", "video_id"),
    )
