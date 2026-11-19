
from datetime import datetime

from sqlalchemy import (
    Integer, String, Text, DateTime, ForeignKey
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from app.database.base import Base

class LoanAssessment(Base):
    __tablename__ = "loan_assessments"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    application_id: Mapped[int] = mapped_column(
        ForeignKey("loan_applications.id"),
        nullable=False
    )

    loan_officer_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    recommendation: Mapped[str] = mapped_column(
        String(30),
        nullable=False
    )

    remarks: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    assessed_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    application = relationship(
        "LoanApplication",
        back_populates="assessments"
    )

    loan_officer = relationship("User")