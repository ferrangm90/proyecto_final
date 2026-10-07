import requests as consulta

KEY = "4c927440"
BASE_URL = "http://www.omdbapi.com/"

def buscar_peliculas(titulo: str, fecha: str = None):
    """
    Busca peliculas por nombre y si se proporciona por fecha tambien
    """
    try:
        url = f"{BASE_URL}?apikey={KEY}&s={titulo}"
        # si se pone el año se añade a la url
        if fecha:
            url += f"&y={fecha}"
        respuesta = consulta.get(url)
        return respuesta.json()
    except Exception as error:
        print(error)
        return {"Error": "Error de conexión con omdb"}

def id_pelicula(id: str):
    """
    Consulta los detalles de una pelicula por la id
    """
    try:
        url = f"{BASE_URL}?apikey={KEY}&i={id}&plot=full"
        respuesta = consulta.get(url)
        return respuesta.json()
    except Exception as error:
        print(error)
        return {"Error": "Error de conexion con omdb"}