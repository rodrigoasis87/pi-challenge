# A-PI Challenge

## Estado Actual

¡Bienvenid@s! Ya se puede desplegar la api en un entorno local (`venv`) en caso de necesitarlo (el despliegue con Docker continúa en configuración). En esta API Characters se encontrarán: 

1. **API Documentada y Estructurada**  
   - Arquitectura limpia con **FastAPI**, proporcionando una API rápida y eficiente, con documentación automática. 
   - Documentación Swagger: [http://localhost:8000/docs](http://localhost:8000/docs)
   - La documentación proporciona uno de los entornos donde puede testear los endpoints.

2. **Tres de los métodos CRUD**  
   - Endpoints para Crear, Leer y Eliminar personajes en la base de datos.

3. **Base de Datos Integrada**  
   - Usa **SQLite** y el archivo `characters.db` incluido. No requiere configuración adicional.

4. **Complemento Back Office**  
   - GUI realizado en **Streamlit** para realizar las operaciones CRUD. 

5. **Fácil Configuración**  
   - Soporte para correr con **Docker** (en progreso) o con entorno virtual (`venv`).

6. **Colección de Postman Incluida**  
   - Colección **Postman** con los endpoints creados (`PI-challenge.postman_collection.json`).

7. **Buenas Prácticas**  
   - Validaciones con **Pydantic**, arquitectura escalable y modular con **routers** en FastAPI.


## Instrucciones para Ejecutar el Proyecto

### Clonar el repositorio

1. Antes de comenzar, es fundamental clonar el repositorio:

    - HTTPS
    `git clone https://github.com/rodrigoasis87/pi-challenge.git`
    - SSH
    `git clone git@github.com:rodrigoasis87/pi-challenge.git`
    - Ir al repositorio
    `cd pi-challenge`

### Ejecutar con Docker (en progreso)

1. **Asegúrate de tener Docker y Docker Compose instalados**

2. **Construye y levanta los contenedores con Docker Compose:**

    `docker-compose up --build`

### Ejecutar con ambiente virtual (Alternativa)

1. **Asegúrate de tener Python y pip instalados**
    `python -m venv venv`
    `source venv/bin/activate  # Linux/MacOS`
    `venv\Scripts\activate     # Windows`

2. **Instalar dependencias**
    `pip install -r requirements.txt`

3. **Correr la API**
    `uvicorn app.main:app --reload`

4. **Correr el panel de streamlit**
    `streamlit run streamlit_app.py`

### Base de datos
- El archivo `characters.db` ya está incluido en el proyecto, no se requieren configuraciones adicionales para la base de datos.