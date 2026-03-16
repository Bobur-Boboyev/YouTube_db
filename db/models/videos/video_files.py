import enum

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey, Enum, BigInteger, UniqueConstraint

from ..base import Base, TimestampMixin


class VideoFormat(str, enum.Enum):
    MP4 = "mp4"
    WEBM = "webm"


class VideoResolution(str, enum.Enum):
    P120 = "120p"
    P240 = "240p"
    P360 = "360p"
    P480 = "480p"
    P720 = "720p"
    P1080 = "1080p"


class VideoFile(Base, TimestampMixin):
    __tablename__ = "video_files"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    video_id: Mapped[int] = mapped_column(
        ForeignKey("videos.id", ondelete="CASCADE"), nullable=False
    )
    format: Mapped[VideoFormat] = mapped_column(
        Enum(
            VideoFormat,
            name="video_format_enum",
            validate_strings=True,
            create_constraints=True,
        ),
        nullable=False,
    )
    resolution: Mapped[VideoResolution] = mapped_column(
        Enum(
            VideoResolution,
            name="video_resolution_enum",
            validate_strings=True,
            create_constraints=True,
        ),
        nullable=False,
    )
    bitrate: Mapped[int] = mapped_column(Integer, nullable=False)
    codec: Mapped[str] = mapped_column(String(20), nullable=False)
    file_size: Mapped[int] = mapped_column(BigInteger, nullable=False)
    storage_path: Mapped[str] = mapped_column(String, nullable=False)

    __table_args__ = UniqueConstraint(
        "video_id", "format", "resolution", name="unique_video"
    )

    video: Mapped["Video"] = relationship("Video", back_populates="files")
