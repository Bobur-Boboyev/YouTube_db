import enum

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Enum, ForeignKey, UniqueConstraint

from ..base import Base, TimestampMixin


class UserSocialPlatformEnum(str, enum.Enum):
    EMAIL = "email"
    TWITTER = "twitter"
    INSTAGRAM = "instagram"
    TELEGRAM = "telegram"
    GITHUB = "github"
    LINKEDIN = "linkedin"
    WEBSITE = "website"


class UserSocialLink(Base, TimestampMixin):
    __tablename__ = "user_social_links"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
    )
    platform: Mapped[UserSocialPlatformEnum] = mapped_column(
        Enum(
            UserSocialPlatformEnum,
            name="user_social_platform_enum",
            create_constraint=True,
            validate_strings=True,
        ),
        nullable=False,
    )
    url: Mapped[str] = mapped_column(String(255), nullable=False)

    __table_args__ = (UniqueConstraint("user_id", "platform"),)

    user_profile = relationship("UserProfile", back_populates="social_links")
