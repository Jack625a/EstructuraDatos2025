#LISTA ENLAZADA CON AGREGADO EN DIFERENTES POSICIONES
#PASO 1. CREAR LA CLASE NODO
class Nodo:
    def __init__(self, dato):
        self.dato=dato
        self.siguiente=None

#Paso 2. CREAR LA LISTA ENLAZADA DE ESTUDIANTES
class ListaEnlazadaEstudiantes:
    def __init__(self):
        self.cabeza=None

    #Paso 3. CREAR LOS METODOS O ACCIONES DE LA CLASE 
    def agregarEstudiantes(self,estudiante):
        nuevoEstudiante=Nodo(estudiante)
        if not self.cabeza:
            self.cabeza=nuevoEstudiante
        else:
            actual=self.cabeza
            while actual.siguiente:
                actual=actual.siguiente
            actual.siguiente=nuevoEstudiante
        
    #Mostrar los estudiante
    def mostrar(self):
        actual=self.cabeza
        while actual:
            print(actual.dato)
            actual=actual.siguiente
    #FUNCION PARA AGREGAR EN DIFERENTES POSICIONES
    def agregarPosicionIndicada(self,posicion,estudiante):
        nuevoEstudiante=Nodo(estudiante)
        #verificar la posicion 
        if posicion==0:
            nuevoEstudiante.siguiente=self.cabeza
            self.cabeza=nuevoEstudiante
            return
        actual=self.cabeza
        contador=0
        while actual and contador <posicion-1:
            actual=actual.siguiente
            contador=contador+1

        if actual:
            nuevoEstudiante.siguiente=actual.siguiente
            actual.siguiente=nuevoEstudiante

#Paso 4.CREAR LOS OBJETOS DE LA CLASE - ESTUDIANTES
lista=ListaEnlazadaEstudiantes()
lista.agregarEstudiantes("Kevin Arroyo")
lista.agregarEstudiantes("Juan Perez")
lista.agregarEstudiantes("Ana Perez")
lista.agregarEstudiantes("Jesus")
lista.agregarEstudiantes("Jose")
lista.mostrar()
print("ESTUDIANTES EN DIFERENTES POSICIONES")
lista.agregarPosicionIndicada(1,"Carlos")
lista.agregarPosicionIndicada(4,"Maria")
lista.mostrar()

