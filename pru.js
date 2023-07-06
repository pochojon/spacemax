const url = 'https://tu-domino-en-pythonanywhere.com/productos'
const data = {
    codigo: 2,
    tipo: 'CONDO',
    planeta: 'MARTE',
    descripcion: '3 ambientes 2 baños Central Termonuclear propia',
    cantidad: 1,
    precio: 12500
}

fetch(url, {
    method: 'POST', headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
})
    .then(response => {
        if (response.ok) {
            console.log('Propiedad agregado correctamente')
        } else {
            console.log('Error al agregar la propiedad')
        }
    })
    .catch(error => {
        console.error('Error de conexión:', error)
    })

    