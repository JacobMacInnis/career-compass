from fastapi import APIRouter
from pydantic import BaseModel
from src.db.database import SessionLocal
from src.db.models import UserEntry
from src.schemas.user_profile import UserProfileWithEmployment


router = APIRouter()

@router.post("/submit")
def submit(user: UserProfileWithEmployment):
    try:
        db = SessionLocal()
        new_entry = UserEntry(**user.dict())
        db.add(new_entry)
        db.commit()
        db.refresh(new_entry)
        return {"status": "success", "entry_id": new_entry.id}
    except Exception as e:
        db.rollback()
        return {"status": "error", "message": str(e)}
    finally:
        db.close()
