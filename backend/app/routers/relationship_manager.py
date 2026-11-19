from fastapi import APIRouter, Depends
from app.core.security import require_role

router = APIRouter(
    prefix="/relationship-manager",
    tags=["Relationship Manager"]
)


@router.get("/dashboard")
def rm_dashboard(
    current_user=Depends(
        require_role("relationship_manager")
    )
):
    return {
        "message": "Welcome to Relationship Manager dashboard",
        "user_id": current_user.id,
        "role": current_user.role
    }