
from app.database.connection import engine
from app.database.base import Base

# Import all models so SQLAlchemy registers them
from app.models import (
    User,
    SMEProfile,
    LoanApplication,
    FinancialData,
    RMReview,
    Prediction,
    LoanAssessment
)

def create_tables():
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")

if __name__ == "__main__":
    create_tables()