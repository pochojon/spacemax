import sqlite3


# Configurar la conexión a la base de datos SQLite
DATABASE = 'spacemaxpropiedades.db'

def get_db_connection():
    print("Obteniendo conexión...") # Para probar que se ejecuta la función
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Crear la tabla 'productos' si no existe
def create_table():
    print("Creando tabla propiedades...") # Para probar que se ejecuta la función
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS propiedades (
            codigo INTEGER PRIMARY KEY,
            tipo TEXT NOT NULL,
            planeta TEXT NOT NULL,
            descripcion TEXT NOT NULL,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL
        ) ''')
    
    conn.commit()
    cursor.close()
    conn.close()

# Verificar si la base de datos existe, si no, crearla y crear la tabla
def create_database():
    print("Creando la BD...") # Para probar que se ejecuta la función
    conn = sqlite3.connect(DATABASE)
    conn.close()
    create_table()





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
        self.conexion = get_db_connection()
        self.cursor = self.conexion.cursor()


    # Este método permite crear objetos de la clase "Propiedad" y agregarlos al catalogo
    def agregar_propiedad(self, codigo, tipo, planeta, descripcion, cantidad, precio):
        propiedad_existente = self.consultar_propiedad(codigo)
        if propiedad_existente:
            print("Ya existe una propiedad con ese código.")
            #return False
            print("como ya exsiste la modifico.")
            sql = f'UPDATE propiedades SET tipo = "{tipo}",planeta = "{planeta}",descripcion = "{descripcion}", cantidad = {cantidad}, precio = {precio} WHERE codigo = {codigo};' 
            self.cursor.execute(sql)
            self.conexion.commit()
            return True

        #nueva_propiedad = Propiedad(codigo, tipo, planeta, descripcion, cantidad, precio)
        sql = f'INSERT INTO propiedades VALUES ({codigo}, "{tipo}", "{planeta}", "{descripcion}", {cantidad}, {precio});'
        self.cursor.execute(sql)
        self.conexion.commit()
        return True



    # Este método permite consultar datos de las propiedades que están en el catalogo de propiedades
    # Devuelve la propiedad correspondiente al código proporcionado o False si no existe.
    def consultar_propiedad(self, codigo):
        sql = f'SELECT * FROM propiedades WHERE codigo = {codigo};'
        self.cursor.execute(sql)
        row = self.cursor.fetchone()
        if row:
            codigo, tipo, planeta, descripcion, cantidad, precio = row
            return Propiedad(codigo, tipo, planeta,descripcion, cantidad, precio)
        return False


# Utiliza el método consultar_propiedad del catalogo de propioedades para modificar la propiedad.
    def modificar_propiedad(self, codigo, nuevo_tipo, nuevo_planeta,nueva_descripcion, nueva_cantidad, nuevo_precio):
        propiedad = self.consultar_propiedad(codigo)
        if propiedad:
            propiedad.modificar(nuevo_tipo, nuevo_planeta,nueva_descripcion, nueva_cantidad, nuevo_precio)
            sql = f'UPDATE propiedades SET tipo = "{nuevo_tipo}",planeta = "{nuevo_planeta}",descripcion = "{nueva_descripcion}", cantidad = {nueva_cantidad}, precio = {nuevo_precio} WHERE codigo = {codigo};' 
            self.cursor.execute(sql)
            self.conexion.commit()


    # Este método elimina la propiedad indicado por codigo de la lista mantenida en el catalogo de propiedades
    def eliminar_propiedad(self, codigo):
        sql = f'DELETE FROM propiedades WHERE codigo = {codigo};' 
        self.cursor.execute(sql)
     
        if self.cursor.rowcount > 0:
            print(f'Producto {codigo} eliminado.')
            self.conexion.commit()
        else:
            print(f'Producto {codigo} no encontrado.')

    # Este método imprime en la terminal una lista con los datos de las propiedades que figuran en el catalogo de proopiedades
    def listar_propiedades(self):
        print("-"*50)
        print("Lista de propiedades en el catalogo de propiedades:")
        print("Código\tTipo\tPlaneta\tDescripción\tCant\tPrecio")
        self.cursor.execute("SELECT * FROM propiedades")
        rows = self.cursor.fetchall()
        for row in rows:
            codigo, tipo, planeta,descripcion, cantidad, precio = row
            print(f'{codigo}\t{tipo}\t{planeta}\t{descripcion}\t{cantidad}\t{precio}')
        print("-"*50)





# El inversor elegirá propiedades del catalogo de propiedades y las irá colocalndo o quitándolas de su portafolio


class Portafolio:
    # Definimos el constructor e inicializamos los atributos de instancia
    def __init__(self):
        self.conexion = sqlite3.connect('spacemaxpropiedades.db')  # Conexión a la BD
        self.cursor = self.conexion.cursor()
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
                sql = f'UPDATE propiedades SET cantidad = cantidad - {cantidad}  WHERE codigo = {codigo};'
                self.cursor.execute(sql)
                self.conexion.commit()
                return True

        # Si no existe en el portafolio, lo agregamos como un nueva seleccion .
        nueva_seleccion = Propiedad(codigo, propiedad.tipo, propiedad.planeta, propiedad.descripcion, cantidad, propiedad.precio)
        self.selecciones.append(nueva_seleccion)
        # Actualizamos la cantidad en el catalogo
        sql = f'UPDATE propiedades SET cantidad = cantidad - {cantidad}  WHERE codigo = {codigo};'
        self.cursor.execute(sql)
        self.conexion.commit()
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
                sql = f'UPDATE propiedades SET cantidad = cantidad + {cantidad} WHERE codigo = {codigo};'
                self.cursor.execute(sql)
                self.conexion.commit()

                return True

        # Si el bucle finaliza sin novedad, es que ese producto NO ESTA en el portafolio.
        print("El producto no se encuentra en el portafolio.")
        return False

    def mostrar(self):
        print("-"*50)
        print("Lista de productos en el carrito:")
        print("Código\tTipo\tPlaneta\tDescripción\tCant\tPrecio")
        for seleccion in self.selecciones:
            print(f'{seleccion.codigo}\t{seleccion.tipo}\t{seleccion.planeta}\t{seleccion.descripcion}\t{seleccion.cantidad}\t{seleccion.precio}')
        print("-"*50)




# Programa principal
create_database()
# Crear una instancia de la clase Inventario
spmx_catalogo = Catalogo() 





# Agregar productos 
spmx_catalogo.agregar_propiedad(1,'CONDO', 'VENUS', '3 ambientes 2 baños Central Termonuclear propia', 1, 14500)
spmx_catalogo.agregar_propiedad(2,'CONDO', 'MARTE', '2 ambientes 1 baños', 1, 12500)
spmx_catalogo.agregar_propiedad(3,'DOMO', 'JUPITER', '2 ambientes 2 baños', 1, 17500)
spmx_catalogo.agregar_propiedad(4,'VILLA', 'NEPTUNO', '4 ambientes 3 baños', 1, 35000)
spmx_catalogo.agregar_propiedad(5,'DOMO', 'LUNA', '1 ambientes 1 baños', 1, 7500)
spmx_catalogo.agregar_propiedad(5,'DOMO', 'PLUTON', '1 ambientes 1 baños', 1, 20500)

# Consultar algún producto del inventario
print(spmx_catalogo.consultar_propiedad(3)) #Existe, se muestra la dirección de memoria
print(spmx_catalogo.consultar_propiedad(1)) #No existe, se muestra False


# Listar todos los productos
spmx_catalogo.listar_propiedades()

spmx_catalogo.modificar_propiedad(2,'CONDO', 'SATURNO', '2 ambientes 1 baños', 1, 30000)

spmx_catalogo.listar_propiedades()

spmx_catalogo.eliminar_propiedad(4)

spmx_catalogo.listar_propiedades()

# creo una instancia de la calse Portafolio
inversor_portafolio = Portafolio()

# agrego al potafolio una propiedad del codigo 1 y la quito del catalogo
inversor_portafolio.agregar(1,1,spmx_catalogo)
# agrego al portafolio una propiedad del codigo 2 y la quito del catalogo
inversor_portafolio.agregar(2,1,spmx_catalogo)

inversor_portafolio.mostrar()
spmx_catalogo.listar_propiedades()




