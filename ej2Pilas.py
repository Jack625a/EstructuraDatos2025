#Ejercicio 2.22/03/2025
#Simulacion del manejor del historial de navegacion Web
#Control de historial de Navegacion con Pilas

#Paso 1.  Crear la clase para el Historial
class HistorialNavegacion:
    #Paso 2. Definir el constructor
    def __init__(self):
        self.pila=[]
    
    #Paso 3. Crear las acciones de la ´Pila (VISITAR PAGINA, RETROCEDER "push, pop", peck)
    #VISITAR UNA PAGINA
    def visitarPagina(self, pagina):
        self.pila.append(pagina)
        print(f"Ingresando al sitio web: {pagina}")
    
    def retrocederPagina(self):
        if self.pila:
            paginaActual=self.pila.pop()
            print("Se obtubo del historial la pagina: ",paginaActual)
        else:
            print("No hay paginas en el historial")
    
    def mostrarHistorial(self):
        if self.pila:
            print("El historial de navegacion es: ",self.pila)
        else:
            print("El historial esta vacio")

#Paso 4. SIMULAR EL PROCESO DEL HISTORIAL

historialNavegadorChrome=HistorialNavegacion()

historialNavegadorChrome.visitarPagina("Wikipedia")
historialNavegadorChrome.visitarPagina("Github")
historialNavegadorChrome.visitarPagina("Youtube")
historialNavegadorChrome.visitarPagina("ClassRoom")

historialNavegadorChrome.mostrarHistorial()
historialNavegadorChrome.retrocederPagina()
historialNavegadorChrome.mostrarHistorial()
historialNavegadorChrome.retrocederPagina()
historialNavegadorChrome.mostrarHistorial()
historialNavegadorChrome.retrocederPagina()
historialNavegadorChrome.mostrarHistorial()
