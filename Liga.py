import random
def Datos():
    file = open("equips.cfg", "r")
    datos = file.read().splitlines()
    file.close()
    return(datos)


def crearLiga(Datos):
    Lista = []
    for i in Datos:
        for j in Datos:
            if i != j:
                Lista.append(j)
    Ligas = {}
    for i in range(0, len(Datos)):
        ListaTempo = []
        for j in range(1, len(Datos)):
            diccionario = {}
            diccionario[Lista[0]] = "none"
            del Lista[0]
            ListaTempo.append(diccionario)
            Ligas[str(Datos[i])] = ListaTempo
    return (Ligas)

def PuntosResultados():
    puntos1 = random.randint(0, 9)
    puntos2 = random.randint(0, 9)
    return (puntos1, puntos2)

def añadirResultados(Liga):
    global dicc
    for Local in Liga:
        for Visitentes in Liga[Local]:
            reultado = PuntosResultados()
            for puntos in Visitentes:
                dicc={}
                dicc[puntos] = reultado
            Visitentes.update(dicc)
    return(Liga)

def MostrarResultado(Liga,Datos):
    for j in range(1,len(Datos)):
        Datos[j] = {Datos[j]: 1}
    for Local in Liga:
        for Visitante in Liga[Local]:
            print("|",Local, "       |     \tcontra      ","|     ", Visitante, "|")


Datos = Datos()
Liga= crearLiga(Datos)
añadir=añadirResultados(Liga)
MostrarResultado(Liga,Datos)