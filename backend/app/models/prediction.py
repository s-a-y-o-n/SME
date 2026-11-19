
from datetime import datetime

from sqlalchemy import (
    Integer, String, Float, DateTime, ForeignKey
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from app.database.base import Base

class Prediction(Base):
    __tablename__ = "predictions"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    application_id: Mapped[int] = mapped_column(
        ForeignKey("loan_applications.id"),
        nullable=False
    )

    model_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    default_probability: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    predicted_class: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    risk_category: Mapped[str] = mapped_column(
        String(30),
        nullable=False
    )

    model_version: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    application = relationship(
        "LoanApplication",
        back_populates="predictions"
    )