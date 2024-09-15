from sqlalchemy.orm import Session
from . import models, schemas

def get_all_characters(db: Session):
    return db.query(models.Character).all()

def get_character_by_id(db: Session, character_id: int):
    return db.query(models.Character).filter(models.Character.id == character_id).first()

def create_character(db: Session, character: schemas.CharacterCreate):
    db_character = models.Character(**character.model_dump())
    db.add(db_character)
    db.commit()
    db.refresh(db_character)
    return db_character

def delete_character(db: Session, character_id: int):
    character = db.query(models.Character).filter(models.Character.id == character_id).first()
    if character:
        db.delete(character)
        db.commit()
        return character
    return None