from datetime import datetime
import enum

from sqlalchemy import Integer, String, Enum, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column

from ..base import Base, TimestampMixin


class SearchType(str, enum.Enum):
    VIDEO = "video"
    CHANNEL = "channel"
    PLAYLIST = "playlist"


class SearchEntityType(str, enum.Enum):
    VIDEO = "video"
    CHANNEL = "channel"
    PLAYLIST = "playlist"


class SearchQuery(Base, TimestampMixin):
    __tablename__ = "search_queries"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    query_text: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True,
    )
    results_count: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )
    search_type: Mapped[SearchType] = mapped_column(
        Enum(SearchType, name="search_type_enum"),
        nullable=False,
        index=True,
    )