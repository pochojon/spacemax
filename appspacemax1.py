# La clase Propiedad instanciará objetos propiedades que serán almacenadas dentro de un catalogo de propiedades
class Propiedad:
    # Definimos el constructor e inicializamos los atributos de instancia
    def __init__(self, codigo,tipo, planeta, descripcion, cantidad, precio):
        self.codigo = codigo           # Código 
        self.tipo = tipo               # Tipo 
        self.planeta = planeta         # Planeta
        self.descripcion = descripcion # Descripción
        self.cantidad = cantidad       # Cantidad disponible (stock)
        self.precio = precio           # Precio 

    # Este método permite modificar un producto.
    def modificar(self, nuevo_tipo, nuevo_planeta ,nueva_descripcion, nueva_cantidad, nuevo_precio):
        self.tipo = nuevo_tipo                # Tipo 
        self.planeta = nuevo_planeta          # Planeta
        self.descripcion = nueva_descripcion  # Modifica la descripción
        self.cantidad = nueva_cantidad        # Modifica la cantidad
        self.precio = nuevo_precio            # Modifica el precio
        
class Catalogo:
    # Definimos el constructor e inicializamos los atributos de instancia
    def __init__(self):
        self.propiedades = []  # Lista de propiedades dentro del catalogo de propiedades (variable de clase)

    # Este método permite crear objetos de la clase "Propiedad" y agregarlos al catalogo
    def agregar_propiedad(self, codigo,tipo, planeta,descripcion, cantidad, precio):
        nueva_propiedad = Propiedad(codigo,tipo, planeta, descripcion, cantidad, precio)
        self.propiedades.append(nueva_propiedad)  # Agrega un nueva propiedad a la lista de propiedades

    # Este método permite consultar datos de las propiedades que están en el catalogo de propiedades
    # Devuelve la propiedad correspondiente al código proporcionado o False si no existe.
    def consultar_propiedad(self, codigo):
        for propiedad in self.propiedades:
            if propiedad.codigo == codigo:
                return propiedad # Retorna un objeto propiedad
        return False

# Utiliza el método consultar_propiedad del catalogo de propioedades para modificar la propiedad.
    def modificar_propiedad(self, codigo, nuevo_tipo, nuevo_planeta,nueva_descripcion, nueva_cantidad, nuevo_precio):
        propiedad = self.consultar_propiedad(codigo)
        if propiedad:
            propiedad.modificar(nuevo_tipo, nuevo_planeta,nueva_descripcion, nueva_cantidad, nuevo_precio)

    # Este método elimina la propiedad indicado por codigo de la lista mantenida en el catalogo de propiedades
    def eliminar_propiedad(self, codigo):
        eliminar = False
        for propiedad in self.propiedades:
            if propiedad.codigo == codigo:
                eliminar = True
                propiedad_eliminar = propiedad       
        if eliminar == True:
            self.propiedades.remove(propiedad_eliminar)
            print(f'Producto {codigo} eliminado.')
        else:
            print(f'Producto {codigo} no encontrado.')

    # Este método imprime en la terminal una lista con los datos de las propiedades que figuran en el catalogo de proopiedades
    def listar_propiedades(self):
        print("-"*50)
        print("Lista de propiedades en el catalogo de propiedades:")
        print("Código\tTipo\tPlaneta\tDescripción\tCant\tPrecio")
        for propiedad in self.propiedades:
            print(f'{propiedad.codigo}\t{propiedad.tipo}\t{propiedad.planeta}\t{propiedad.descripcion}\t{propiedad.cantidad}\t{propiedad.precio}')
        print("-"*50)


# El inversor elegirá propiedades del catalogo de propiedades y las irá colocalndo o quitándolas de su portafolio


