from fastapi import FastAPI
from .database import init_db
from .routers import character

app = FastAPI()

# Inicializa la base de datos
init_db()

# Incluye las rutas de character
app.include_router(character.router, prefix='/character')

@app.get('/')
async def root():
    return {"message": "Character API"}