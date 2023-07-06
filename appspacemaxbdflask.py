import sqlite3
from flask import Flask, jsonify, request

# Configurar la conexión a la base de datos SQLite
DATABASE = 'spacemaxpropiedades.db'

def get_db_connection():
    print("Obteniendo conexión...") # Para probar que se ejecuta la función
    conn = sqlite3.connect(DATABASE,check_same_thread=False)
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
            sql = f'UPDATE propiedades SET tipo = "{tipo}",planeta = "{planeta}",descripcion = "{descripcion}", cantidad = {cantidad}, precio = {precio} WHERE codigo = {codigo};' 
            self.cursor.execute(sql)
            self.conexion.commit()
            return jsonify({'message': 'Ya existe una propiedad con ese código. pero igual lo modifico con los nuevos valores'}), 200
        #nueva_propiedad = Propiedad(codigo, tipo, planeta, descripcion, cantidad, precio)
        sql = f'INSERT INTO propiedades VALUES ({codigo}, "{tipo}", "{planeta}", "{descripcion}", {cantidad}, {precio});'
        self.cursor.execute(sql)
        self.conexion.commit()
        return jsonify({'message': 'Propiedad agregado correctamente.'}), 200



    # Este método permite consultar datos de las propiedades que están en el catalogo de propiedades
    # Devuelve la propiedad correspondiente al código proporcionado o False si no existe.
    def consultar_propiedad(self, codigo):
        sql = f'SELECT * FROM propiedades WHERE codigo = {codigo};'
        self.cursor.execute(sql)
        row = self.cursor.fetchone()
        if row:
            codigo, tipo, planeta, descripcion, cantidad, precio = row
            return Propiedad(codigo, tipo, planeta,descripcion, cantidad, precio)
        return None


# Utiliza el método consultar_propiedad del catalogo de propioedades para modificar la propiedad.
    def modificar_propiedad(self, codigo, nuevo_tipo, nuevo_planeta,nueva_descripcion, nueva_cantidad, nuevo_precio):
        propiedad = self.consultar_propiedad(codigo)
        if propiedad:
            propiedad.modificar(nuevo_tipo, nuevo_planeta,nueva_descripcion, nueva_cantidad, nuevo_precio)
            sql = f'UPDATE propiedades SET tipo = "{nuevo_tipo}",planeta = "{nuevo_planeta}",descripcion = "{nueva_descripcion}", cantidad = {nueva_cantidad}, precio = {nuevo_precio} WHERE codigo = {codigo};' 
            self.cursor.execute(sql)
            self.conexion.commit()
            return jsonify({'message': 'Propiedad modificado correctamente.'}), 200
        return jsonify({'message': 'Propiedad no encontrado.'}), 404



    # Este método elimina la propiedad indicado por codigo de la lista mantenida en el catalogo de propiedades
    def eliminar_propiedad(self, codigo):
        sql = f'DELETE FROM propiedades WHERE codigo = {codigo};' 
        self.cursor.execute(sql)
     
        if self.cursor.rowcount > 0:
            self.conexion.commit()
            return jsonify({'message': 'Propiedad eliminado correctamente.'}), 200
        return jsonify({'message': 'Propiedad no encontrado.'}), 404


    # Este método imprime en la terminal una lista con los datos de las propiedades que figuran en el catalogo de proopiedades
    def listar_propiedades(self):
        self.cursor.execute("SELECT * FROM propiedades")
        rows = self.cursor.fetchall()
        propiedades = []
        for row in rows:
            codigo, tipo, planeta, descripcion, cantidad, precio = row
            producto = {'codigo': codigo, 'tipo': tipo,'planeta': planeta,'descripcion': descripcion, 'cantidad': cantidad, 'precio': precio}
            propiedades.append(producto)
        return jsonify(propiedades), 200




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
        if propiedad is None: 
            return jsonify({'message': 'La propiedad no existe.'}), 404
        
        # Verificamos que la cantidad en stock sea suficiente
        if propiedad.cantidad < cantidad:
            return jsonify({'message': 'Cantidad en catalogo insuficiente.'}), 400


        # Si existe y hay stock, vemos si ya existe en el carrito.
        for seleccion in self.selecciones:
            if seleccion.codigo == codigo:
                seleccion.cantidad += cantidad
                # Actualizamos la cantidad en el catalogo
                sql = f'UPDATE propiedades SET cantidad = cantidad - {cantidad}  WHERE codigo = {codigo};'
                self.cursor.execute(sql)
                self.conexion.commit()
                return jsonify({'message': 'Propiedad agregada al portafolio correctamente.'}), 200



        # Si no existe en el portafolio, lo agregamos como un nueva seleccion .
        nueva_seleccion = Propiedad(codigo, propiedad.tipo, propiedad.planeta, propiedad.descripcion, cantidad, propiedad.precio)
        self.selecciones.append(nueva_seleccion)
        # Actualizamos la cantidad en el catalogo
        sql = f'UPDATE propiedades SET cantidad = cantidad - {cantidad}  WHERE codigo = {codigo};'
        self.cursor.execute(sql)
        self.conexion.commit()
        return jsonify({'message': 'Propiedad agregada al portafolio correctamente.'}), 200


    # Este método quita unidades de una propiedad del portafolio, o lo elimina.
    def quitar(self, codigo, cantidad, catalogo):
        for seleccion in self.selecciones:
            if seleccion.codigo == codigo:
                if cantidad > seleccion.cantidad:
                    return jsonify({'message': 'Cantidad a quitar mayor a la cantidad en el portafolio.'}), 400
                seleccion.cantidad -= cantidad
                if seleccion.cantidad == 0:
                    self.selecciones.remove(seleccion)
                # Actualizamos la cantidad en el catalogo
                sql = f'UPDATE propiedades SET cantidad = cantidad + {cantidad} WHERE codigo = {codigo};'
                self.cursor.execute(sql)
                self.conexion.commit()
                return jsonify({'message': 'Propiedad quitado del portafolio correctamente.'}), 200

        # Si el bucle finaliza sin novedad, es que ese producto NO ESTA en el portafolio.
        return jsonify({'message': 'La propiedad no se encuentra en el portafolio.'}), 404

    def mostrar(self):
        propiedades_portafolio = []
        for seleccion in self.selecciones:
            propiedad = {'codigo': seleccion.codigo,'tipo': seleccion.tipo,'planeta': seleccion.planeta,'descripcion': seleccion.descripcion, 'cantidad': seleccion.cantidad, 'precio': seleccion.precio}
            propiedades_portafolio.append(propiedad)
        return jsonify(propiedades_portafolio), 200

