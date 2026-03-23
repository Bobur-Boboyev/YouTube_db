from datetime import date

from sqlalchemy import (
    BigInteger,
    ForeignKey,
    Date,
    UniqueConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..base import Base, TimestampMixin


class VideoDailyStats(Base, TimestampMixin):
    __tablename__ = "video_daily_stats"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    video_id: Mapped[int] = mapped_column(
        ForeignKey("videos.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    date_: Mapped[date] = mapped_column(Date, nullable=False, index=True)
    views_count: Mapped[int] = mapped_column(BigInteger, default=0)
    unique_viewers: Mapped[int] = mapped_column(BigInteger, default=0)
    watch_time_seconds: Mapped[int] = mapped_column(BigInteger, default=0)
    likes_count: Mapped[int] = mapped_column(BigInteger, default=0)
    dislikes_count: Mapped[int] = mapped_column(BigInteger, default=0)
    comments_count: Mapped[int] = mapped_column(BigInteger, default=0)
    shares_count: Mapped[int] = mapped_column(BigInteger, default=0)
    average_watch_duration: Mapped[int] = mapped_column(BigInteger, default=0)
    completion_rate: Mapped[float] = mapped_column(default=0.0)

    __table_args__ = (UniqueConstraint("video_id", "date_", name="uq_video_date"),)

    video = relationship("Video")
