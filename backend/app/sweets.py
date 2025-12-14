from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import Sweet
from app.dependencies import admin_required
from app.schemas import SweetCreate, SweetResponse


router = APIRouter(prefix="/api/sweets", tags=["Sweets"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=SweetResponse, status_code=status.HTTP_201_CREATED)
def add_sweet(sweet: SweetCreate, db: Session = Depends(get_db)):
    new_sweet = Sweet(**sweet.dict())
    db.add(new_sweet)
    db.commit()
    db.refresh(new_sweet)
    return new_sweet



@router.get("/")
def get_sweets(db: Session = Depends(get_db)):
    return db.query(Sweet).all()


@router.get("/search")
def search_sweets(name: str = None, category: str = None, db: Session = Depends(get_db)):
    query = db.query(Sweet)
    if name:
        query = query.filter(Sweet.name.contains(name))
    if category:
        query = query.filter(Sweet.category.contains(category))
    return query.all()




@router.post("/{sweet_id}/purchase")
def purchase_sweet(sweet_id: int, quantity: int = 1, db: Session = Depends(get_db)):
    sweet = db.query(Sweet).filter(Sweet.id == sweet_id).first()
    if not sweet:
        raise HTTPException(status_code=404, detail="Sweet not found")

    if sweet.quantity < quantity:
        raise HTTPException(status_code=400, detail="Not enough stock")

    sweet.quantity -= quantity
    db.commit()
    return {"message": "Purchase successful", "remaining": sweet.quantity}


@router.post("/{sweet_id}/restock")
def restock_sweet(
    sweet_id: int,
    quantity: int,
    db: Session = Depends(get_db)
    
):
    sweet = db.query(Sweet).filter(Sweet.id == sweet_id).first()
    if not sweet:
        raise HTTPException(status_code=404, detail="Sweet not found")

    sweet.quantity += quantity
    db.commit()
    return {"message": "Restocked successfully", "total": sweet.quantity}
