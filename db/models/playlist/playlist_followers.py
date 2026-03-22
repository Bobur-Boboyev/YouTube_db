from sqlalchemy import (
    BigInteger,
    ForeignKey,
    UniqueConstraint
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..base import Base, TimestampMixin


class PlaylistFollower(Base, TimestampMixin):
    __tablename__ = "playlist_followers"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    playlist_id: Mapped[int] = mapped_column(
        ForeignKey("playlists.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    __table_args__ = (
        UniqueConstraint(
            "playlist_id",
            "user_id",
            name="uq_playlist_follower"
        ),
    )

    playlist = relationship("Playlist", back_populates="followers")
    user = relationship("User")