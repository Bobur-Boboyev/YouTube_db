from sqlalchemy import (
    BigInteger,
    ForeignKey,
    UniqueConstraint
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..base import Base, TimestampMixin


class PlaylistVideo(Base, TimestampMixin):
    __tablename__ = "playlist_videos"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    playlist_id: Mapped[int] = mapped_column(
        ForeignKey("playlists.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    video_id: Mapped[int] = mapped_column(
        ForeignKey("videos.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    position: Mapped[int] = mapped_column(nullable=False)
    added_by_user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
    )

    __table_args__ = (
        UniqueConstraint(
            "playlist_id",
            "video_id",
            name="uq_playlist_video_unique"
        ),
        UniqueConstraint(
            "playlist_id",
            "position",
            name="uq_playlist_position"
        ),
    )

    playlist = relationship("Playlist", back_populates="videos")
    video = relationship("Video")
    added_by = relationship("User")