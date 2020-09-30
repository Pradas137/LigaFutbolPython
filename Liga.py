import random
import operator


def partido():
    file = open("equips.cfg", "r")
    datos = file.read().splitlines()
    file.close()

    equipos = []
    for Local in datos:
        # print(Local)
        for Visitantes in datos:
            # print(Visitantes)
            if Local != Visitantes:
                equipos.append(Visitantes)
                #print(equipos)
    Liga=[]
    Ligas ={}
    for Local in range(0, len(datos)):
        Lista = []
        # print(Local)
        for Visitantes in range(1, len(datos)):
            # print(Visitantes)
            diccionario1 = {}
            diccionario1[equipos[0]] = "none"
            del equipos[0]
            Lista.append(diccionario1)
            # print(List)
            Ligas[str(datos[Local])] = Lista
    return (Ligas)


def PuntosResultados():
    puntos1 = random.randint(0, 9)
    puntos2 = random.randint(0, 9)
    return (puntos1, puntos2)


def añadiryMostrar(Partidos):
    diccionario2 = {}
    for Local in Partidos:
        # print(Local)
        for Visitantes in Partidos[Local]:
            # print(Visitantes)
            reultado = PuntosResultados()
            for puntos in Visitantes:
                # print(puntos)
                diccionario2[puntos] = reultado
            Visitantes.update(diccionario2)

    equips = open("equips.cfg", "r")
    datos = equips.read().splitlines()
    for j in range(1,len(datos)):
        datos[j] = {datos[j] : 1}
    equips.close()
    for Local in Partidos:
        # print(local)
        for pe in Partidos[Local]:
            # print(pe)
            for Visitante in pe:
                #print(Visitante)
                print("|",Local, "       |     \tcontra      ","|     ", Visitante, "|", pe.get(Visitante))

    #print(datos)


Partidos = partido()
Liga = añadiryMostrar(Partidos)