from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Boolean, ForeignKey

from ..base import Base, TimestampMixin


class Channel(Base, TimestampMixin):
    __tablename__ = "channels"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    owner_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    handle: Mapped[str] = mapped_column(
        String(50), unique=True, index=True, nullable=False
    )
    description: Mapped[str] = mapped_column(String(500), nullable=True)
    is_verified: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    user: Mapped["User"] = relationship(
        "User", lazy="selectin", back_populates="channels"
    )
    categories: Mapped[list["Category"]] = relationship(
        "Category",
        secondary="channel_categories",
        back_populates="channels",
        lazy="selectin",
    )
