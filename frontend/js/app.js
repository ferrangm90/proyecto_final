console.log("javascript cargado");
const urlBase = 'http://127.0.0.1:8000';

// Crea la tabla de resultados
function generarFilasTabla(data) {
    let filas = '';
    data.forEach(pelicula => {
        filas += `
        <tr data-id="${pelicula.imdbID}">
            <td><img src="${pelicula.Poster}" width="50"></td>
            <td>${pelicula.Title}</td>
            <td>${pelicula.Year}</td>
        </tr>
        `;
    });

    return filas;
}

// Muestra los detalles de la peli seleccionada
function pintarDetallePelicula(pelicula) {
    // quito el mensaje y muestro el contenido
    document.getElementById('mensaje').style.display = 'none';
    document.getElementById('contenido').style.display = 'block';

    document.getElementById('detalle-id-omdb').value = pelicula.imdbID;
    document.getElementById('detalle-id-texto').innerText = pelicula.imdbID;
    document.getElementById('detalle-titulo').innerText = pelicula.Title;
    document.getElementById('detalle-year').innerText = pelicula.Year;
    document.getElementById('detalle-genre').innerText = pelicula.Genre;
    document.getElementById('detalle-plot').innerText = pelicula.Plot;
    document.getElementById('detalle-caratula').src = pelicula.Poster;
}

// Muestra los comentarios
function generarHTMLComentarios(listaComentarios) {
    let html = '';
    listaComentarios.forEach(item => {
        html += `
        <div class="card mb-2 p-3">
            <strong>${item.nombre}</strong> 
            <i>${item.fecha}</i>
            <p>${item.comment}</p>
        </div>
        `;
    });
    return html;
}

// Busca pelis segun el titulo y por fecha
function buscarPeliculas() {
    const titulo = document.getElementById('titulo').value;
    const fecha = document.getElementById('fecha').value;

    if (titulo === "") {
        alert("Tienes que escribir el título de una película");
        return;
    }
    // paso la fecha porque lo controla el backend
    let urlBusqueda = `${urlBase}/peliculas/buscar?titulo=${titulo}&fecha=${fecha}`;
    const tbody = document.getElementById('cuerpo-tabla');

    fetch(urlBusqueda)
        .then(response => response.json())
        .then(data => {
            if (data.Response === "False") {
                alert("No se encontraron películas");
                tbody.innerHTML = '';
                return;
            }

            tbody.innerHTML = generarFilasTabla(data.Search);
            // al tener la la lista de pelis ahora se llama a la funcion que captura el clic
            capturarItemTabla();
        })
        .catch(error => console.log("Error al buscar películas: ",error));
}

// Captura el clic en la tabla de resultados
function capturarItemTabla() {
    const tabla = document.getElementById("tabla");

    for (let i = 1; i < tabla.rows.length; i++) {
        tabla.rows[i].onclick = function () {
            // el data-id de la funcion generarFilasTabla
            let idOmdb = this.getAttribute("data-id");
            cargarDetallePelicula(idOmdb);
        };
    }
}

// Llama a mostrar detalles y comentarios de la peli seleccionada
function cargarDetallePelicula(idOmdb) {
    fetch(`${urlBase}/peliculas/detalle/${idOmdb}`)
        .then(response => response.json())
        .then(pelicula => {
            pintarDetallePelicula(pelicula);
            cargarComentarios(pelicula.imdbID);
        })
        .catch(error => console.log("Error al cargar detalles: ",error));
}


// Muestra los comentarios de la peli seleccionada
function cargarComentarios(idOmdb) {
    const contenedor = document.getElementById('lista-comentarios');

    fetch(`${urlBase}/comentarios/${idOmdb}`)
        .then(response => response.json())
        .then(comentarios => {
            if (comentarios.length === 0) {
                contenedor.innerHTML = '<p>No hay comentarios</p>';
                return;
            }

            contenedor.innerHTML = generarHTMLComentarios(comentarios);
        })
        .catch(error => console.log("Error al cargar comentarios: ",error));
}

// Gestiona los comentarios nuevos
function altaComentario() {
    const idOmdb = document.getElementById('detalle-id-omdb').value;
    const nombre = document.getElementById('nombre').value;
    const comentario = document.getElementById('comentario').value;

    if (nombre === "" || comentario === "") {
        alert("Tienes que rellenar tu nombre y el comentario");
        return;
    }

    const fechaHoy = new Date().toISOString().split('T')[0];
    const url = `${urlBase}/comentarios`;

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            id_omdb: idOmdb,
            nombre: nombre,
            comment: comentario,
            fecha: fechaHoy
        })
    })
    .then(response => response.json())
    .then(data => {
        alert("Comentario guardado correctamente");
        limpiarFormularioComentario();
        cargarComentarios(idOmdb);
    })
    .catch(error => console.log("Error al guardar comentario: ",error));
}

// Limpia el formulario de comentario
function limpiarFormularioComentario() {
    document.getElementById('nombre').value = '';
    document.getElementById('comentario').value = '';
}

// Botones de buscar y guardar comentario
let btnBuscar = document.getElementById('btnBuscar');
btnBuscar.addEventListener('click', buscarPeliculas);

let btnGuardarComentario = document.getElementById('btnGuardarComentario');
btnGuardarComentario.addEventListener('click', altaComentario);