class Portafolio:
    # Definimos el constructor e inicializamos los atributos de instancia
    def __init__(self):
        self.selecciones = []  # Lista de selecciones en el portafolio (variable de clase)

    # Este método permite agregar propiedades del catalogo al portafolio del inversor
    def agregar(self, codigo, cantidad, catalogo):
        # Nos aseguramos que la propiedad se encuente en el catalogo
        propiedad = catalogo.consultar_propiedad(codigo)
        if propiedad is False: 
            print("El producto no existe.")
            return False

        # Verificamos que la cantidad en stock sea suficiente
        if propiedad.cantidad < cantidad:
            print("Cantidad en stock insuficiente.")
            return False

        # Si existe y hay stock, vemos si ya existe en el carrito.
        for seleccion in self.selecciones:
            if seleccion.codigo == codigo:
                seleccion.cantidad += cantidad
                # Actualizamos la cantidad en el catalogo
                propiedad = catalogo.consultar_propiedad(codigo)
                propiedad.modificar(propiedad.tipo, propiedad.planeta,propiedad.descripcion, propiedad.cantidad - cantidad, propiedad.precio)
                return True

        # Si no existe en el portafolio, lo agregamos como un nueva seleccion .
        nuevo_seleccion = Propiedad(codigo, propiedad.tipo, propiedad.planeta, propiedad.descripcion, cantidad, propiedad.precio)
        self.selecciones.append(nuevo_seleccion)
        # Actualizamos la cantidad en el catalogo
        propiedad = catalogo.consultar_propiedad(codigo)
        propiedad.modificar(propiedad.tipo, propiedad.planeta,propiedad.descripcion, propiedad.cantidad - cantidad, propiedad.precio)
        return True


    # Este método quita unidades de una propiedad del portafolio, o lo elimina.
    def quitar(self, codigo, cantidad, catalogo):
        for seleccion in self.selecciones:
            if seleccion.codigo == codigo:
                if cantidad > seleccion.cantidad:
                    print("Cantidad a quitar mayor a la cantidad en el portafolio.")
                    return False
                seleccion.cantidad -= cantidad
                if seleccion.cantidad == 0:
                    self.selecciones.remove(seleccion)
                # Actualizamos la cantidad en el catalogo
                propiedad= catalogo.consultar_propiedad(codigo)
                propiedad.modificar(propiedad.tipo, propiedad.planeta,propiedad.descripcion, propiedad.cantidad + cantidad, propiedad.precio)
                return True

        # Si el bucle finaliza sin novedad, es que ese producto NO ESTA en el portafolio.
        print("El producto no se encuentra en el carrito.")
        return False

    def mostrar(self):
        print("-"*50)
        print("Lista de productos en el carrito:")
        print("Código\tTipo\tPlaneta\tDescripción\tCant\tPrecio")
        for seleccion in self.selecciones:
            print(f'{seleccion.codigo}\t{seleccion.tipo}\t{seleccion.planeta}\t{seleccion.descripcion}\t{seleccion.cantidad}\t{seleccion.precio}')
        print("-"*50)




# Programa principal
# Crear una instancia de la clase Catalogo
spmx_catalogo = Catalogo() 


# Agregar propiedades al catalogo
spmx_catalogo.agregar_propiedad(1,'CONDO', 'VENUS', '3 ambientes 2 baños Central Termonuclear propia', 1, 14500)
spmx_catalogo.agregar_propiedad(2,'CONDO', 'MARTE', '2 ambientes 1 baños', 1, 12500)
spmx_catalogo.agregar_propiedad(3,'DOMO', 'JUPITER', '2 ambientes 2 baños', 1, 17500)
spmx_catalogo.agregar_propiedad(4,'VILLA', 'NEPTUNO', '4 ambientes 3 baños', 1, 35000)
spmx_catalogo.agregar_propiedad(5,'DOMO', 'LUNA', '1 ambientes 1 baños', 1, 7500)

# Listar todos los propiedades del catalogo
spmx_catalogo.listar_propiedades()


# agrego 2 propiedades al portafolio del inversor
inversor_portafolio.agregar(1,1,spmx_catalogo)
inversor_portafolio.quitar(1,2,spmx_catalogo)


inversor_portafolio.mostrar()



spmx_catalogo.listar_propiedades()

spmx_catalogo.modificar_propiedad_propiedad(1,'CONDO', 'SATURNO', '3 ambientes 2 baños Central Termonuclear propia', 1, 20000)

spmx_catalogo.listar_propiedades()

spmx_catalogo.eliminar_propiedad(3)


spmx_catalogo.listar_propiedades()