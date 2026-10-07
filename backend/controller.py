from fastapi import FastAPI
import model

app = FastAPI()

@app.get("/peliculas/buscar", tags=['Pelis'])
def buscar_peliculas(titulo: str, fecha: str = None):
    return model.buscar_peliculas(titulo, fecha)

@app.get("/peliculas/detalle/{id}", tags=['Pelis'])
def id_pelicula(id: str):
    return model.id_pelicula(id)