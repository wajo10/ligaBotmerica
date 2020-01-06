import io
from math import *

import PIL

import facebook
from PIL import Image, ImageDraw, ImageFont
from random import *
import xml.etree.ElementTree as ET
global fechas, tabla, listaEquipos, campeonRegular, campeonLiguilla, campeonTotal, serie1, serie2, serie3, fecha, resultados, mensajeExtra
graph =  facebook.GraphAPI(access_token='EAAIbeSGZBSXABAOzVoYjHhplTrq1DjUQBZCoRVOqOzGIgwbavjywk4Bp1vwjwMDekZCiLDIbuVyO2PGViVuizny5HaCe8v6LmVJIlziISYnBaHmf5CFFdKhW1UO3JxhRaSDgAe46VUYrL2ObWtvMnk5VrUeLgZC29Mz9fQ7afAZDZD')
listaEquipos = []
tabla = []
fecha = 0
resultados = []
campeonRegular = None
campeonLiguilla = None
campeonTotal = None
mensajeExtra = ""
class equipo:
    nombre = ""
    puntos = 0
    golFavor = 0
    golContra = 0
    golDiferencia = golFavor-golContra
    derrotas = 0
    imagen= Image.open('img/liga3.png')
    def __init__(self,nombre):
        self.nombre = nombre
        listaEquipos.append(self)

# __________Simula cada fecha del campeonato
def jornada(partidos):
    global fecha, resultados
    resultados = []
    for x in range(0,len(partidos)):
        equipo1 = partidos[x][0]
        equipo2 = partidos[x][1]
        temporal = randint(0,22)
        temporal2 = randint(0,22)
        goles1 = 0
        goles2 =0
        posibilidad = 0
        if temporal < 18:
            posibilidad = 3
        elif temporal >= 18 and temporal <= 20:
            posibilidad = 5
        elif temporal >= 21:
            posibilidad = 7

        if temporal2 < 18:
            posibilidad2 = 3
        elif temporal2 >= 18 and temporal2 <= 20:
            posibilidad2 = 5
        elif temporal2 >= 21:
            posibilidad2 = 7

        if equipo1.derrotas - equipo2.derrotas > 5:
            goles1 = randint(0,posibilidad-1)
            goles2 = randint(0,posibilidad2)
        elif equipo1.derrotas - equipo2.derrotas > 2 and equipo1.derrotas - equipo2.derrotas <= 5:
            goles1 = randint(0, posibilidad - 1)
            goles2 = randint(0, posibilidad2)
        elif equipo2.derrotas - equipo1.derrotas > 5:
            goles1 = randint(0, posibilidad)
            goles2 = randint(0, posibilidad2 -2)
        elif equipo2.derrotas - equipo1.derrotas > 2 and equipo2.derrotas - equipo1.derrotas <= 5:
            goles2 = randint(0, posibilidad2 - 1)
            goles1 = randint(0, posibilidad)
        else:
            goles2 = randint(0, posibilidad2)
            goles1 = randint(0, posibilidad)
        if equipo1 == lda or equipo1== saprissa:
            goles1 = randint(0,posibilidad +1)
        if equipo2 == lda:
            goles2 = randint(0,posibilidad2 +1)
        equipo1.golFavor+=goles1
        equipo1.golContra+=goles2
        equipo2.golFavor+=goles2
        equipo2.golContra+=goles1
        equipo1.golDiferencia=equipo1.golFavor-equipo1.golContra
        equipo2.golDiferencia = equipo2.golFavor - equipo2.golContra
        if goles1 > goles2:
            equipo1.puntos+=3
            equipo2.derrotas+=1
        elif goles2 > goles1:
            equipo2.puntos+=3
            equipo1.derrotas += 1
        elif goles1 == goles2:
            equipo1.puntos+=1
            equipo2.puntos+=1
        print(equipo1.nombre + " "+ str(goles1) + " " + equipo2.nombre + " "+ str(goles2))
        resultados.append([goles1,goles2])
