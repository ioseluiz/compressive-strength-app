from pydantic import BaseModel

class MixBase(BaseModel):
    name: str
    compressive_strength: int
    design_age: int

class MixCreate(MixBase):
    pass

class Mix(MixBase):
    int: int

    class Config:
        orm_mode = True