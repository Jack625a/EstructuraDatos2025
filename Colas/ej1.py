#SIMULACION DE UNA COLA EN EL BANCO
#AGREGAR PERSONAS A LA COLA DE ESPERA PARA SER ATENDIDO
#UNA VEZ ES ATENDIDO LA PRIMERA PERSONA DE LA COLA ESTE SE RETIRA
#MOSTRAR LA COLA DE ESPERA

#PASO 1. DEFINIR LA CLASE
class ColaBanco:
    #Definir el contructor
    def __init__(self):
        self.personas=[]
    #PASO 2. CREAR LAS ACCIONES 
    #agregado de las personas
    def agregarPersona(self,numeroIngreso):
        self.personas.append(numeroIngreso)
        print(f"El numero: {numeroIngreso} en cola de espera...")
    
    #Atender a las personas
    def atender(self):
        if self.personas:
            cajero=self.personas.pop(0)
            print(f"El cajero atendio a la persona: {cajero}")
        else:
            print("No hay personas en la fila de espera...")
    #Mostrar la cola de espera
    def mostarColaEspera(self):
        if self.personas:
            print(f"Tickets en la cola de espera: {self.personas}")
        else:
            print("No hay tickets para atencion. Cola vacia...")


#Programa Principal

def menu():
    bancoBNB=ColaBanco()

    while True:
        print("Acciones")
        print("1. Ingresar a ser atendido")
        print("2. Salir")
        opcion=input("Seleccion la operacion ")
        if opcion=="1":
            numeroTicket=input("Numero de Ticket: ")
            bancoBNB.agregarPersona(numeroTicket)
        elif opcion=="2":
            print("Gracias por su visita...")
            break
        elif opcion=="Atender":
            bancoBNB.atender()
        elif opcion=="Mostrar":
            bancoBNB.mostarColaEspera()
        else: 
            print("Opcion invalida...")

menu()