def semifinales(serie):
    global serie1, serie2, fecha, global1Serie1, global2Serie1,global1Serie2, global2Serie2, finalista1, finalista2, mensajeExtra
    equipo1 = serie[0][0]
    equipo2 = serie[1][0]
    goles1global = serie[0][1]
    goles2global = serie[1][1]
    numSerie = serie[2]
    partido = serie[3]

    posibilidad = 0

    if partido == 1:
        temporal = randint(0, 22)
        if temporal < 15:
            posibilidad = 3
        elif temporal >= 15 and temporal <= 20:
            posibilidad = 5
        elif temporal > 20:
            posibilidad = 7
        goles1 = randint(0, posibilidad)
        goles2 = randint(0, posibilidad)
        if equipo1 == lda:
            goles1 = randint(0,posibilidad +1)
        if equipo2 == lda:
            goles2 = randint(0,posibilidad +1)


        # equipo1.golFavor += goles1
        # equipo1.golContra += goles2
        # equipo2.golFavor+=goles2
        # equipo2.golContra+=goles1
        # equipo1.golDiferencia = equipo1.golFavor - equipo1.golContra
        # equipo2.golDiferencia = equipo2.golFavor - equipo2.golContra
        # if goles1>goles2:
        #     equipo1.puntos+=3
        # elif goles1==goles2:
        #     equipo1.puntos+=1
        #     equipo2.puntos+=1
        # elif goles2>goles1:
        #     equipo2.puntos+=3
        if numSerie == 1:
            serie1 = [[equipo1,goles1],[equipo2,goles2],1,2]
        elif numSerie == 2:
            serie2 = [[equipo1, goles1], [equipo2, goles2], 2, 2]
        print(equipo1.nombre + " "+ str(goles1) + " " + equipo2.nombre + " "+ str(goles2))
    elif partido == 2:
        temporal = randint(0, 22)
        if temporal < 15:
            posibilidad = 3
        elif temporal >= 15 and temporal <= 20:
            posibilidad = 5
        elif temporal > 20:
            posibilidad = 7
        goles1 = randint(0, posibilidad)
        goles2 = randint(0, posibilidad)
        if equipo1 == lda:
            goles1 = randint(0,posibilidad +1)
        if equipo2 == lda:
            goles2 = randint(0,posibilidad +1)



        print(equipo2.nombre + " " + str(goles2) + " " + equipo1.nombre + " " + str(goles1))
        print(equipo2.nombre + " " + str(goles2+goles2global) + " " + equipo1.nombre + " " + str(goles1+goles1global) + " GLOBAL")

        equipo1.golFavor += goles1
        equipo1.golContra += goles2
        equipo2.golFavor += goles2
        equipo2.golContra += goles1
        equipo1.golDiferencia = equipo1.golFavor - equipo1.golContra
        equipo2.golDiferencia = equipo2.golFavor - equipo2.golContra
        if goles1 > goles2:
            equipo1.puntos += 3
        elif goles1 == goles2:
            equipo1.puntos += 1
            equipo2.puntos += 1
        elif goles2 > goles1:
            equipo2.puntos += 3

        if goles1 + goles1global > goles2 + goles2global:
            listaEquipos.remove(equipo2)
            tabla.remove(equipo2)
            finalista= equipo1
            mensajeExtra += (equipo1.nombre + " avanza a la final. ")
        elif goles2 +goles2global > goles1 + goles1global:
            listaEquipos.remove(equipo1)
            tabla.remove(equipo1)
            finalista = equipo2
            mensajeExtra += (equipo2.nombre + " avanza a la final. ")
        elif goles2 +goles2global ==  goles1 + goles1global:
            if goles2global > goles1:
                listaEquipos.remove(equipo2)
                tabla.remove(equipo2)
                finalista = equipo1
                mensajeExtra +=  (equipo1.nombre + " avanza a la final por gol visitante. ")
            elif goles2global < goles1:
                listaEquipos.remove(equipo1)
                tabla.remove(equipo1)
                finalista = equipo2
                mensajeExtra +=  (equipo2.nombre + " avanza a la final por gol visitante. ")
            elif goles2global == goles1:
                ganador = randint(1,2)
                if ganador == 1:
                    listaEquipos.remove(equipo2)
                    tabla.remove(equipo2)
                    finalista = equipo1
                    mensajeExtra +=  (equipo1.nombre + " avanza a la final por penales. ")
                elif ganador == 2:
                    listaEquipos.remove(equipo1)
                    tabla.remove(equipo1)
                    finalista = equipo2
                    mensajeExtra +=  (equipo2.nombre + " avanza a la final por penales. ")
        if numSerie == 1:
            serie1 = [[equipo1, goles1], [equipo2, goles2], 1, 2]
            global1Serie1 = goles1 + goles1global
            global2Serie1 = goles2 + goles2global
            finalista1 = finalista
        elif numSerie == 2:
            serie2 = [[equipo1, goles1], [equipo2, goles2], 2, 2]
            global1Serie2 = goles1 + goles1global
            global2Serie2 = goles2 + goles2global
            finalista2 = finalista

    return goles1, goles2

def finales(serie):
    global serie1, fecha, campeonLiguilla, global1Serie1, global2Serie1, mensajeExtra
    equipo1 = serie[0][0]
    equipo2 = serie[1][0]
    goles1global = serie[0][1]
    goles2global = serie[1][1]
    partido = serie[3]

    posibilidad = 0
    if partido == 1:
        temporal = randint(0, 22)
        if temporal < 15:
            posibilidad = 3
        elif temporal >= 15 and temporal <= 20:
            posibilidad = 5
        elif temporal > 20:
            posibilidad = 7

        goles1 = randint(0, posibilidad)
        goles2 = randint(0, posibilidad)
        if equipo1 == lda:
            goles1 = randint(0, posibilidad +1)
        if equipo2 == lda:
            goles2 = randint(0, posibilidad +1)
        # equipo1.golFavor += goles1
        # equipo1.golContra += goles2
        # equipo2.golFavor += goles2
        # equipo2.golContra += goles1
        # equipo1.golDiferencia = equipo1.golFavor - equipo1.golContra
        # equipo2.golDiferencia = equipo2.golFavor - equipo2.golContra
        # if goles1 > goles2:
        #     equipo1.puntos += 3
        # elif goles1 == goles2:
        #     equipo1.puntos += 1
        #     equipo2.puntos += 1
        # elif goles2 > goles1:
        #     equipo2.puntos += 3
        serie1 = [[equipo1, goles1], [equipo2, goles2],1,2]
        print(equipo1.nombre + " " + str(goles1) + " " + equipo2.nombre + " " + str(goles2))
    elif partido == 2:
        temporal = randint(0, 22)
        if temporal < 15:
            posibilidad = 3
        elif temporal >= 15 and temporal <= 20:
            posibilidad = 5
        elif temporal > 20:
            posibilidad = 7

        goles1 = randint(0, posibilidad)
        goles2 = randint(0, posibilidad)

        print(equipo2.nombre + " " + str(goles2) + " " + equipo1.nombre + " " + str(goles1))
        print(equipo2.nombre + " " + str(goles2 + goles2global) + " " + equipo1.nombre + " " + str(
            goles1 + goles1global) + " GLOBAL")

        equipo1.golFavor += goles1
        equipo1.golContra += goles2
        equipo2.golFavor += goles2
        equipo2.golContra += goles1
        equipo1.golDiferencia = equipo1.golFavor - equipo1.golContra
        equipo2.golDiferencia = equipo2.golFavor - equipo2.golContra
        if goles1 > goles2:
            equipo1.puntos += 3
        elif goles1 == goles2:
            equipo1.puntos += 1
            equipo2.puntos += 1
        elif goles2 > goles1:
            equipo2.puntos += 3

        if goles1 + goles1global > goles2 + goles2global:
            listaEquipos.remove(equipo2)
            tabla.remove(equipo2)
            ganador = equipo1
            mensajeExtra +=  ("¡Felicidades " + equipo1.nombre + ". Campeón Segunda Fase!")
        elif goles2 + goles2global > goles1 + goles1global:
            listaEquipos.remove(equipo1)
            tabla.remove(equipo1)
            ganador = equipo2
            mensajeExtra +=  ("¡Felicidades " + equipo2.nombre + ". Campeón Segunda Fase!")
        elif goles2 + goles2global == goles1 + goles1global:
            if goles2global > goles1:
                listaEquipos.remove(equipo1)
                tabla.remove(equipo1)
                ganador = equipo2
                mensajeExtra +=  ("¡Felicidades " + equipo2.nombre + ". Campeón de la Segunda Fase por gol visitante!")
            elif goles2global < goles1:
                listaEquipos.remove(equipo2)
                tabla.remove(equipo2)
                ganador = equipo1
                mensajeExtra +=  ("¡Felicidades " + equipo1.nombre + ". Campeón de la Segunda Fase por gol visitante!")
            elif goles2global == goles1:
                ganador = randint(1, 2)
                if ganador == 1:
                    listaEquipos.remove(equipo2)
                    tabla.remove(equipo2)
                    ganador = equipo1
                    mensajeExtra +=  ("¡Felicidades" + equipo1.nombre + " .Campeón de la Segunda Fase por penales!")
                elif ganador == 2:
                    listaEquipos.remove(equipo1)
                    tabla.remove(equipo1)
                    ganador = equipo2
                    mensajeExtra +=  ("¡Felicidades" + equipo2.nombre + ". Campeón de la Segunda Fase por penales!")
        serie1 = [[equipo1, goles1], [equipo2, goles2], 1, 2]
        campeonLiguilla = ganador
        global1Serie1 = goles1 + goles1global
        global2Serie1 = goles2 + goles2global
    return goles1, goles2

