from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import BigInteger, ForeignKey, TIMESTAMP, Integer

from ..base import Base, TimestampMixin


class ChannelStatistics(Base, TimestampMixin):
    __tablename__ = "channel_statistics"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    channel_id: Mapped[int] = mapped_column(ForeignKey("channels.id", ondelete="CASCADE"), unique=True, nullable=False)

    total_subscribers: Mapped[int] = mapped_column(BigInteger, default=0, nullable=False)
    total_videos: Mapped[int] = mapped_column(BigInteger, default=0, nullable=False)
    total_views: Mapped[int] = mapped_column(BigInteger, default=0, nullable=False)
    total_watch_time: Mapped[int] = mapped_column(BigInteger, default=0, nullable=False)  # in seconds
    total_likes: Mapped[int] = mapped_column(BigInteger, default=0, nullable=False)
    total_comments: Mapped[int] = mapped_column(BigInteger, default=0, nullable=False)

    channel: Mapped["Channel"] = relationship("Channel", back_populates="statistics")