from fastapi import APIRouter, Depends
from app.core.security import require_role

router = APIRouter(
    prefix="/sme",
    tags=["SME Applicant"]
)


@router.get("/dashboard")
def sme_dashboard(
    current_user=Depends(require_role("sme_applicant"))
):
    return {
        "message": "Welcome to SME dashboard",
        "user_id": current_user.id,
        "role": current_user.role
    }