def granFinal(serie):
    global serie1, campeonTotal, fecha, global1Serie1, global2Serie1, mensajeExtra
    equipo1 = serie[0][0]
    equipo2 = serie[1][0]
    goles1global = serie[0][1]
    goles2global = serie[1][1]
    partido = serie[3]

    posibilidad = 0
    if partido == 1:
        temporal = randint(0, 22)
        if temporal < 15:
            posibilidad = 3
        elif temporal >= 15 and temporal <= 20:
            posibilidad = 5
        elif temporal > 20:
            posibilidad = 7

        goles1 = randint(0, posibilidad)
        goles2 = randint(0, posibilidad)
        if equipo1 == lda:
            goles1 = randint(0, posibilidad +1)
        if equipo2 == lda:
            goles2 = randint(0, posibilidad +1)
        # equipo1.golFavor += goles1
        # equipo1.golContra += goles2
        # equipo2.golFavor += goles2
        # equipo2.golContra += goles1
        # equipo1.golDiferencia = equipo1.golFavor - equipo1.golContra
        # equipo2.golDiferencia = equipo2.golFavor - equipo2.golContra
        # if goles1 > goles2:
        #     equipo1.puntos += 3
        # elif goles1 == goles2:
        #     equipo1.puntos += 1
        #     equipo2.puntos += 1
        # elif goles2 > goles1:
        #     equipo2.puntos += 3
        serie1 = [[equipo1, goles1], [equipo2, goles2],1,2]
        print(equipo1.nombre + " " + str(goles1) + " " + equipo2.nombre + " " + str(goles2))
    elif partido == 2:
        temporal = randint(0, 22)
        if temporal < 15:
            posibilidad = 3
        elif temporal >= 15 and temporal <= 20:
            posibilidad = 5
        elif temporal > 20:
            posibilidad = 7

        goles1 = randint(0, posibilidad)
        goles2 = randint(0, posibilidad)

        print(equipo2.nombre + " " + str(goles2) + " " + equipo1.nombre + " " + str(goles1))
        print(equipo2.nombre + " " + str(goles2 + goles2global) + " " + equipo1.nombre + " " + str(
            goles1 + goles1global) + " GLOBAL")

        equipo1.golFavor += goles1
        equipo1.golContra += goles2
        equipo2.golFavor += goles2
        equipo2.golContra += goles1
        equipo1.golDiferencia = equipo1.golFavor - equipo1.golContra
        equipo2.golDiferencia = equipo2.golFavor - equipo2.golContra
        if goles1 > goles2:
            equipo1.puntos += 3
        elif goles1 == goles2:
            equipo1.puntos += 1
            equipo2.puntos += 1
        elif goles2 > goles1:
            equipo2.puntos += 3

        if goles1 + goles1global > goles2 + goles2global:
            campeonTotal = equipo1
            mensajeExtra +=  ("¡Felicidades " + equipo1.nombre + ". Campeones Torneo de Clausura 2020!")
        elif goles2 + goles2global > goles1 + goles1global:
            campeonTotal = equipo2
            mensajeExtra +=  ("¡Felicidades " + equipo2.nombre + ". Campeones Torneo de Clausura 2020!")
        elif goles2 + goles2global == goles1 + goles1global:
            ganador = randint(1, 2)
            if ganador == 1:
                campeonTotal = equipo1
                mensajeExtra +=  ("¡Felicidades " + equipo1.nombre + ". Campeones Torneo de Clausura 2020 por medio de los Penales!")
            elif ganador == 2:
                campeonTotal = equipo2
                mensajeExtra +=  ("¡Felicidades " + equipo2.nombre + ". Campeones Torneo de Clausura 2020 por medio de los Penales!")
        serie1 = [[equipo1, goles1], [equipo2, goles2], 1, 2]
        global1Serie1 = goles1 + goles1global
        global2Serie1 = goles2 + goles2global
    return goles1, goles2
