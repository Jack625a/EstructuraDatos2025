#PASO 1. CREAR LA CLASE NODO
class Nodo:
    def __init__(self,valor):
        self.valor=valor
        self.siguiente=None

#PASO 2. CREAR LA CLASE PARA LA LISTA ENLAZADA
class ListaEnlazada:
    def __init__(self):
        self.cabeza=None
    
    #PASO 3. METODOS DE LA LISTA ENLAZADA
    def verificacionVacio(self):
        return self.cabeza is None
    
    #METODO PARA AGREGAR AL INICIO
    def agregarAlInicio(self,valor):
        nuevoNodo=Nodo(valor)
        nuevoNodo.siguiente=self.cabeza
        self.cabeza=nuevoNodo

    #METODO PARA AGREGAR AL FINAL
    def agregarAlFinal(self,valor):
        nuevoNodo=Nodo(valor)
        if self.verificacionVacio():
            self.cabeza=nuevoNodo
        else:
            actual=self.cabeza
            while actual.siguiente:
                actual=actual.siguiente
            actual.siguiente=nuevoNodo

    def mostrar(self):
        actual=self.cabeza
        while actual:
            print(actual.valor, end=" ->")
            actual=actual.siguiente
        print("None")


#Aplicacion
lista=ListaEnlazada()
lista.agregarAlInicio(10)
lista.agregarAlInicio(20)
lista.agregarAlFinal(8)
lista.agregarAlInicio(30)

lista.mostrar()
        