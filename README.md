# Proyecto Final Ferran Giménez

## Aplicación web de búsqueda de películas y comentarios con FastAPI y SQLite

He aprovechado este proyecto de buscador de películas para hacer tributo a la mítica página de películas "Películas Yonkis". Permite realizar búsquedas de películas consumiendo la API externa de OMDb, visualizar los detalles completos de cada título y gestionar comentarios guardados en una base de datos local SQLite.

## Funcionalidades cumplidas en la aplicación

1. **Buscar películas:** Búsqueda dinámica por título y año opcional mediante la API de OMDb.
2. **Vista de detalles:** Visualización ampliada de la película seleccionada al hacer clic en los resultados de la tabla.
3. **Gestión de comentarios:**
   - Consulta de comentarios guardados para cada película concreta.
   - Formulario para publicar nuevos comentarios que se almacenan automáticamente en la base de datos SQLite con la fecha actual.

## Estructura del proyecto

- **Frontend:** HTML5, CSS3 con Bootstrap y JavaScript.
- **Backend:** Framework FastAPI en Python siguiendo el patrón MVC.
- **Base de Datos:** SQLite3.

## Guía de instalación y ejecución

### 1. Crear el entorno virtual

Abre tu terminal en la carpeta principal del proyecto y crea el entorno virtual:

- En **Windows**:
  ```bash
  py -m venv entorno
  ```
- En **Mac / Linux**:
  ```bash
  python3 -m venv entorno
  ```

### 2. Activar el entorno virtual

- En **Windows**:
  ```bash
  .\entorno\Scripts\activate
  ```
- En **Mac / Linux**:
  ```bash
  source entorno/bin/activate
  ```

### 3. Instalar las dependencias

Con el entorno activado, ejecuta el siguiente comando:

```bash
pip install -r backend/requirements.txt
```

### 4. Iniciar el servidor backend

Accede a la carpeta del backend e inicia el servidor con Uvicorn:

```bash
cd backend
fastapi dev main.py
```

El servidor estará corriendo en: `http://127.0.0.1:8000`

### 5. Abrir la aplicación

Abre el archivo `frontend/index.html` en tu navegador web.