def updateSemis(serie1,serie2, proxJornada):
    global global1Serie1, global2Serie1,global1Serie2, global2Serie2
    # Serie[0][0] -> primero en la tabla, serie[0][1] -> goles, serie[2] -> numero de serie, serie[3] -> numero de partido
    imgTemp = Image.open('img/Semifinales.png').convert('RGBA')
    fnt = ImageFont.truetype('img/font.ttf', 27)
    fnt1 = ImageFont.truetype('img/font.ttf', 65)
    fnt2 = ImageFont.truetype('img/font.ttf', 35)
    txt = Image.new('RGBA', imgTemp.size, (255, 255, 255, 0))
    if proxJornada:
        guardar = "proximaFecha.png"
    else:
        guardar = "resultados.png"

    d = ImageDraw.Draw(txt)

    #SERIE 1_______________________________________________________________________
    d.text((60, 540), (serie1[0][0]).nombre, font=fnt, fill=(255, 255, 255, 255))
    if fecha != 24:
        d.text((340, 515), (str(serie1[0][1])), font=fnt1, fill=(145, 223, 77, 255))
    else:
        d.text((320, 535), (str(serie1[0][1])), font=fnt2, fill=(145, 223, 77, 255))
        d.text((350, 535), ("("+str(global1Serie1)+")"), font=fnt2, fill=(145, 223, 77, 255))
    imgTemp.paste(serie1[0][0].imagen, (140,447), mask=serie1[0][0].imagen)

    d.text((60, 636), (serie1[1][0]).nombre, font=fnt, fill=(255, 255, 255, 255))
    if fecha != 24:
        d.text((340, 617), (str(serie1[1][1])), font=fnt1, fill=(145, 223, 77, 255))
    else:
        d.text((320, 637), (str(serie1[1][1])), font=fnt2, fill=(145, 223, 77, 255))
        d.text((350, 637), ("("+str(global2Serie1)+")"), font=fnt2, fill=(145, 223, 77, 255))
    imgTemp.paste(serie1[1][0].imagen, (140, 690), mask=serie1[1][0].imagen)
    #SERIE 2_______________________________________________________________________
    d.text((688, 540), (serie2[0][0]).nombre, font=fnt, fill=(255, 255, 255, 255))
    if fecha != 24:
        d.text((595, 515), (str(serie2[0][1])), font=fnt1, fill=(145, 223, 77, 255))
    else:
        d.text((575, 535), (str(serie2[0][1])), font=fnt2, fill=(145, 223, 77, 255))
        d.text((605, 535), ("(" + str(global1Serie2) + ")"), font=fnt2, fill=(145, 223, 77, 255))
    imgTemp.paste(serie2[0][0].imagen, (778, 447), mask=serie2[0][0].imagen)

    d.text((688, 636), (serie2[1][0]).nombre, font=fnt, fill=(255, 255, 255, 255))
    if fecha != 24:
        d.text((595, 617), (str(serie2[1][1])), font=fnt1, fill=(145, 223, 77, 255))
    else:
        d.text((575, 637), (str(serie2[1][1])), font=fnt2, fill=(145, 223, 77, 255))
        d.text((605, 637), ("(" + str(global2Serie2) + ")"), font=fnt2, fill=(145, 223, 77, 255))
    imgTemp.paste(serie2[1][0].imagen, (778, 690), mask=serie2[1][0].imagen)
    out = Image.alpha_composite(imgTemp, txt)
    out.save(guardar)
def updateFinales(proxJornada):
    new_im = Image.new('RGB', (960, 960))
    bandera1 = Image.open('img/Banderas/Finales/' + serie1[0][0].nombre + ".png")
    bandera2 = Image.open('img/Banderas/Finales/' + serie1[1][0].nombre + ".png")
    escudo1 = Image.open('img/Escudos/' + serie1[0][0].nombre + ".png")
    escudo2 = Image.open('img/Escudos/' + serie1[1][0].nombre + ".png")
    new_im.paste(bandera1, (-47, -100), mask=bandera1)
    new_im.paste(bandera2, (626, -100), mask=bandera2)
    imgTemp = Image.open('img/Finales.png').convert('RGBA')
    new_im.paste(imgTemp, (0, 0), mask=imgTemp)
    new_im.paste(escudo1, (80, 550), mask=escudo1)
    new_im.paste(escudo2, (650, 550), mask=escudo2)

    fnt1 = ImageFont.truetype('img/font.ttf', 105)
    fnt2 = ImageFont.truetype('img/font.ttf', 65)
    txt = Image.new('RGBA', imgTemp.size, (255, 255, 255, 0))
    if proxJornada:
        guardar = "proximaFecha.png"
    else:
        guardar = "resultados.png"

    d = ImageDraw.Draw(txt)
    if fecha != 26:
        d.text((180, 400), (str(serie1[0][1])), font=fnt1, fill=(150, 132, 108, 255))
    else:
        d.text((140, 400), (str(serie1[0][1])), font=fnt2, fill=(150, 132, 108, 255))
        d.text((180, 400), ("(" + str(global1Serie1) + ")"), font=fnt2, fill=(150, 132, 108, 255))

    if fecha != 26:
        d.text((750, 400), (str(serie1[1][1])), font=fnt1, fill=(150, 132, 108, 255))
    else:
        d.text((710, 400), (str(serie1[1][1])), font=fnt2, fill=(150, 132, 108, 255))
        d.text((750, 400), ("(" + str(global2Serie1) + ")"), font=fnt2, fill=(150, 132, 108, 255))

    new_im = new_im.convert('RGBA')
    out = Image.alpha_composite(new_im, txt)
    out.save(guardar)
