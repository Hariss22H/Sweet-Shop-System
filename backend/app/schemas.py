from pydantic import BaseModel


class SweetCreate(BaseModel):
    name: str
    category: str
    price: float
    quantity: int


class SweetResponse(SweetCreate):
    id: int

    class Config:
        from_attributes = True
