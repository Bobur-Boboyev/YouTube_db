from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey

from ..base import Base, TimestampMixin


class ChannelProfile(Base, TimestampMixin):
    __tablename__ = "channel_profiles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    channel_profile: Mapped[int] = mapped_column(
        ForeignKey("channels.id", ondelete="CASCADE"), unique=True, nullable=False
    )
    avatar_url: Mapped[str] = mapped_column(String(120), nullable=True)
    banner_url: Mapped[str] = mapped_column(String(120), nullable=True)
    location: Mapped[str] = mapped_column(String(120), nullable=True)

    social_links: Mapped[list["ChannelSocialLink"]] = relationship(
        "ChannelSocialLink", uselist=True, back_populates="channel", lazy="selectin"
    )
