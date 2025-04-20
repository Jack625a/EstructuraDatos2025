#Cola Simple
#2 ACCIONES DE UNA COLAS ENCOLAR (INSERTAR ELEMENTOS AL FINAL DE LA COLA)
#DESENCOLAR (ELIMINAR EL PRIMER ELEMENTO DE LA COLAS)

#PASO 1. DEFINIR LA CLASE (COLA)
class Cola:
    #Paso 2. Definir el constructor
    def __init__(self,):
        self.cola=[]
    #Paso 3. Crear las acciones
    #Encolar
    def ingresarCola(self,elemeto):
        self.cola.append(elemeto)
        print(f"El elemento {elemeto} fue agregado...")
    #Desencolar
    def salirCola(self):
        return self.cola.pop(0)

    #Mostrar Cola
    def mostrar(self):
        print("la cola de espera es: ",self.cola)


#Paso 4. Crear los objetos de la cola
cola=Cola()
cola.ingresarCola("Persona 1")
cola.ingresarCola("Persona 2")
cola.ingresarCola("Persona 3")
cola.ingresarCola("Persona 4")   
cola.mostrar()
cola.salirCola()
cola.mostrar()
cola.salirCola()
cola.mostrar()
cola.salirCola()
cola.mostrar()
cola.ingresarCola("Perosna 5")
cola.ingresarCola("Persona 6")
cola.mostrar()