<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Agregar producto</title>
</head>

<body>
    <h1>Agregar Producto al Inventario</h1>
    <form id="formulario">
        <label for="codigo">Código:</label>
        <input type="text" id="codigo" name="codigo" required><br>

        <label for="descripcion">Descripción:</label>
        <input type="text" id="descripcion" name="descripcion" required><br>

        <label for="cantidad">Cantidad:</label>
        <input type="number" id="cantidad" name="cantidad" required><br>

        <label for="precio">Precio:</label>
        <input type="number" step="0.01" id="precio" name="precio" required><br>

        <button type="submit">Agregar Producto</button>
    </form>

    <script>
        // Capturamos el evento de envío del formulario
        document.getElementById('formulario').addEventListener('submit', function (event) {
            event.preventDefault() // Evitamos que se recargue la página

            // Obtenemos los valores del formulario
var codigo = document.getElementById('codigo').value
            var descripcion = document.getElementById('descripcion').value
            var cantidad = document.getElementById('cantidad').value
            var precio = document.getElementById('precio').value

            // Creamos un objeto con los datos del producto
            var producto = {
                codigo: codigo,
                descripcion: descripcion,
                cantidad: cantidad,
                precio: precio
            }
            console.log(producto)
            // Realizamos la solicitud POST al servidor
            url = 'https://xxxxxx.pythonanywhere.com/productos'
            fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(producto)
            })
                .then(function (response) {
                    if (response.ok) {
                        return response.json() // Parseamos la respuesta JSON
                    } else {
                        throw new Error('Error al agregar el producto.')
                    }
                })
                .then(function (data) {
                    alert('Producto agregado correctamente.')
                })
                .catch(function (error) {
                    console.log('Error:', error)
                    alert('Error al agregar el producto.')
                })
            })
    </script>
</body>

</html>
