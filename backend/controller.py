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

# plantilla pydantic
class ModelComentario(BaseModel):
    id_omdb: str
    nombre: str
    comment: str
    fecha: str


# buscar peliculas en la api
@app.get("/peliculas/buscar", tags=['Pelis'])
def buscar_peliculas(titulo: str, fecha: str = None):
    return model.buscar_peliculas(titulo, fecha)

@app.get("/peliculas/detalle/{id}", tags=['Pelis'])
def id_pelicula(id: str):
    return model.id_pelicula(id)


# buscar comentarios en la base de datos
@app.get("/comentarios/{id_omdb}", tags=['Comentarios'])
def comentarios_por_pelicula(id_omdb: str):
    return consultas.select_by_id_omdb(id_omdb)

@app.post("/comentarios", tags=['Comentarios'])
def comentario_registro(body: ModelComentario):
    consultas.insert_data([body.id_omdb, body.nombre, body.comment, body.fecha])
    return {'mensaje': 'registro correcto'}