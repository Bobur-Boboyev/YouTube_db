import enum

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey, Enum

from ..base import Base, TimestampMixin


class CommentTypeReaction(str, enum.Enum):
    LIKE = "like"
    DISLIKE = "dislike"


class CommentReaction(Base, TimestampMixin):
    __tablename__ = "comment_reactions"

    comment_id: Mapped[int] = mapped_column(
        ForeignKey("comments.id", ondelete="CASCADE"), nullable=False, primary_key=True
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False, primary_key=True
    )
    reaction_type: Mapped[CommentTypeReaction] = mapped_column(
        Enum(
            CommentTypeReaction,
            name="comment_type_reaction_enum",
            create_constraint=True,
            validate_strings=True,
        ),
        nullable=False,
    )

    comment: Mapped["Comment"] = relationship("Comment", back_populates="reactions")
    user: Mapped["User"] = relationship("User", back_populates="comment_reactions")
