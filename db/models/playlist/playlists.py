import enum

from sqlalchemy import (
    BigInteger,
    String,
    ForeignKey,
    Enum,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..base import Base, TimestampMixin


class PlaylistVisibility(str, enum.Enum):
    PUBLIC = "public"
    PRIVATE = "private"
    UNLISTED = "unlisted"


class Playlist(Base, TimestampMixin):
    __tablename__ = "playlists"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(String, nullable=True)
    visibility: Mapped[PlaylistVisibility] = mapped_column(
        Enum(PlaylistVisibility, name="playlist_visibility_enum"),
        default=PlaylistVisibility.PUBLIC,
        nullable=False,
    )
    thumbnail_url: Mapped[str | None] = mapped_column(String, nullable=True)
    videos_count: Mapped[int] = mapped_column(BigInteger, default=0)
    followers_count: Mapped[int] = mapped_column(BigInteger, default=0)

    user = relationship("User", back_populates="playlists")
    videos = relationship(
        "PlaylistVideo",
        back_populates="playlist",
        cascade="all, delete-orphan",
    )
    followers = relationship(
        "PlaylistFollower",
        back_populates="playlist",
        cascade="all, delete-orphan",
    )