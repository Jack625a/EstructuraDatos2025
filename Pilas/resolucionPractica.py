#Paso 1 CLASE PILA
class Pila:
    def __init__(self):
        self.items=[]
    
    #ACCIONES DE LA CLASE
    #APILAR, DESAPILAR, MOSTRAR PILA, MOSTRAR EL ULTIMO ELEMENTO, VERIFICAT SI LA PILA ESTA VACIA
    def pilaVacia(self):
        return len(self.items)==0
    
    def apilar(self,item):
        self.items.append(item)
    
    def desapilar(self):
        if not self.pilaVacia():
            return self.items.pop()
        return None
    
    def mostrarPila(self):
        print(self.items)

#Ej1. Simulacion de deshacer en word
class Word:
    def __init__(self):
        self.historial=Pila()
    
    def escribir(self, palabra):
        self.historial.apilar(palabra)
    def deshacer(self):
        return self.historial.desapilar()
    def mostrarTexto(self):
        print((self.historial.mostrarPila()))

word=Word()
word.escribir("Hola")
word.escribir("Prueba")
word.mostrarTexto()
word.deshacer()
word.mostrarTexto()

#Eje2.Simular caja registradora
class Caja():
    def __init__(self):
        self.caja=Pila()
    
    def recibirDinero(self,dinero):
        self.caja.apilar(dinero)
    
    def devolverCambio(self):
        return self.caja.desapilar()
    
    def mostrarCaja(self):
        self.caja.mostrarPila()

#Ej3. Sistema de control de tareas
class Tareas:
    def __init__(self):
        self.tareas=Pila()
    
    def agregarTarea(self,tarea):
        self.tareas.apilar(tarea)
    
    def completarTarea(self):
        return self.tareas.desapilar()
    
    def mostrarPendientes(self):
        self.tareas.mostrarPila()

caja=Caja()
caja.recibirDinero(150)
caja.recibirDinero(200)
caja.mostrarCaja()
caja.devolverCambio()

tareas=Tareas()
tareas.agregarTarea("PruebaTarea")
tareas.agregarTarea("Tarea2")
tareas.mostrarPendientes()
tareas.completarTarea()
tareas.mostrarPendientes()


llamadas=Pila()
#REGISTRAR LLAMADA APILAR
def registarLlamada(llamada):
    llamadas.apilar()

def contestar():
    llamadas.desapilar()