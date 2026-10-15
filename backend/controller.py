from fastapi import FastAPI
from pydantic import BaseModel
import model
import consultas
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # Permite cualquier origen (dominio)
    allow_credentials=False,  # ¡ATENCIÓN! Debe ser False si usas "*" en origins
    allow_methods=["*"],      # Permite todos los métodos HTTP (GET, POST, PUT, etc.)
    allow_headers=["*"],      # Permite todas las cabeceras HTTP
)

# plantillas pydantic
class ModelComentario(BaseModel):
    id_omdb: str
    nombre: str
    comment: str
    fecha: str

class ModelCalificacion(BaseModel):
    id_omdb: str
    nombre: str
    calificacion: int
    fecha: str

# API
# buscar peliculas en la api
@app.get("/peliculas/buscar", tags=['Pelis'])
def buscar_peliculas(titulo: str, fecha: str = None):
    return model.buscar_peliculas(titulo, fecha)

@app.get("/peliculas/detalle/{id}", tags=['Pelis'])
def id_pelicula(id: str):
    return model.id_pelicula(id)

# COMENTARIOS
# buscar comentarios en la base de datos
@app.get("/comentarios/{id_omdb}", tags=['Comentarios'])
def comentarios_por_pelicula(id_omdb: str):
    return consultas.select_id_omdb(id_omdb)

# guardar comentario en la base de datos
@app.post("/comentarios", tags=['Comentarios'])
def comentario_registro(body: ModelComentario):
    consultas.insert_data([body.id_omdb, body.nombre, body.comment, body.fecha])
    return {'mensaje': 'registro correcto'}

# CALIFICACIONES
# buscar calificaciones en la base de datos
@app.get("/calificaciones/{id_omdb}", tags=['Calificaciones'])
def obtener_promedio_calificacion(id_omdb: str):
    lista_calificaciones = consultas.select_calificaciones_id_omdb(id_omdb)
    # devolver el promedio
    return consultas.calcular_promedio(lista_calificaciones)

# guardar calificacion en la base de datos
@app.post("/calificaciones", tags=['Calificaciones'])
def guardar_calificacion(body: ModelCalificacion):
    consultas.insert_calificacion([body.id_omdb, body.nombre, body.calificacion, body.fecha])
    return {'mensaje': 'calificacion registrada correctamente'}