# creamos una instancia de la clase Flask llamada app
app = Flask(__name__)

# Crear una instancia de la clase Inventario
spmx_catalogo = Catalogo() 
# creo una instancia de la calse Portafolio
inversor_portafolio = Portafolio()

# Ruta para obtener los datos de un producto según su código
@app.route('/propiedades/<int:codigo>', methods=['GET'])
def obtener_propiedad(codigo):
    propiedad = spmx_catalogo.consultar_propiedad(codigo)
    if propiedad:
        return jsonify({
            'codigo': propiedad.codigo,
            'tipo': propiedad.tipo,
            'planeta': propiedad.planeta,
            'descripcion': propiedad.descripcion,
            'cantidad': propiedad.cantidad,
            'precio': propiedad.precio
        }), 200
    return jsonify({'message': 'Propiedad no encontrado.'}), 404


# Ruta para obtener la lista de productos del inventario
@app.route('/')
def index():
    return 'API de Catalogo de Propiedades Space/Max'

# Ruta para obtener la lista de productos del inventario
@app.route('/propiedades', methods=['GET'])
def obtener_propiedades():
    return spmx_catalogo.listar_propiedades()


# Ruta para agregar una propiedad al catalogo de propiedades
@app.route('/propiedades', methods=['POST'])
def agregar_propiedades():
    codigo = request.json.get('codigo')
    tipo = request.json.get('tipo')
    planeta = request.json.get('planeta')
    descripcion = request.json.get('descripcion')
    cantidad = request.json.get('cantidad')
    precio = request.json.get('precio')
    return spmx_catalogo.agregar_propiedad(codigo, tipo, planeta, descripcion, cantidad, precio)



# Ruta para modificar un producto del inventario
@app.route('/propiedades/<int:codigo>', methods=['PUT'])
def modificar_propiedad(codigo):
    nuevo_tipo = request.json.get('tipo')
    nuevo_planeta = request.json.get('planeta')
    nueva_descripcion = request.json.get('descripcion')
    nueva_cantidad = request.json.get('cantidad')
    nuevo_precio = request.json.get('precio')
    return spmx_catalogo.modificar_propiedad(codigo, nuevo_tipo, nuevo_planeta,nueva_descripcion, nueva_cantidad, nuevo_precio)


# Ruta para eliminar una propiedadd del catalogo de propiedades 
@app.route('/propiedades/<int:codigo>', methods=['DELETE'])
def eliminar_propiedades(codigo):
    return spmx_catalogo.eliminar_propiedad(codigo)


# Ruta para agregar un propiedad al portafolio del inversor
@app.route('/portafolio', methods=['POST'])
def agregar_portafolio():
    codigo = request.json.get('codigo')
    tipo = request.json.get('tipo')
    planeta = request.json.get('planeta')
    cantidad = request.json.get('cantidad')
    catalogo = Catalogo()
    return inversor_portafolio.agregar(codigo, tipo, planeta,cantidad,catalogo)

# Ruta para quitar un producto del carrito
@app.route('/portafolio', methods=['DELETE'])
def quitar_portafolio():
    codigo = request.json.get('codigo')
    tipo = request.json.get('tipo')
    planeta = request.json.get('planeta')
    cantidad = request.json.get('cantidad')
    catalogo = Catalogo()
    return inversor_portafolio.quitar(codigo, tipo, planeta,cantidad, catalogo)


# Ruta para obtener el contenido del portafolio del inversor
@app.route('/portafolio', methods=['GET'])
def obtener_portafolio():
    return inversor_portafolio.mostrar()


# Finalmente, si estamos ejecutando este archivo, lanzamos app.
if __name__ == '__main__':
    app.run()
