from datetime import datetime
import enum

from sqlalchemy import Integer, Enum, TIMESTAMP, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..base import Base, TimestampMixin


class SearchEntityType(str, enum.Enum):
    VIDEO = "video"
    CHANNEL = "channel"
    PLAYLIST = "playlist"


class SearchClick(Base, TimestampMixin):
    __tablename__ = "search_clicks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    query_id: Mapped[int] = mapped_column(
        ForeignKey("search_queries.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    user_id: Mapped[int | None] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )
    entity_type: Mapped[SearchEntityType] = mapped_column(
        Enum(SearchEntityType, name="search_entity_type_enum"),
        nullable=False,
        index=True,
    )
    entity_id: Mapped[int] = mapped_column(
        nullable=False,
        index=True,
    )
    position: Mapped[int] = mapped_column(nullable=False)
    clicked_at: Mapped[datetime] = mapped_column(
        TIMESTAMP,
        default=datetime.utcnow,
        index=True,
    )

    query = relationship("SearchQuery")
    user = relationship("User")