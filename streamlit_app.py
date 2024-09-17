import streamlit as st
import requests
from app.schemas import HairColorEnum, SkinColorEnum, EyeColorEnum  # Importa las enumeraciones

# URL base de tu API de FastAPI
API_URL = "http://127.0.0.1:8000/character"

st.title("Administración de Characters")

# Opciones del menú
option = st.selectbox(
    "Selecciona una acción",
    ("Obtener todos los characters", "Obtener character por ID", "Crear character", "Eliminar character")
)

# Obtener todos los characters
if option == "Obtener todos los characters":
    st.subheader("Lista de todos los characters")
    
    # Hacer la solicitud GET a la API
    response = requests.get(f"{API_URL}/getAll")
    
    if response.status_code == 200:
        characters = response.json()
        st.write(characters)
    else:
        st.error("Error al obtener los characters")

# Obtener un character por ID
elif option == "Obtener character por ID":
    st.subheader("Obtener character por ID")
    
    character_id = st.number_input("Ingresa el ID del character", min_value=1, step=1)
    
    if st.button("Buscar"):
        response = requests.get(f"{API_URL}/get/{character_id}")
        
        if response.status_code == 200:
            character = response.json()
            st.write(character)
        else:
            st.error(f"Error al obtener el character con ID {character_id}")

# Crear un nuevo character
elif option == "Crear character":
    st.subheader("Crear un nuevo character")
    
    # Campos de entrada de datos del personaje
    id = st.number_input("Id del character", min_value=0, step=1)
    name = st.text_input("Nombre del character")
    height = st.number_input("Altura del character (en cm)", min_value=0, step=1)
    mass = st.number_input("Peso del character (en kg)", min_value=0, step=1)
    
    # Opciones desplegables para las enumeraciones, obtenidas dinámicamente desde los Enum
    hair_color = st.selectbox(
        "Color de cabello",
        options=[hair.value for hair in HairColorEnum]  # Extrae las opciones desde HairColorEnum
    )
    
    skin_color = st.selectbox(
        "Color de piel",
        options=[skin.value for skin in SkinColorEnum]  # Extrae las opciones desde SkinColorEnum
    )
    
    eye_color = st.selectbox(
        "Color de ojos",
        options=[eye.value for eye in EyeColorEnum]  # Extrae las opciones desde EyeColorEnum
    )
    
    birth_year = st.number_input("Año de nacimiento (ej. 1980)", min_value=0, step=1)
    
    if st.button("Crear"):
        # Estructura los datos en formato JSON para la API
        character_data = {
            "id": id,
            "name": name,
            "height": height,
            "mass": mass,
            "hair_color": hair_color,
            "skin_color": skin_color,
            "eye_color": eye_color,
            "birth_year": birth_year
        }
        
        # Realiza la solicitud POST para crear el personaje
        response = requests.post(f"{API_URL}/add", json=character_data)
        
        if response.status_code == 200:
            st.success("Character creado exitosamente")
        else:
            st.error("Error al crear el character")

# Eliminar un character
elif option == "Eliminar character":
    st.subheader("Eliminar un character")
    
    character_id = st.number_input("Ingresa el ID del character a eliminar", min_value=1, step=1)
    
    if st.button("Eliminar"):
        response = requests.delete(f"{API_URL}/delete/{character_id}")
        
        if response.status_code == 200:
            st.success(f"Character con ID {character_id} eliminado exitosamente")
        else:
            st.error(f"Error al eliminar el character con ID {character_id}")