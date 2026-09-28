var api = "http://127.0.0.1:8000/"
var profesores = []

function renderizarLista(listaProfesores) {
        for (const profesor of listaProfesores) {
                const conProfe = document.createElement("div")
                conProfe.innerHTML = `
                  <h4>${profesor.nombre}<h4>
                  <br>
                  <p>Materia: ${profesor.materia}</p>
                  <p>Aura: ${profesor.aura}</p>
                  <button class="boton" onclick="eliminar(${profesor.id})">
                `

                document.querySelector(".listadoDeProfes").appendChild(conProfe)
        }
}

function cargarProfes() {
        fetch(api + "/listar")
        .then(function (respuesta) { return respuesta.json() })
        .then(function (datos) {
                profesores = datos
                renderizarLista(profesores)
        })
        .catch(function () {
                var mensaje = document.createElement("h1")
                mensaje.textContent = "No se pudo conectar a la API"
        })
}

function agregarProfe() {
        var profesor = {
                nombre: document.getElementById("nombre").value,
                materia: document.getElementById("materia").value,
                aura: Number(document.getElementById("aura").value)
        }

        fetch(api + "/agregar", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(profesor)
        }).then(function () {
                document.querySelector(".aniadidor").reset()
                cargarProfes()
        })
}

function eliminar(id) {
        fetch(api + "/eliminar/" + id, { method: "DELETE" }).then(function() { cargarProfes() })
}

cargarProfes()
