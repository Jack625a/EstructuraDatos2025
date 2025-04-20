#Crear una Pila de Productos en un Almacen
#Manejar productos en un almacen donde los productos se apilaran
#tambien se retirararan siguiendo el principio LIFO
#NOTA (AGREGAR-RETIRAR-MIRAR "PUSH,POP,PECK")

#Paso 1. Crear la clase 
class Almacen:
    #Paso 2. Definir el contructor
    def __init__(self):
        #Crear la pila de productos
        self.pilaProducto=[]
    
    #Paso 3. Definir las acciones o metodos de la clase
    #ACCION PARA AGREGAR UN PRODUCTO (PUSH)
    def agregarProducto(self, producto):
        self.pilaProducto.append(producto)
    #ACCION PARA RETIRAR UN PRODUCTO (POP)
    def retirarProducto(self):
        if self.pilaProducto:
            producto=self.pilaProducto.pop()
            print(f"Producto retirado: {producto}")
        else:
            print("El almacen esta vacio...")
    #ACDCION PARA MIRAR LOS PRODUCTOS (PECK)
    def mirarProductos(self):
        if self.pilaProducto:
            print("Producto del Almacen",self.pilaProducto)
        else:
            print("El almacen esta vacio...")

#Paso 4. Probar el almacen (Creacion de objetos de la clase)
almacen=Almacen()

almacen.agregarProducto("Laptop")
almacen.agregarProducto("Mouse")
almacen.agregarProducto("Teclado")
almacen.agregarProducto("Parlantes")
almacen.agregarProducto("Celular")
almacen.agregarProducto("Tablet")

#Mostrar los productos
almacen.mirarProductos()

#Retirar productos
almacen.retirarProducto()