def updateGranFinal(proxJornada):
    new_im = Image.new('RGB', (960, 960))
    bandera1=  Image.open('img/Banderas/Finales/' + serie1[0][0].nombre + ".png")
    bandera2 = Image.open('img/Banderas/Finales/' + serie1[1][0].nombre + ".png")
    escudo1 = Image.open('img/Escudos/' + serie1[0][0].nombre + ".png")
    escudo2 = Image.open('img/Escudos/' + serie1[1][0].nombre + ".png")
    new_im.paste(bandera1,(-47,-100),mask = bandera1)
    new_im.paste(bandera2,(626,-100),mask = bandera2)
    imgTemp = Image.open('img/GranFinal.png').convert('RGBA')
    new_im.paste(imgTemp,(0,0),mask=imgTemp)
    new_im.paste(escudo1,(80,550),mask=escudo1)
    new_im.paste(escudo2, (650, 550), mask=escudo2)

    fnt1 = ImageFont.truetype('img/font.ttf', 105)
    fnt2 = ImageFont.truetype('img/font.ttf', 65)
    txt = Image.new('RGBA', imgTemp.size, (255, 255, 255, 0))
    if proxJornada:
        guardar = "proximaFecha.png"
    else:
        guardar = "resultados.png"

    d = ImageDraw.Draw(txt)
    if fecha != 28:
        d.text((180, 400), (str(serie1[0][1])), font=fnt1, fill=(150, 132, 108, 255))
    else:
        d.text((140, 400), (str(serie1[0][1])), font=fnt2, fill=(150, 132, 108, 255))
        d.text((180, 400), ("(" + str(global1Serie1) + ")"), font=fnt2, fill=(150, 132, 108, 255))

    if fecha != 28:
        d.text((750, 400), (str(serie1[1][1])), font=fnt1, fill=(150, 132, 108, 255))
    else:
        d.text((710, 400), (str(serie1[1][1])), font=fnt2, fill=(150, 132, 108, 255))
        d.text((750, 400), ("(" + str(global2Serie1) + ")"), font=fnt2, fill=(150, 132, 108, 255))

    new_im = new_im.convert('RGBA')
    out = Image.alpha_composite(new_im, txt)
    out.save(guardar)

    if fecha == 28:
        new_im = Image.new('RGB', (960, 960))
        bandera1 = Image.open('img/Banderas/Finales/' + campeonTotal.nombre + ".png")
        escudo1 = Image.open('img/Campeones/' + campeonTotal.nombre + ".png")
        confetti = Image.open('img/Campeones/confetti.png')
        trofeo = Image.open('img/Campeones/trofeo.png')
        new_im.paste(bandera1, (-47, -100), mask=bandera1)
        new_im.paste(bandera1, (626, -100), mask=bandera1)

        imgTemp = Image.open('img/Campeones/campeones.png').convert('RGBA')
        new_im.paste(imgTemp, (0, 0), mask=imgTemp)
        new_im.paste(escudo1,(250,90), mask=escudo1)
        new_im.paste(confetti,(0,0),mask=confetti)
        new_im.paste(trofeo,(0,0),mask=trofeo)
        new_im.save("proximaFecha.png")


def updateTabla(listaEquipos):
    global tabla, fecha
    tabla = listaEquipos[:]
    tabla.sort(key=lambda x: (x.puntos,x.golDiferencia,x.golFavor), reverse=True)
    for x in range(0,len(tabla)):
        print(str(x+1)+". " + tabla[x].nombre + " ____________ " + str(tabla[x].puntos) + " pts"+ "   " + str(tabla[x].golDiferencia)+ " GD")

    imgTemp = Image.open('img/posiciones.png').convert('RGBA')
    fnt = ImageFont.truetype('img/font.ttf', 27)
    txt = Image.new('RGBA', imgTemp.size, (255, 255, 255, 0))
    d = ImageDraw.Draw(txt)
    x = 150
    y = 310
    if fecha <= 23:
        for i in tabla:
            d.text((x, y), i.nombre, font=fnt, fill=(255, 255, 255, 255))
            d.text((x+450, y), str(fecha), font=fnt, fill=(255, 255, 255, 255))
            d.text((x + 511, y), str(i.golFavor), font=fnt, fill=(255, 255, 255, 255))
            d.text((x + 577, y), str(i.golDiferencia), font=fnt, fill=(255, 255, 255, 255))
            d.text((x + 647, y), str(i.puntos), font=fnt, fill=(255, 255, 255, 255))
            y += 39
        out = Image.alpha_composite(imgTemp, txt)
        out.save("tabla.png")

lda = equipo("Alajuelense")
lda.imagen = Image.open('img/liga3.png')
saprissa = equipo("Saprissa")
saprissa.imagen = Image.open('img/saprissa3.png')
csh = equipo("Herediano")
csh.imagen = Image.open('img/heredia3.png')
csc = equipo("Cartaginés")
csc.imagen = Image.open('img/cartago3.png')
pz = equipo("Pérez Zeledón")
pz.imagen = Image.open('img/pz3.png')
sc = equipo("San Carlos")
sc.imagen = Image.open('img/adsc3.png')
ucr = equipo("La U")
ucr.imagen = Image.open('img/ucr3.png')
guadalupe = equipo("Guadalupe FC")
guadalupe.imagen = Image.open('img/guadalupe3.png')
santos = equipo("Santos")
santos.imagen = Image.open('img/santos3.png')
limon = equipo("Limón")
limon.imagen = Image.open('img/limon3.png')
jicaral = equipo("Jicaral")
jicaral.imagen = Image.open('img/jicaral3.png')
grecia = equipo("Grecia")
grecia.imagen = Image.open('img/grecia3.png')
fechas =[
    [[csc,santos],[grecia,jicaral],[guadalupe,lda],[pz,limon],[sc,saprissa],[ucr,csh]],
    [[jicaral,csc],[csh,grecia],[limon,lda],[santos,guadalupe],[saprissa,pz],[ucr,sc]],
    [[lda,csh],[jicaral,ucr],[csc,sc],[grecia,limon],[guadalupe,pz],[santos,saprissa]],
    [[csh,jicaral],[limon,santos],[pz,lda],[sc,grecia],[saprissa,guadalupe],[ucr,csc]],
    [[lda,saprissa],[jicaral,sc],[csc,csh],[grecia,ucr],[guadalupe,limon],[santos,pz]],
    [[grecia,lda],[csh,limon],[pz,csc],[sc,santos],[saprissa,jicaral],[ucr,guadalupe]],
    [[lda,ucr],[jicaral,pz],[csh,guadalupe],[limon,sc],[santos,grecia],[saprissa,csc]],
    [[lda,santos],[csc,grecia],[guadalupe,jicaral],[limon,saprissa],[pz,ucr],[sc,csh]],
    [[jicaral,santos],[csc,lda],[grecia,guadalupe],[csh,saprissa],[sc,pz],[ucr,limon]],
    [[lda,sc],[guadalupe,csc],[limon,jicaral],[pz,grecia],[santos,csh],[saprissa,ucr]],
    [[jicaral,lda],[csc,limon],[grecia,saprissa],[csh,pz],[sc,guadalupe],[ucr,santos]],
    [[lda,guadalupe],[jicaral,grecia],[csh,ucr],[limon,pz],[santos,csc],[saprissa,sc]],
    [[lda,limon],[csc,jicaral],[grecia,csh],[guadalupe,santos],[pz,saprissa],[sc,ucr]],
    [[csh,lda],[limon,grecia],[pz,guadalupe],[sc,csc],[saprissa,santos],[ucr,jicaral]],
    [[lda,pz],[jicaral,csh],[csc,ucr],[grecia,sc],[guadalupe,saprissa],[santos,limon]],
    [[csh,csc],[limon,guadalupe],[pz,santos],[sc,jicaral],[saprissa,lda],[ucr,grecia]],
    [[lda,grecia],[jicaral,saprissa],[csc,pz],[guadalupe,ucr],[limon,csh],[santos,sc]],
    [[csc,saprissa],[grecia,santos],[guadalupe,csh],[pz,jicaral],[sc,limon],[ucr,lda]],
    [[jicaral,guadalupe],[grecia,csc],[csh,sc],[santos,lda],[saprissa,limon],[ucr,pz]],
    [[lda,csc],[guadalupe,grecia],[limon,ucr],[pz,sc],[santos,jicaral],[saprissa,csh]],
    [[jicaral,limon],[csc,guadalupe],[grecia,pz],[csh,santos],[sc,lda],[ucr,saprissa]],
    [[lda,jicaral],[guadalupe,sc],[limon,csc],[pz,csh],[santos,ucr],[saprissa,grecia]]
    ]
