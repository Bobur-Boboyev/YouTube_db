from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String

from ..base import Base, TimestampMixin


class Tag(Base, TimestampMixin):
    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    slug: Mapped[str] = mapped_column(String(200), unique=True, nullable=False)

    videos: Mapped[list["Video"]] = relationship(
        "Video", secondary="video_tags", uselist=True, back_populates="tags"
    )
