
from datetime import date

from sqlalchemy import String, Integer, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base

class SMEProfile(Base):
    __tablename__ = "sme_profiles"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        unique=True,
        nullable=False
    )

    business_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    registration_number: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=True
    )

    industry: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    business_address: Mapped[str] = mapped_column(
        String(300),
        nullable=False
    )

    establishment_date: Mapped[date] = mapped_column(
        Date,
        nullable=True
    )

    user = relationship("User", backref="sme_profile")
    applications = relationship(
        "LoanApplication",
        back_populates="sme"
    )