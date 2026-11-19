
from datetime import datetime

from sqlalchemy import (
    Integer, String, Numeric, DateTime,
    ForeignKey
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from app.database.base import Base

class LoanApplication(Base):
    __tablename__ = "loan_applications"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    sme_id: Mapped[int] = mapped_column(
        ForeignKey("sme_profiles.id"),
        nullable=False
    )

    assigned_rm_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=True
    )

    loan_amount: Mapped[float] = mapped_column(
        Numeric(15, 2),
        nullable=False
    )

    loan_purpose: Mapped[str] = mapped_column(
        String(300),
        nullable=False
    )

    tenure_months: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(40),
        default="submitted",
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    sme = relationship(
        "SMEProfile",
        back_populates="applications"
    )

    assigned_rm = relationship(
        "User",
        foreign_keys=[assigned_rm_id]
    )

    financial_data = relationship(
        "FinancialData",
        back_populates="application",
        uselist=False
    )

    reviews = relationship(
        "RMReview",
        back_populates="application"
    )

    predictions = relationship(
        "Prediction",
        back_populates="application"
    )

    assessments = relationship(
        "LoanAssessment",
        back_populates="application"
    )