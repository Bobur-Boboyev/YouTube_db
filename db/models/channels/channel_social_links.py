import enum

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Enum, ForeignKey, UniqueConstraint

from ..base import Base, TimestampMixin


class ChannelSocialPlatformEnum(str, enum.Enum):
    EMAIL = "email"
    TWITTER = "twitter"
    INSTAGRAM = "instagram"
    TELEGRAM = "telegram"
    GITHUB = "github"
    LINKEDIN = "linkedin"
    WEBSITE = "website"


class ChannelSocialLink(Base, TimestampMixin):
    __tablename__ = "channel_social_links"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    channel_id: Mapped[int] = mapped_column(
        ForeignKey("channel.id", ondelete="CASCADE"),
        nullable=False,
    )
    platform: Mapped[SocialPlatformEnum] = mapped_column(
        Enum(
            SocialPlatformEnum,
            name="channel_social_platform_enum",
            create_constraint=True,
            validate_strings=True,
        ),
        nullable=False,
    )
    url: Mapped[str] = mapped_column(String(255), nullable=False)

    __table_args__ = (UniqueConstraint("channel_id", "platform"),)

    channel = relationship("Channel", back_populates="social_links", lazy="selectin")
