
from fastapi import FastAPI

from app.routers.auth import router as auth_router
from app.routers.sme import router as sme_router
from app.routers.relationship_manager import (
    router as rm_router
)
from app.routers.loan_officer import (
    router as loan_officer_router
)


app = FastAPI(
    title="SME Loan Default Risk Prediction System",
    description="Backend API for SME loan applications and default risk assessment",
    version="1.0.0"
)


# Register API routers
app.include_router(auth_router)
app.include_router(sme_router)
app.include_router(rm_router)
app.include_router(loan_officer_router)


@app.get("/")
def root():
    return {
        "message": "SME Loan Risk Prediction API is running"
    }
