from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, ForeignKey

from ..base import Base, TimestampMixin


class VideoTags(Base, TimestampMixin):
    __tablename__ = "video_tags"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    video_id: Mapped[int] = mapped_column(ForeignKey("videos.id", ondelete="CASCADE"), nullable=False)
    tag_id: Mapped[int] = mapped_column(ForeignKey("tags.id", ondelete="CASCADE"), nullable=False)