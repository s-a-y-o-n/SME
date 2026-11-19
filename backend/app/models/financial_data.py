
from sqlalchemy import (
    Integer, Numeric, ForeignKey
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base

class FinancialData(Base):
    __tablename__ = "financial_data"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    application_id: Mapped[int] = mapped_column(
        ForeignKey("loan_applications.id"),
        unique=True,
        nullable=False
    )

    annual_revenue: Mapped[float] = mapped_column(
        Numeric(15, 2),
        nullable=False
    )

    annual_expenses: Mapped[float] = mapped_column(
        Numeric(15, 2),
        nullable=False
    )

    net_profit: Mapped[float] = mapped_column(
        Numeric(15, 2),
        nullable=False
    )

    total_debt: Mapped[float] = mapped_column(
        Numeric(15, 2),
        nullable=False
    )

    current_assets: Mapped[float] = mapped_column(
        Numeric(15, 2),
        nullable=False
    )

    current_liabilities: Mapped[float] = mapped_column(
        Numeric(15, 2),
        nullable=False
    )

    years_in_business: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    employee_count: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    existing_loan_count: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    application = relationship(
        "LoanApplication",
        back_populates="financial_data"
    )