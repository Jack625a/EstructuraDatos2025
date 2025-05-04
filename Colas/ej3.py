#Ej1. Realizar la combinacion de pilas y colas 
#PILA (Ultimo en entrar es el primero en salir)
#COLAS (El primero en ingresar es el primero en salir)

#Realizar la simulacin de un sistema de atencion de cliente pero con prioridad emergente
#ATENCION DE CLIENTES EN BANCO
#CLIENTES COMUNES -> COLA DE ESPERA 

#CLIENTES PRIORITARIOS
#1. CLIENTES TERCERA EDAD 
#2. CLIENTES MUJERES EMBARAZADAS
#APILARSE 

class SistemaAtencion:
    def __init__(self):
        self.clienteNormales=[] #Cola de espera de los clientes normales
        self.clientesPrioritarios=[] #Clientes con prioridad (Tercera edad, Mujeres embarazadas)
    
    #Acciones de la clase
    def llegadaClientes(self,codigo,prioridad=False):
        if prioridad:
            self.clientesPrioritarios.append(codigo)
            print(f"Cliente con prioridad {codigo} ")
        else:
            self.clienteNormales.append(codigo)
            print(f"Cliente comun {codigo}")
    
    #accion para atencion
    def atenderCliente(self):
        if len(self.clientesPrioritarios)>0:
            cliente=self.clientesPrioritarios.pop()
            print(f"Se atendio al cliente prioritario {cliente}")
        elif len(self.clienteNormales)>0:
            cliente=self.clienteNormales.pop(0)
            print(f"Se atendio al cliente comun {cliente}")
        else:
            print("No hay clientes para atender...")
    
    def mostrarClientes(self):
        print("Clientes comunes en espera", self.clienteNormales)
        print("Clientes prioritarios en espera", self.clientesPrioritarios)

#simulacion
banco=SistemaAtencion()

banco.llegadaClientes("C123")
banco.llegadaClientes("C124")
banco.llegadaClientes("C125")
banco.llegadaClientes("C126")
banco.llegadaClientes("P1",prioridad=True)
banco.llegadaClientes("C127")
banco.llegadaClientes("P2",prioridad=True)

banco.mostrarClientes()

banco.atenderCliente()
banco.atenderCliente()
banco.atenderCliente()

banco.llegadaClientes("P3",prioridad=True)

banco.atenderCliente()
banco.atenderCliente()
banco.atenderCliente()

banco.mostrarClientes()
banco.atenderCliente()
banco.atenderCliente()