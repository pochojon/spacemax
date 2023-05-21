 
var inmuebles = [
    {
        codigo: "spmx1",
        imagen: "img/spaceprop-2.jpg",
        nombre: "Condo",
        planeta: "Marte",
        cplaneta: "2",
        operacion: "Venta",
        descripcion: "3 ambientes <br>2 baños <br> Central Termonuclear propia <br>Pantalla Solar"
    },
    {
        codigo: "spmx2",
        imagen: "img/spaceprop-3.jpg",
        nombre: "Condo",
        planeta: "Venus",
        cplaneta: "8",
        operacion: "Venta",
        descripcion: "3 ambientes <br>2 baños <br> Central Termonuclear propia "
    },
    {
        codigo: "spmx3",
        imagen: "img/spaceprop-4.jpg",
        nombre: "Domo",
        planeta: "Saturno",
        cplaneta: "4",
        operacion: "Alquiler",
        descripcion: "2 ambientes <br>1 baño <br> Generadores termoeléctrico"
    },
    {
        codigo: "spmx4",
        imagen: "img/spaceprop-5.jpg",
        nombre: "Domo",
        planeta: "Luna",
        cplaneta: "3",
        operacion: "Alquiler",
        descripcion: "3 ambientes <br>1 baño <br>Paneles fotovoltaicos"
    },
    {
        codigo: "spmx5",
        imagen: "img/spaceprop-6.jpg",
        nombre: "Condo",
        planeta: "Jupiter",
        cplaneta: "9",
        operacion: "Alquiler",
        descripcion: "2 ambientes <br>1 baño <br>Pileta regulada por electrolisis <br>Generador termoeléctrico"
    },
    {
        codigo: "spmx6",
        imagen: "img/spaceprop-7.jpg",
        nombre: "Villa",
        planeta: "Saturno",
        cplaneta: "4",
        operacion: "Venta",
        descripcion: "6 ambientes <br>4 baños <br>Acumuladores de baterías <br>Atmósfera artificial"
    },
    {
        codigo: "spmx7",
        imagen: "img/spaceprop-8.jpg",
        nombre: "Villa",
        planeta: "Luna",
        cplaneta: "3",
        operacion: "Venta",
        descripcion: "6 ambientes <br>4 baños <br>Paneles Solares <br>Atmósfera artificial"
    },
    {
        codigo: "spmx8",
        imagen: "img/spaceprop-13.jpg",
        nombre: "Domo",
        planeta: "Jupiter",
        cplaneta: "9",
        operacion: "Alquiler",
        descripcion: "2 ambientes <br> 1 baño <br> Aumuladores de baterias propio"
    },
    {
        codigo: "spmx9",
        imagen: "img/spaceprop-10.jpg",
        nombre: "Domo",
        planeta: "Marte",
        cplaneta: "2",
        operacion: "Venta",
        descripcion: "1 ambiente <br>1 baño <br>Generadores termoeléctrico"
    },

    {
        codigo: "spmx10",
        imagen: "img/spaceprop-11.jpg",
        nombre: "Domo",
        planeta: "Luna",
        cplaneta: "2",
        operacion: "Venta",
        descripcion: "1 ambiente <br>1 baño <br>Generadores termoeléctrico"
    },
    {
        codigo: "spmx11",
        imagen: "img/spaceprop-12.jpg",
        nombre: "Villa",
        planeta: "Jupiter",
        cplaneta: "2",
        operacion: "Venta",
        descripcion: "5 ambiente <br>2 baño <br>Protectores solares"
    },
    {
        codigo: "spmx12",
        imagen: "img/spaceprop-14.jpg",
        nombre: "Domo",
        planeta: "Venus",
        cplaneta: "2",
        operacion: "Venta",
        descripcion: "1 ambiente <br>1 baño <br>Estructura tipo Loft"
    },
    {
        codigo: "spmx13",
        imagen: "img/spaceprop-15.jpg",
        nombre: "Condo",
        planeta: "Venus",
        cplaneta: "2",
        operacion: "Venta",
        descripcion: "3 ambiente <br>2 baño <br>Acumuladores de energia propios"
    },
    {
        codigo: "spmx14",
        imagen: "img/spaceprop-16.jpg",
        nombre: "Condo",
        planeta: "Marte",
        cplaneta: "2",
        operacion: "Alquiler",
        descripcion: "2 ambiente <br>2 baño <br>Vistas 360 grados en todos los ambientes"
    },
    {
        codigo: "spmx16",
        imagen: "img/spaceprop-17.jpg",
        nombre: "Domo",
        planeta: "Luna",
        cplaneta: "2",
        operacion: "Venta",
        descripcion: "1 ambiente <br>1 baños <br>Reserva natural interna. Paneles solares propios"
    },
    {
        codigo: "spmx17",
        imagen: "img/spaceprop-18.jpg",
        nombre: "Condo",
        planeta: "Marte",
        cplaneta: "2",
        operacion: "Alquiler",
        descripcion: "4 ambiente <br>2 baños <br>Dock vehiculo incorporado"
    },
    {
        codigo: "spmx18",
        imagen: "img/spaceprop-19.jpg",
        nombre: "Domo",
        planeta: "Jupiter",
        cplaneta: "2",
        operacion: "Venta",
        descripcion: "3 ambiente <br>3 baños <br>Tanquies reservorios de agua propia"
    },
    {
        codigo: "spmx11",
        imagen: "img/spaceprop-20.jpg",
        nombre: "Villa",
        planeta: "Venusr",
        cplaneta: "2",
        operacion: "Venta",
        descripcion: "4 ambiente <br>3 baños <br>Atmósfera articial"
    },
    {
        codigo: "spmx12",
        imagen: "img/spaceprop-21.jpg",
        nombre: "Condo",
        planeta: "Marte",
        cplaneta: "2",
        operacion: "Venta",
        descripcion: "2 ambiente <br>1 baño <br>Protectores solares"
    }









]
datosplaneta=" "
var formbusqueda = document.getElementById("formppal");

    
formbusqueda.addEventListener('submit', function(e){
    e.preventDefault();

    console.log("hizo click");
    var datos = new FormData(formbusqueda);
    console.log(datos);
    console.log(datos.get('fplaneta'));
    datosplaneta=datos.get('fplaneta');
    datosoperaciontipo=datos.get('foperaciontipo');
    datospropiedadtipo=datos.get('fpropiedadtipo');

    let spmxhome=` `

    if ( document.getElementById( "propiedades" )) 
        {
         for(var i=0; i<inmuebles.length; i++){

           console.log(inmuebles[i].planeta)
           console.log(inmuebles[i].nombre) 

           if ((inmuebles[i].planeta==datosplaneta ||datosplaneta=="Todos" ) && (inmuebles[i].operacion==datosoperaciontipo || datosoperaciontipo=="Todos" ) && (inmuebles[i].nombre==datospropiedadtipo || datospropiedadtipo=="Todos") )

           {
             spmxhome+=`
            <div class="card-propiedad">
                <div class="card-imgprop">
                    <img src="${inmuebles[i].imagen}" alt="Card image" style="width:100%">
                </div>
                <div class="card-bprop">
                 <h2 class="card-tipoprop">${inmuebles[i].nombre}</h2>
                 <p>${inmuebles[i].descripcion}</p>
                 <h3 class="hplaneta">${inmuebles[i].planeta}</h3>
                 <h2 class="hoperacion">${inmuebles[i].operacion}</h2>
                </div>
            </div>
            `
           }
         }
 
      document.getElementById("propiedades").innerHTML=spmxhome;
    };





       
} 
)


let spmxhome=` `

    if ( document.getElementById( "propiedades" )) 
        {
         for(var i=0; i<inmuebles.length; i++){

           console.log(inmuebles[i].planeta)
            

           //if (inmuebles[i].planeta=="Marte")
           //{
             spmxhome+=`
            <div class="card-propiedad">
                <div class="card-imgprop">
                    <img src="${inmuebles[i].imagen}" alt="Card image" style="width:100%">
                </div>
                <div class="card-bprop">
                 <h2 class="card-tipoprop">${inmuebles[i].nombre}</h2>
                 <p>${inmuebles[i].descripcion}</p>
                 <h3 class="hplaneta">${inmuebles[i].planeta}</h3>
                 <h2 class="hoperacion">${inmuebles[i].operacion}</h2>
                </div>
            </div>
            `
           //}
         }
 
      document.getElementById("propiedades").innerHTML=spmxhome;
    };


 
    

 






