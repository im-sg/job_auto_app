from pydantic import BaseModel
from typing import Optional, List

class ProfileFieldCreate(BaseModel):
    field_name: str
    field_value: str

class ProfileFieldOut(ProfileFieldCreate):
    id: int
    class Config:
        from_attributes = True


class ProfileCreate(BaseModel):
    profile_name: str
    description: Optional[str] = None

class ProfileOut(ProfileCreate):
    id: int
    fields: List[ProfileFieldOut] = []
    class Config:
        from_attributes = True
