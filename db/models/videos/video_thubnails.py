import enum

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, BigInteger, Boolean, Enum, ForeignKey
from ..base import Base, TimestampMixin


class VideoThumbnailResolution(str, enum.Enum):
    P120 = "120p"
    P240 = "240p"
    P360 = "360p"
    P480 = "480p"
    P720 = "720p"
    P1080 = "1080p"


class VideoThumbnail(Base, TimestampMixin):
    __tablename__ = "video_thumbnails"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    video_id: Mapped[int] = mapped_column(
        ForeignKey("videos.id", ondelete="CASCADE"), nullable=False
    )
    thumbnail_url: Mapped[str] = mapped_column(String, nullable=False)
    resolution: Mapped[VideoThumbnailResolution] = mapped_column(
        Enum(
            VideoThumbnailResolution,
            name="thumbnail_resolution_enum",
            create_constraint=True,
            validate_strings=True,
        ),
        nullable=False,
    )
    width: Mapped[int] = mapped_column(Integer, nullable=False)
    height: Mapped[int] = mapped_column(Integer, nullable=False)
    is_default: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    video: Mapped["Video"] = relationship("Video", back_populates="thumbnails")
