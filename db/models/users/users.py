from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Boolean, TIMESTAMP, func

from ..base import Base, TimestampMixin


class User(Base, TimestampMixin):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(30), nullable=False)
    last_name: Mapped[str] = mapped_column(String(30), nullable=True)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    is_verified: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    is_banned: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    ban_reason: Mapped[str] = mapped_column(String, nullable=True)
    last_login_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, server_default=func.now(), nullable=False
    )
    password_changed_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, server_default=func.now(), nullable=False
    )
    two_factors_enabled: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
    deleted_at: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=True)
    email_verified_at = Mapped[datetime] = mapped_column(TIMESTAMP, nullable=True)

    profile: Mapped["UserProfile"] = relationship("UserProfile", back_populates="user")
    channels: Mapped[list["Channel"]] = relationship(
        "Channel", uselist=True, back_populates="user"
    )
    subscribed_channels: Mapped[list["Channel"]] = relationship(
        "Channel",
        secondary="channel_subscribers",
        uselist=True,
        back_populates="subscribers",
    )
    reactions: Mapped[list["VideoReaction"]] = relationship(
        "VideoReaction", uselist=True, back_populates="user"
    )
    watch_history: Mapped[list["WatchHistory"]] = relationship(
        "WatchHistory", back_populates="user", cascade="all, delete-orphan"
    )
    views: Mapped[list["VideoView"]] = relationship("VideoView", back_populates="user")
    watch_laters: Mapped[list["WatchLater"]] = relationship(
        "WatchLater", back_populates="user", cascade="all, delete-orphan"
    )
    comments: Mapped[list["Comment"]] = relationship(
        "Comment", back_populates="user", uselist=True
    )
    comment_reactions: Mapped[list["CommentReaction"]] = relationship(
        "CommentReaction", back_populates="user"
    )
