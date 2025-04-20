#Crear una clase: MODELO O PLANTILLAS 

#Paso 1. Crear una clase (clase PilaPlatos)
#En Python se define una lista con (class NombreClase)
class PilaPlatos:
    #Paso 2. Definir el contructor de la clase
    #funciones en python se definen con (def nombreFuncion)
    def __init__(self):
        #Paso 3. crear la lista de platos
        #Guardamos los platos
        self.pila=[]
    
    #Paso 4. Agregar las acciones de la pila
    #PUSH, POP, PEEK
    def agregarPlato(self,plato): #PUSH
        self.pila.append(plato) #Apilamiento de platos
        print(f"Plato agregado correctamente: {plato}")

    def sacarPlato(self):
        platoSalir=self.pila.pop() #quitar el plato de la cima
        print(f"SACANDO EL PLATO DE LA CIMA: {platoSalir}")

    def verUltimoPlato(self):
        print(f"El plato ultimo es: {self.pila[-1]} ")



#Paso 5. Emular el apilado de platos
pila=PilaPlatos()

pila.agregarPlato("Plato Rojo")
pila.agregarPlato("Plato Verde")
pila.agregarPlato("Plato Rosado")
pila.agregarPlato("Plato Azul")

pila.verUltimoPlato()

pila.sacarPlato()
pila.sacarPlato()

pila.verUltimoPlato()

