
from datetime import datetime

from sqlalchemy import (
    Integer, String, Text, DateTime, ForeignKey
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from app.database.base import Base

class RMReview(Base):
    __tablename__ = "rm_reviews"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    application_id: Mapped[int] = mapped_column(
        ForeignKey("loan_applications.id"),
        nullable=False
    )

    rm_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    verification_status: Mapped[str] = mapped_column(
        String(30),
        nullable=False
    )

    remarks: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    reviewed_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    application = relationship(
        "LoanApplication",
        back_populates="reviews"
    )

    relationship_manager = relationship("User")