def jornadasFotos(fechas, jornada):
    global resultados
    base = Image.open('img/resultados.png').convert('RGBA')
    base2 = Image.open('img/proximaFecha.png').convert('RGBA')
    txt = Image.new('RGBA', base.size, (255, 255, 255, 0))
    txt2 = Image.new('RGBA', base.size, (255, 255, 255, 0))
    fnt = ImageFont.truetype('img/font.ttf', 25)
    fnt1 = ImageFont.truetype('img/font.ttf', 65)
    d = ImageDraw.Draw(txt)
    d2 = ImageDraw.Draw(txt2)
    x= 180
    y=260
    cont = 0
    for partido in fechas[jornada]:
        d.text((x, y), partido[0].nombre, font=fnt, fill=(0, 0, 0, 160))
        d.text((x+391, y), partido[1].nombre, font=fnt, fill=(0, 0, 0, 160))
        d.text((x + 240, y-23), str(resultados[cont][0]), font=fnt1, fill=(145, 223, 77, 255))
        d.text((x + 330, y-23), str(resultados[cont][1]), font=fnt1, fill=(145, 223, 77, 255))
        base.paste(partido[0].imagen, (x-75, y-20), mask =partido[0].imagen )
        base.paste(partido[1].imagen, (x + 615, y-20),mask =partido[1].imagen)
        y+= 85
        cont += 1
    fnt3 = ImageFont.truetype('img/font.ttf', 35)
    d.text((338, 93), str(fecha+1), font=fnt3, fill=(255, 255, 255, 255))
    out = Image.alpha_composite(base, txt)
    out.save('resultados.png')
    x = 180
    y = 260
    if jornada < 21:
        for partido in fechas[jornada+1]:
            d2.text((x, y), partido[0].nombre, font=fnt, fill=(0, 0, 0, 160))
            d2.text((x+391, y), partido[1].nombre, font=fnt, fill=(0, 0, 0, 160))
            d2.text((x + 240, y-23), "-", font=fnt1, fill=(145, 223, 77, 255))
            d2.text((x + 330, y-23), "-", font=fnt1, fill=(145, 223, 77, 255))
            base2.paste(partido[0].imagen, (x-75, y-20), mask =partido[0].imagen )
            base2.paste(partido[1].imagen, (x + 615, y-20),mask =partido[1].imagen)
            y+= 85
            cont += 1
        out = Image.alpha_composite(base2, txt2)
        out.save('proximaFecha.png')


def readXML():
    global fecha, serie1,serie2, campeonLiguilla,campeonRegular,campeonTotal
    tree = ET.parse('datos.xml')
    root = tree.getroot()
    fecha = int(root[0].text)
    for x in listaEquipos:
        if (root[17]).text == x.nombre:
            campeonRegular = x
    for x in listaEquipos:
        if (root[18]).text == x.nombre:
            campeonLiguilla = x
    for x in listaEquipos:
        if (root[19]).text == x.nombre:
            campeonTotal = x
    cont = 1
    for x in listaEquipos:
        x.puntos = int(root[cont][0].text)
        x.golFavor = int(root[cont][1].text)
        x.golContra = int(root[cont][2].text)
        x.golDiferencia = int(root[cont][3].text)
        x.derrotas = int(root[cont][4].text)
        cont += 1
    if fecha == 22 or fecha == 23:
        for x in listaEquipos:
            if (root[13][0]).text == x.nombre:
                equipo1serie1 = x
        for x in listaEquipos:
            if(root[13][1]).text == x.nombre:
                equipo2serie1 = x
        for x in listaEquipos:
            if (root[14][0]).text == x.nombre:
                equipo1serie2 = x
        for x in listaEquipos:
            if (root[14][1]).text == x.nombre:
                equipo2serie2 = x
        serie1 = [[equipo1serie1,int(root[13][2].text)],[equipo2serie1,int(root[13][3].text)],1,int(root[13][4].text)]
        serie2 = [[equipo1serie2, int(root[14][2].text)], [equipo2serie2, int(root[14][3].text)], 2,
                  int(root[14][4].text)]
    if fecha == 24 or fecha == 25:
        for x in listaEquipos:
            if (root[15][0]).text == x.nombre:
                equipo1serie1 = x
        for x in listaEquipos:
            if(root[15][1]).text == x.nombre:
                equipo2serie1 = x
        serie1 = [[equipo1serie1, int(root[15][2].text)], [equipo2serie1, int(root[15][3].text)], 1,
                  int(root[15][4].text)]
    if fecha == 26 or fecha == 27:
        for x in listaEquipos:
            if (root[16][0]).text == x.nombre:
                equipo1serie1 = x
        for x in listaEquipos:
            if(root[16][1]).text == x.nombre:
                equipo2serie1 = x
        serie1 = [[equipo1serie1, int(root[16][2].text)], [equipo2serie1, int(root[16][3].text)], 1,
                  int(root[16][4].text)]

