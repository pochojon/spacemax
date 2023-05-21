
  
var inmuebles = [
    {
        codigo: "spmx1",
        imagen: "img/space domo 2.jpg",
        nombre: "Villa",
        planeta: "Marte",
        cplaneta: "2",
        descripcion: "3 ambientes <br>2 baños <br> Central Termonuclear propia <br>Pantalla Solar"
    },
    {
        codigo: "spmx2",
        imagen: "img/space domo 3.jpg",
        nombre: "Condo",
        planeta: "Venus",
        cplaneta: "8",
        descripcion: "3 ambientes <br>2 baños <br> Central Termonuclear propia "
    },
    {
        codigo: "spmx3",
        imagen: "img/space domo 4.jpg",
        nombre: "Domo",
        planeta: "Saturno",
        cplaneta: "4",
        descripcion: "2 ambientes <br>1 baño <br> Generadores termoeléctrico"
    },
    {
        codigo: "spmx4",
        imagen: "img/space domo 5.jpg",
        nombre: "Domo",
        planeta: "Luna",
        cplaneta: "3",
        descripcion: "3 ambientes <br>1 baño <br>Paneles fotovoltaicos"
    },
    {
        codigo: "spmx5",
        imagen: "img/space domo 6.jpg",
        nombre: "Condo",
        planeta: "Jupiter",
        cplaneta: "9",
        descripcion: "2 ambientes <br>1 baño <br>Pileta regulada por electrolisis <br>Generador termoeléctrico"
    },
    {
        codigo: "spmx6",
        imagen: "img/space domo 7.jpg",
        nombre: "Villa",
        planeta: "Saturno",
        cplaneta: "4",
        descripcion: "6 ambientes <br>4 baños <br>Acumuladores de baterías <br>Atmósfera artificial"
    },
    {
        codigo: "spmx7",
        imagen: "img/space domo 8.jpg",
        nombre: "Villa",
        planeta: "Luna",
        cplaneta: "3",
        descripcion: "6 ambientes <br>4 baños <br>Paneles Solares <br>Atmósfera artificial"
    },
    {
        codigo: "spmx8",
        imagen: "img/space domo 8.jpg",
        nombre: "Domo",
        planeta: "Jupiter",
        cplaneta: "9",
        descripcion: "2 ambientes <br> 1 baño <br> Aumuladores de baterias propio"
    },
    {
        codigo: "spmx9",
        imagen: "img/space domo 10.jpg",
        nombre: "Domo",
        planeta: "Marte",
        cplaneta: "2",
        descripcion: "1 ambiente <br>1 baño <br>Generadores termoeléctrico"
    }
]



let spmxhome=` `

if ( document.getElementById( "propiedades" )) 
        {
         for(var i=0; i<inmuebles.length; i++){

           console.log(inmuebles[i].planeta)

           //if (inmuebles[i].planeta=="Marte")
           //{
             spmxhome+=`
            <article class="article">
            <img src="${inmuebles[i].imagen}" alt="Card image" style="width:100%">
            <h3>${inmuebles[i].nombre}</h3>
            <h2>${inmuebles[i].planeta}</h2>
            <p>${inmuebles[i].descripcion}</p>
            </article>
            `
           //}
         }
 
  document.getElementById("propiedades").innerHTML=spmxhome;
 };

 

 const formcontacto=document.getElementById('formcontacto');
 const inputs=document.querySelectorAll('#formcontacto input');

 const okcampos = 
 {
    firstname : /^[a-zA-Z]{1,30}$/,
    lastname : /^[a-zA-Z]{1,30}$/,
    address : /^[a-zA-Z]{1,30}$/,
    mail :  /^[a-zA-Z0-9@.-_]{1,30}$/,
    anumber : /^\d{1,10}$/,
    

}

 const validarformcontacto = (e) => {
    switch (e.target.name) {
        case "firstname":
           if (okcampos.firstname.test(e.target.value)) { 

            } else { 
                alert("El nombre contiene caracteres incorrectos o bien está vacío ")
            }       
        break;
        case "lastname":
            if (okcampos.lastname.test(e.target.value)) { 

            } else { 
                alert("El apellido contiene caracteres incorrectos o bien está vacío ")
            }       
        break;
        case "address":
            if (okcampos.address.test(e.target.value)) { 

            } else { 
                alert("La calle contiene caracteres incorrectos o bien está vacío ")
            }       
        break;
        case "number":
            if (okcampos.anumber.test(e.target.value)) { 

            } else { 
                alert("El numero de calle contiene caracteres incorrectos o bien está vacío ")
            }       
        break;
        case "mail":
            if (okcampos.mail.test(e.target.value)) { 

            } else { 
                alert("El mail caracteres incorrectos o bien está vacío ")
            }       
        break;

    }       
 };

 inputs.forEach((input) => {
   input.addEventListener('keyup', validarformcontacto);
});



 formcontacto.addEventListener('submit', (e) => {
    e.preventDefault();
 });

 






