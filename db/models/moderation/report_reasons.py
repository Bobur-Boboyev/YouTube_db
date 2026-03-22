from sqlalchemy import BigInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from ..base import Base, TimestampMixin


class ReportReason(Base, TimestampMixin):
    __tablename__ = "report_reasons"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(String, nullable=True)
