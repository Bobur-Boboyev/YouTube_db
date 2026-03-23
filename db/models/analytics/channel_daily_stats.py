from datetime import date

from sqlalchemy import (
    BigInteger,
    ForeignKey,
    Date,
    UniqueConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..base import Base, TimestampMixin


class ChannelDailyStats(Base, TimestampMixin):
    __tablename__ = "channel_daily_stats"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    channel_id: Mapped[int] = mapped_column(
        ForeignKey("channels.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    date_: Mapped[date] = mapped_column(Date, nullable=False, index=True)
    subscribers_gained: Mapped[int] = mapped_column(BigInteger, default=0)
    subscribers_lost: Mapped[int] = mapped_column(BigInteger, default=0)
    total_subscribers: Mapped[int] = mapped_column(BigInteger, default=0)
    videos_uploaded: Mapped[int] = mapped_column(BigInteger, default=0)
    views_count: Mapped[int] = mapped_column(BigInteger, default=0)
    watch_time_seconds: Mapped[int] = mapped_column(BigInteger, default=0)
    unique_viewers: Mapped[int] = mapped_column(BigInteger, default=0)
    likes_count: Mapped[int] = mapped_column(BigInteger, default=0)
    comments_count: Mapped[int] = mapped_column(BigInteger, default=0)
    shares_count: Mapped[int] = mapped_column(BigInteger, default=0)

    __table_args__ = (UniqueConstraint("channel_id", "date", name="uq_channel_date"),)

    channel = relationship("Channel")
