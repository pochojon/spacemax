var inmuebles = []
const URL = "https://tpofspacemax.pythonanywhere.com/"
// Realizamos la solicitud GET al servidor para obtener todos los productos
fetch(URL + 'propiedades')
    .then(function (response) {
        if (response.ok) {
            return response.json() // Parseamos la respuesta JSON
        } else {
            throw new Error('Error al obtener las propiedades 1.')
        }
    })
    .then(function (data) {
        inmuebles = data

    })
    .catch(function (error) {
        console.log('Error:', error)
        alert('Error al obtener las propiedades 2.')
    })



console.log(inmuebles)


datosplaneta = " "
var formbusqueda = document.getElementById("formppal");


formbusqueda.addEventListener('submit', function (e) {
    e.preventDefault();

    console.log("hizo click");
    var datos = new FormData(formbusqueda);
    console.log(datos);
    console.log(datos.get('fplaneta'));
    datosplaneta = datos.get('fplaneta');
    datosoperaciontipo = datos.get('foperaciontipo');
    datospropiedadtipo = datos.get('fpropiedadtipo');

    let spmxhome = ` `

    //
    //<button @click="agregarAlPortafolio(propiedad)">&nbsp;&nbsp;<b>+</b>&nbsp;&nbsp;</button>
    //<button @click="restarDelPortafolio(propiedad)">&nbsp;&nbsp;<b>-</b>&nbsp;&nbsp;</button>

    if (document.getElementById("propiedades")) {
        for (var i = 0; i < inmuebles.length; i++) {

            console.log(inmuebles[i].planeta)
            console.log(inmuebles[i].nombre)

            if ((inmuebles[i].planeta == datosplaneta || datosplaneta == "Todos") && (inmuebles[i].operacion == datosoperaciontipo || datosoperaciontipo == "Todos") && (inmuebles[i].nombre == datospropiedadtipo || datospropiedadtipo == "Todos")) {
                spmxhome += `
            <div class="card-propiedad">
                <div class="card-imgprop">
                    <img src="${inmuebles[i].imagen}" alt="Card image" style="width:100%">
                </div>
                <div class="card-bprop">
                 <h2 class="card-tipoprop"> ${inmuebles[i].nombre} <br> Código:${inmuebles[i].codigo}</h2>
                 <p>${inmuebles[i].descripcion}</p>
                 <h3 class="hplaneta">${inmuebles[i].planeta}</h3>
                 <h2 class="hoperacion">${inmuebles[i].operacion}</h2>
 
                </div>
            </div>
            `
            }
        }

        document.getElementById("propiedades").innerHTML = spmxhome;
    };
}
)
