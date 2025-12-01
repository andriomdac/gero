from fastapi import HTTPException
from sqlalchemy.orm import Session

def get_object_or_404(model, object_id: int, db: Session, object_name: str = "Object"):
    obj = db.query(model).filter(model.id == object_id).first()
    if not obj:
        raise HTTPException(404, f"{object_name} not found")
    return obj
