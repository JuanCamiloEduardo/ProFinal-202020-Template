"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * Contribución de:
 *
 * Dario Correal
 *
 """
import config
from DISClib.ADT.graph import gr
from DISClib.ADT import map as m
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as op
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import mergesort as mg
from DISClib.DataStructures import listiterator as it
from DISClib.Algorithms.Graphs import scc
from DISClib.Algorithms.Graphs import dijsktra as djk
from DISClib.Utils import error as error
from DISClib.ADT import stack as stack
assert config

"""
En este archivo definimos los TADs que vamos a usar y las operaciones
de creacion y consulta sobre las estructuras de datos.
"""

# -----------------------------------------------------
#                       API
# -----------------------------------------------------

# Funciones para agregar informacion al grafo

# ==============================
# Funciones de consulta
# ==============================
def newAnalyzer():
    """ Inicializa el analizador
    """
    analyzer = {
               "lista":None,
               "mapcompany":None,
               "taxids":None,
                }
    analyzer["lista"]=lt.newList("ARRAY_LIST")
    analyzer["mapcompany"]=m.newMap(numelements=37,maptype="CHAINING",loadfactor=0.4,comparefunction=comparecompany)
    analyzer["MapaId"]=op.newMap(omaptype='RBT', comparefunction=compareDates)
    analyzer["taxids"]=m.newMap(numelements=37,maptype="CHAINING",loadfactor=0.4,comparefunction=comparecompany)
    analyzer['grafo'] = gr.newGraph(datastructure='ADJ_LIST',
                                          directed=True,
                                          size=300,
                                          comparefunction=comparecompany)
    return analyzer
# ==============================
# Funciones Helper
# ==============================
def addtrip(analyzer,trip):
    lt.addLast( analyzer["lista"],trip)

def addMap(analyzer,trip):    
    if trip["trip_total"]!="" and trip["trip_miles"]!="" and float(trip["trip_total"])>0 and float(trip["trip_miles"])>0 :
        llave=trip["trip_start_timestamp"]
        llave=str(llave[0:10])
        valor1=trip["taxi_id"]
        valor2=float(trip["trip_total"])
        valor3=float(trip["trip_miles"])
        Lista=lt.newList("ARRAY_LIST")
        if op.contains(analyzer["MapaId"],llave[0:10])==True:
            Valor=op.get(analyzer["MapaId"],llave[0:10])
            Valor=Valor["value"]
            Lista3=lt.newList("ARRAY_LIST")
            lt.addFirst(Lista3,valor1)
            lt.addLast(Lista3,valor2)
            lt.addLast(Lista3,valor3)
            lt.addLast(Valor,Lista3)
        else:
            Lista2=lt.newList("ARRAY_LIST")
            lt.addFirst(Lista2,valor1)
            lt.addLast(Lista2,valor2)
            lt.addLast(Lista2,valor3)
            lt.addFirst(Lista,Lista2)
            op.put(analyzer["MapaId"],llave[0:10],Lista)       
# ==============================
# Funciones de Comparacion
# ==============================
def compareDates(date1, date2):
    """
    Compara dos ids de libros, id es un identificador
    y entry una pareja llave-valor
    """
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1

def comparecompany(keyname,company):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    compentry = me.getKey(company)
    if (keyname == compentry):
        return 0
    elif (keyname > compentry):
        return 1
    else:
        return -1
def greater_company(element1, element2):
    if (element1["value"]["Cantidad de servicios: "]) > (element2["value"]["Cantidad de servicios: "]):
        return True
    return False
def greater_company_taxis(element1, element2):
    if (element1["value"]["taxis: "]) > (element2["value"]["taxis: "]):
        return True

def GreaterTaxis(element1, element2):
    Longitud1=len(element1)
    Longitud2=len(element2)
    Buscador1=element1.find("_: ")
    Buscador2=element2.find("_: ")
    Value1=element1[Buscador1+3:Longitud1]
    Value2=element2[Buscador2+3:Longitud2]
    Value1=float(Value1)
    Value2=float(Value2)
    if Value1>Value2:
        return True
    return False
# ==============================
# Funciones requerimientos
# ==============================ç




