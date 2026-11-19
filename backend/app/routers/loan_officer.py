from fastapi import APIRouter, Depends
from app.core.security import require_role

router = APIRouter(
    prefix="/loan-officer",
    tags=["Loan Officer"]
)


@router.get("/dashboard")
def loan_officer_dashboard(
    current_user=Depends(
        require_role("loan_officer")
    )
):
    return {
        "message": "Welcome to Loan Officer dashboard",
        "user_id": current_user.id,
        "role": current_user.role
    }