def updateXml():
    global  campeonTotal,campeonRegular,campeonLiguilla, serie1,serie2, semi1,semi2, finalista1, finalista2
    global fecha
    tree = ET.parse('datos.xml')
    root = tree.getroot()
    for f in root.iter('fecha'):
        f.text = str(fecha)
    if campeonRegular != None and campeonRegular != "":
        for cR in root.iter('campeonRegular'):
            cR.text = campeonRegular.nombre
    if campeonLiguilla != None and campeonLiguilla != "":
        for cL in root.iter('campeonLiguilla'):
            cL.text = campeonLiguilla.nombre
    if campeonTotal != None and campeonTotal != "":
        for cT in root.iter('campeonTotal'):
            cT.text = campeonTotal.nombre
    for equipo in root.findall(".//*[@nombre = 'lda']"):
        equipo[0].text = str(lda.puntos)
        equipo[1].text = str(lda.golFavor)
        equipo[2].text = str(lda.golContra)
        equipo[3].text = str(lda.golDiferencia)
        equipo[4].text = str(lda.derrotas)
    for equipo in root.findall(".//*[@nombre = 'saprissa']"):
        equipo[0].text = str(saprissa.puntos)
        equipo[1].text = str(saprissa.golFavor)
        equipo[2].text = str(saprissa.golContra)
        equipo[3].text = str(saprissa.golDiferencia)
        equipo[4].text = str(saprissa.derrotas)
    for equipo in root.findall(".//*[@nombre = 'csh']"):
        equipo[0].text = str(csh.puntos)
        equipo[1].text = str(csh.golFavor)
        equipo[2].text = str(csh.golContra)
        equipo[3].text = str(csh.golDiferencia)
        equipo[4].text = str(csh.derrotas)
    for equipo in root.findall(".//*[@nombre = 'csc']"):
        equipo[0].text = str(csc.puntos)
        equipo[1].text = str(csc.golFavor)
        equipo[2].text = str(csc.golContra)
        equipo[3].text = str(csc.golDiferencia)
        equipo[4].text = str(csc.derrotas)
    for equipo in root.findall(".//*[@nombre = 'pz']"):
        equipo[0].text = str(pz.puntos)
        equipo[1].text = str(pz.golFavor)
        equipo[2].text = str(pz.golContra)
        equipo[3].text = str(pz.golDiferencia)
        equipo[4].text = str(pz.derrotas)
    for equipo in root.findall(".//*[@nombre = 'sc']"):
        equipo[0].text = str(sc.puntos)
        equipo[1].text = str(sc.golFavor)
        equipo[2].text = str(sc.golContra)
        equipo[3].text = str(sc.golDiferencia)
        equipo[4].text = str(sc.derrotas)
    for equipo in root.findall(".//*[@nombre = 'guadalupe']"):
        equipo[0].text = str(guadalupe.puntos)
        equipo[1].text = str(guadalupe.golFavor)
        equipo[2].text = str(guadalupe.golContra)
        equipo[3].text = str(guadalupe.golDiferencia)
        equipo[4].text = str(guadalupe.derrotas)
    for equipo in root.findall(".//*[@nombre = 'santos']"):
        equipo[0].text = str(santos.puntos)
        equipo[1].text = str(santos.golFavor)
        equipo[2].text = str(santos.golContra)
        equipo[3].text = str(santos.golDiferencia)
        equipo[4].text = str(santos.derrotas)
    for equipo in root.findall(".//*[@nombre = 'limon']"):
        equipo[0].text = str(limon.puntos)
        equipo[1].text = str(limon.golFavor)
        equipo[2].text = str(limon.golContra)
        equipo[3].text = str(limon.golDiferencia)
        equipo[4].text = str(limon.derrotas)
    for equipo in root.findall(".//*[@nombre = 'jicaral']"):
        equipo[0].text = str(jicaral.puntos)
        equipo[1].text = str(jicaral.golFavor)
        equipo[2].text = str(jicaral.golContra)
        equipo[3].text = str(jicaral.golDiferencia)
        equipo[4].text = str(jicaral.derrotas)
    for equipo in root.findall(".//*[@nombre = 'grecia']"):
        equipo[0].text = str(grecia.puntos)
        equipo[1].text = str(grecia.golFavor)
        equipo[2].text = str(grecia.golContra)
        equipo[3].text = str(grecia.golDiferencia)
        equipo[4].text = str(grecia.derrotas)
    for equipo in root.findall(".//*[@nombre = 'ucr']"):
        equipo[0].text = str(ucr.puntos)
        equipo[1].text = str(ucr.golFavor)
        equipo[2].text = str(ucr.golContra)
        equipo[3].text = str(ucr.golDiferencia)
        equipo[4].text = str(ucr.derrotas)
    if fecha == 22:
        for serie in root.findall(".//*[@Serie = '1']"):
            serie[0].text = str(tabla[0].nombre)
            serie[1].text = str(tabla[3].nombre)
            serie[2].text = str(0)
            serie[3].text = str(0)
            serie[4].text = str(1)
        for serie in root.findall(".//*[@Serie = '2']"):
            serie[0].text = str(tabla[1].nombre)
            serie[1].text = str(tabla[2].nombre)
            serie[2].text = str(0)
            serie[3].text = str(0)
            serie[4].text = str(1)
    if fecha == 23:
        for serie in root.findall(".//*[@Serie = '1']"):
            serie[0].text = str(serie1[0][0].nombre)
            serie[1].text = str(serie1[1][0].nombre)
            serie[2].text = str(semi1[0])
            serie[3].text = str(semi1[1])
            serie[4].text = str(2)
        for serie in root.findall(".//*[@Serie = '2']"):
            serie[0].text = str(serie2[0][0].nombre)
            serie[1].text = str(serie2[1][0].nombre)
            serie[2].text = str(semi2[0])
            serie[3].text = str(semi2[1])
            serie[4].text = str(2)
    if fecha == 24:
        for serie in root.findall(".//*[@Serie = 'finales']"):
            serie[0].text= str(finalista1.nombre)
            serie[1].text = str(finalista2.nombre)
            serie[2].text = str(0)
            serie[3].text = str(0)
            serie[4].text = str(1)
    if fecha == 25:
        for serie in root.findall(".//*[@Serie = 'finales']"):
            serie[0].text = str(serie1[0][0].nombre)
            serie[1].text = str(serie1[1][0].nombre)
            serie[2].text = str(semi1[0])
            serie[3].text = str(semi1[1])
            serie[4].text = str(2)
    if fecha == 26:
        for serie in root.findall(".//*[@Serie = 'granFinal']"):
            serie[0].text = str(campeonRegular.nombre)
            serie[1].text = str(campeonLiguilla.nombre)
            serie[2].text = str(0)
            serie[3].text = str(0)
            serie[4].text = str(1)
    if fecha == 27:
        for serie in root.findall(".//*[@Serie = 'granFinal']"):
            serie[0].text = str(serie1[0][0].nombre)
            serie[1].text = str(serie1[1][0].nombre)
            serie[2].text = str(semi1[0])
            serie[3].text = str(semi1[1])
            serie[4].text = str(2)

    tree.write('datos.xml')

