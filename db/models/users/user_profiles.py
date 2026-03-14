from datetime import date
import enum

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Date, Enum, ForeignKey

from ..base import Base, TimestampMixin


class GenderEnum(str, enum.Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"


class UserProfile(Base, TimestampMixin):
    __tablename__ = "user_profiles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False, unique=True
    )
    display_name: Mapped[str] = mapped_column(String(120), nullable=False)
    bio: Mapped[str] = mapped_column(String(500), nullable=True)
    avatar_url: Mapped[str] = mapped_column(String(500), nullable=True)
    banner_url: Mapped[str] = mapped_column(String(500), nullable=True)
    birth_date: Mapped[date] = mapped_column(Date, nullable=True)
    gender: Mapped[GenderEnum] = mapped_column(
        Enum(
            GenderEnum,
            name="gender_enum",
            create_constraint=True,
            validate_strings=True,
        ),
        nullable=True,
    )
    location: Mapped[str] = mapped_column(String(120), nullable=True)

    user: Mapped["User"] = relationship("User", back_populates="profile")
