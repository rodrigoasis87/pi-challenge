from datetime import date
from pydantic import BaseModel, Field
from enum import Enum
from dateutil import parser

# creo variables 

class HairColorEnum(str, Enum):
    black = "black"
    brown = "brown"
    blonde = "blonde"
    red = "red"
    gray = "gray"
    white = "white"

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

    name: str = Field(..., min_length=1, max_length=100)
    height: int = Field(..., gt=0)
    mass: int = Field(..., gt=0)
    hair_color: HairColorEnum = Field (...)
    skin_color: SkinColorEnum = Field (...)
    eye_color: EyeColorEnum = Field (...)
    birth_year: date = Field(..., gt=0)

    def get_birth_year(self):
            return parser.parse(self.birth_year).year


class CharacterCreate(CharacterBase):
    pass

class Character(CharacterBase):
     
    id: int = Field(...)

    class Config:
         orm_mode = True