readXML()

updateTabla(listaEquipos)
if fecha < 22:
    print("Fecha " + str(fecha+1) + " ______________________")
    jornada(fechas[fecha])
    jornadasFotos(fechas,fecha)
    print("__________________________________________________________________")
    fecha += 1
    updateTabla(listaEquipos)
    if fecha == 22:
        campeonRegular=tabla[0]
        print(campeonRegular.nombre + " CAMPEON REGULAR")
        tabla = tabla[0:4]
        #Tabla[0] -> primero en la tabla, serie[0][1] -> goles global, serie[2] -> numero de serie, serie[3] -> numero de partido
        serie1=[[tabla[0],'-'],[tabla[3],'-'],1,0]
        serie2=[[tabla[1],'-'],[tabla[2],'-'],2,0]
        updateSemis(serie1,serie2,True)
elif fecha >= 22 and fecha <24:
    fecha += 1
    print("Semis Serie 1____________________________________________________")
    semi1 = semifinales(serie1)
    print("Semis Serie 2____________________________________________________")
    semi2 = semifinales(serie2)
    updateSemis(serie1,serie2,False)
    if fecha == 24:
      serie1 = [[finalista1,'-'],[finalista2,'-'],1,0]
      updateFinales(True)
elif fecha >= 24 and fecha <26:
    fecha += 1
    print("Finales________________")
    semi1 = finales(serie1)
    updateFinales(False)
    if fecha == 26:
        serie1 = [[campeonRegular,'-'],[campeonLiguilla,'-'],1,0]
        updateGranFinal(True)
elif fecha >=  26 and fecha<28:
    if campeonTotal == "" or campeonTotal == None:
        fecha += 1
        print("Gran Final_______________")
        semi1 = granFinal(serie1)
        updateGranFinal(False)
        if fecha == 28:
            print(campeonTotal.nombre + " CAMPEON TORNEO CLAUSRA EN GRAN FINAL")
if campeonRegular == campeonLiguilla and campeonRegular != None and campeonRegular != "":
    campeonTotal = campeonLiguilla
    print(campeonTotal.nombre + " CAMPEON TORNEO CLAUSURA")
    new_im = Image.new('RGB', (960, 960))
    bandera1 = Image.open('img/Banderas/Finales/' + campeonTotal.nombre + ".png")
    escudo1 = Image.open('img/Campeones/' + campeonTotal.nombre + ".png")
    confetti = Image.open('img/Campeones/confetti.png')
    trofeo = Image.open('img/Campeones/trofeo.png')
    new_im.paste(bandera1, (-47, -100), mask=bandera1)
    new_im.paste(bandera1, (626, -100), mask=bandera1)

    imgTemp = Image.open('img/Campeones/campeones.png').convert('RGBA')
    new_im.paste(imgTemp, (0, 0), mask=imgTemp)
    new_im.paste(escudo1, (250, 90), mask=escudo1)
    new_im.paste(confetti, (0, 0), mask=confetti)
    new_im.paste(trofeo, (0, 0), mask=trofeo)
    new_im.save("proximaFecha.png")

#PUBLICACIONES_____________________________________________________________________________________________________________________________
# if fecha <= 28:
#     fotoTabla = graph.put_photo(
#         image=open('tabla.png','rb'),
#         no_story=True,
#         published=False
#     )
#     fotoProximaJornada = graph.put_photo(
#         image=open('proximaFecha.png','rb'),
#         no_story=True,
#         published=False
#     )
#     if fecha <= 22:
#         mensaje = "Resultados Fecha " +str(fecha)
#     elif fecha == 23:
#         mensaje = "Resultados Semifinales Ida. " + mensajeExtra
#     elif fecha == 24:
#         mensaje = "Resultados Semifinales Vuelta. " + mensajeExtra
#     elif fecha == 25:
#         mensaje = "Resultados Final Ida. " + mensajeExtra
#     elif fecha == 26:
#         mensaje = "Resultados Final Vuelta. " + mensajeExtra
#     elif fecha == 27:
#         mensaje = "Resultados Gran Final Ida. " + mensajeExtra
#     elif fecha == 28:
#         mensaje = "Resultados Gran Final Vuelta. Felicidades " + campeonTotal.nombre + " Campeón Torneo Clausura Liga Botmerica 2020"
#     post = graph.put_photo(image=open('resultados.png', 'rb'), message=mensaje)
#     graph.put_object(post['post_id'], connection_name='comments', attachment_id=fotoProximaJornada['id'], message='Próxima Fecha')
#     print (mensaje)
#     if fecha <= 22:
#         graph.put_object(post['post_id'], connection_name='comments', attachment_id=fotoTabla['id'],
#                          message='Tabla de Posiciones Liga Botmerica')


updateXml();