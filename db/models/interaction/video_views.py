from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import (
    BigInteger,
    Integer,
    ForeignKey,
    Boolean,
    TIMESTAMP,
    Index,
)

from ..base import Base


class VideoView(Base):
    __tablename__ = "video_views"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    video_id: Mapped[int] = mapped_column(
        ForeignKey("videos.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    user_id: Mapped[int | None] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )
    watch_time_seconds: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    completed: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, nullable=False, default=datetime.utcnow, index=True
    )

    video = relationship("Video")
    user = relationship("User")

    __table_args__ = (
        Index("idx_video_views_video_created", "video_id", "created_at"),
        Index("idx_video_views_user", "user_id"),
    )
