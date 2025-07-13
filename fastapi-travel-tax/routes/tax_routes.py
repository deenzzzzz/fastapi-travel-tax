# ...existing code...
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import List

router = APIRouter()

# Dummy in-memory data for demonstration
users_db = {}
provinces_db = [
    {"id": 1, "name": "Bangkok", "is_secondary": False},
    {"id": 2, "name": "Chiang Rai", "is_secondary": True},
    {"id": 3, "name": "Nan", "is_secondary": True},
]
tax_reductions_db = [
    {"province_id": 1, "amount": 1000},
    {"province_id": 2, "amount": 2000},
    {"province_id": 3, "amount": 2500},
]

class UserCreate(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    username: str
    is_active: bool

class ProvinceOut(BaseModel):
    id: int
    name: str
    is_secondary: bool

class TaxReductionOut(BaseModel):
    province_id: int
    amount: int

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

@router.post("/register", response_model=UserOut)
def register(user: UserCreate):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Username already registered")
    users_db[user.username] = {"username": user.username, "password": user.password, "is_active": True}
    return {"username": user.username, "is_active": True}

@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = users_db.get(form_data.username)
    if not user or user["password"] != form_data.password:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    return {"access_token": user["username"], "token_type": "bearer"}

@router.get("/provinces", response_model=List[ProvinceOut])
def get_provinces():
    return provinces_db

@router.get("/tax-reductions", response_model=List[TaxReductionOut])
def get_tax_reductions():
    return tax_reductions_db

@router.get("/tax-reductions/secondary", response_model=List[TaxReductionOut])
def get_secondary_tax_reductions():
    secondary_ids = [p["id"] for p in provinces_db if p["is_secondary"]]
    return [tr for tr in tax_reductions_db if tr["province_id"] in secondary_ids]
# ...existing code...
