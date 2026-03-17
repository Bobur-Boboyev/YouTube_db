import enum

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey, Enum, UniqueConstraint, Index

from ..base import Base, TimestampMixin


class TypeReaction(str, enum.Enum):
    LIKE = "like"
    DISLIKE = "dislike"


class VideoReaction(Base, TimestampMixin):
    __tablename__ = "video_reactions"

    __table_args__ = (
        UniqueConstraint("video_id", "user_id", name="unique_reaction"),
        Index("idx_video_id", "video_id"),
        Index("idx_user_id", "user_id"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    video_id: Mapped[int] = mapped_column(
        ForeignKey("videos.id", ondelete="CASCADE"), nullable=False
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    type_reaction: Mapped[TypeReaction] = mapped_column(
        Enum(
            TypeReaction,
            name="type_reaction_enum",
            create_constraint=True,
            validate_strings=True,
        ),
        nullable=False,
    )

    video: Mapped["Video"] = relationship("Video", back_populates="reactions")
    user: Mapped["User"] = relationship("User", back_populates="reactions")
