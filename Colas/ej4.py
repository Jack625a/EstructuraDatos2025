#Realizar la combinacion de pilas y colas en la simulacion
#sistema de navegacion WEB con historial y descargas

#PASO 1. DEFINIR LA CLASE
class Navegador:
    def __init__(self):
        self.historial=[] #Pila
        self.descargas=[] #Cola
        self.paginaActual="Inicio"

    #ACCIONES DE LA CLASE
    def visitarPagina(self,url):
        self.historial.append(self.paginaActual)
        self.paginaActual=url
        print(f"Ingresando a {url}")
    
    def irAtras(self):
        if not self.historial:
            print("No hay paginas anteriores")
            return 
        self.paginaActual=self.historial.pop()
        print(f"Volviendo atras {self.paginaActual}")

    def agregarDescarga(self,archivo):
        self.descargas.append(archivo)
        print(f"Agregado para descarga...{archivo}")
    
    def comenzarDescarga(self):
        if not self.descargas:
            print("No hay archivos para descargar")
        else:
            archivo=self.descargas.pop(0)
            print(f"Descargando el archivo {archivo}")
    
    def estado(self):
        print("Estado del Navegador")
        print(f"Pagina actual {self.paginaActual}")
        print("Historial " ,self.historial)
        print("Cola de descargas ", self.descargas)

chrome=Navegador()
chrome.visitarPagina("github.com")
chrome.visitarPagina("youtube.com")
chrome.estado()
chrome.irAtras()

chrome.agregarDescarga("git.exe")
chrome.agregarDescarga("libro.pdf")
chrome.comenzarDescarga()

chrome.estado()