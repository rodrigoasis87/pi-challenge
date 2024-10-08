from pydantic import BaseModel, Field
from enum import Enum

# creo variables 

class HairColorEnum(str, Enum):
    black = "black"
    brown = "brown"
    blonde = "blonde"
    red = "red"
    gray = "gray"
    white = "white"
    no_hair = "no hair"

class SkinColorEnum(str, Enum):
    light = "light"
    fair = "fair"
    medium = "medium"
    olive = "olive"
    dark = "dark"

class EyeColorEnum(str, Enum):
    blue = "blue"
    brown = "brown"
    green = "green"
    gray = "gray"
    hazel = "hazel"



class CharacterBase(BaseModel):

    id: int = Field(...)
    name: str = Field(..., min_length=1, max_length=100)
    height: int = Field(..., gt=0)
    mass: int = Field(..., gt=0)
    hair_color: HairColorEnum = Field (...)
    skin_color: SkinColorEnum = Field (...)
    eye_color: EyeColorEnum = Field (...)
    birth_year: int = Field(..., gt=0)



class CharacterCreate(CharacterBase):
    pass

class Character(CharacterBase):
     
    id: int = Field(...)

    class Config:
         orm_mode = True