from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud
from ..database import SessionLocal, init_db

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close_all()

@router.get('/getAll', response_model=list[schemas.Character])
def get_all_characters(db: Session = Depends(get_db)):
    characters = crud.get_all_characters(db)
    return characters

@router.get('/get/{id}', response_model=schemas.Character)
def get_character(id: int, db: Session = Depends(get_db)):
    character = crud.get_character_by_id(db, id)
    if character is None:
        raise HTTPException(status_code=404, detail="Character not found")
    return character


@router.post('/add', response_model=schemas.Character)
def add_character(character: schemas.CharacterCreate, db: Session = Depends(get_db)):
    db_character = crud.get_character_by_id(db, character_id=character.id)
    if db_character:
        raise HTTPException(status_code=404, detail="Character already exists")
    return crud.create_character(db, character)

@router.delete('/delete/{id}', response_model=schemas.Character)
def delete_character(id: int, db: Session = Depends(get_db)):
    character = crud.delete_character(db, id)
    if character is None:
        raise HTTPException(status_code=404, detail="Character not found")
    return character