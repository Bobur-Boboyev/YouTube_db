import enum
from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, Text, ForeignKey, Enum, TIMESTAMP

from ..base import Base, TimestampMixin

import enum


class ReportEntityType(str, enum.Enum):
    VIDEO = "video"
    COMMENT = "comment"
    USER = "user"


class ReportStatus(str, enum.Enum):
    PENDING = "pending"
    REVIEWED = "reviewed"
    REJECTED = "rejected"


class Report(Base, TimestampMixin):
    __tablename__ = "reports"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    reporter_user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    entity_type: Mapped[ReportEntityType] = mapped_column(
        Enum(ReportEntityType, name="report_entity_type_enum"),
        nullable=False,
        index=True,
    )
    entity_id: Mapped[int] = mapped_column(nullable=False, index=True)
    reason_id: Mapped[int] = mapped_column(
        ForeignKey("report_reasons.id", ondelete="SET NULL"),
        nullable=True,
    )
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    status: Mapped[ReportStatus] = mapped_column(
        Enum(ReportStatus, name="report_status_enum"),
        default=ReportStatus.PENDING,
        nullable=False,
        index=True,
    )
    reviewed_by: Mapped[int | None] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
    )
    reviewed_at: Mapped[datetime | None] = mapped_column(TIMESTAMP, nullable=True)

    reporter = relationship("User", foreign_keys=[reporter_user_id])
    reviewer = relationship("User", foreign_keys=[reviewed_by])
    reason = relationship("ReportReason")
