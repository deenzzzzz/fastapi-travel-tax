# ...existing code...
from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    is_active: bool

class ProvinceOut(BaseModel):
    id: int
    name: str
    is_secondary: bool

class TaxReductionOut(BaseModel):
    province_id: int
    amount: int
# ...existing code...
