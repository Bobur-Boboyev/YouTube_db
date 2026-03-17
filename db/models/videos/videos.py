import uuid
import enum
from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import (
    String,
    Integer,
    ForeignKey,
    Enum,
    TIMESTAMP,
    Text,
    CheckConstraint,
    Index,
)

from ..base import Base, TimestampMixin


class VideoVisibility(str, enum.Enum):
    PUBLIC = "public"
    UNLISTED = "unlisted"
    PRIVATE = "private"


class VideoStatus(str, enum.Enum):
    UPLOADING = "uploading"
    PROCESSING = "processing"
    READY = "ready"
    FAILED = "failed"
    BLOCKED = "blocked"


class Video(Base, TimestampMixin):
    __tablename__ = "videos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    channel_id: Mapped[int] = mapped_column(
        ForeignKey("channels.id", ondelete="CASCADE"), nullable=False
    )
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False, default="")
    uuid_: Mapped[str] = mapped_column(
        String(36), index=True, unique=True, default=lambda: str(uuid.uuid4())
    )
    visibility: Mapped[VideoVisibility] = mapped_column(
        Enum(
            VideoVisibility,
            name="video_visibility_enum",
            create_constraint=True,
            validate_strings=True,
        ),
        nullable=False,
        default=VideoVisibility.PUBLIC,
    )
    status: Mapped[VideoStatus] = mapped_column(
        Enum(
            VideoStatus,
            name="video_status_enum",
            create_constraint=True,
            validate_strings=True,
        ),
        nullable=False,
        default=VideoStatus.UPLOADING,
    )
    duration_seconds: Mapped[int] = mapped_column(Integer, nullable=False)
    language: Mapped[str] = mapped_column(String(10), nullable=False)
    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id", ondelete="CASCADE"), nullable=False
    )
    published_at: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=True)

    __table_args__ = (
        CheckConstraint("duration_seconds >= 0", name="check_video_duration_positive"),
        Index("idx_video_channel", "channel_id"),
        Index("idx_video_status", "status"),
        Index("idx_video_published", "published_at"),
    )

    channel: Mapped["Channel"] = relationship("Channel", back_populates="videos")
    category: Mapped["Category"] = relationship("Category", back_populates="videos")
    files: Mapped[list["VideoFile"]] = relationship(
        "VideoFile", back_populates="video", cascade="all, delete-orphan", uselist=True
    )
    thumbnails: Mapped[list["VideoThumbnail"]] = relationship(
        "VideoThumbnail",
        back_populates="video",
        cascade="all, delete-orphan",
        uselist=True,
    )
    tags: Mapped[list["Tag"]] = relationship(
        "Tag", secondary="video_tags", back_populates="videos", uselist=True
    )
    user_reactions: Mapped[list["User"]] = relationship(
        "User", secondary="video_reactions", back_populates="video_reactions"
    )
