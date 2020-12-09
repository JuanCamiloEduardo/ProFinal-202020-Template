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
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import mergesort as mg
from DISClib.DataStructures import listiterator as it
from DISClib.Algorithms.Graphs import scc
from DISClib.Algorithms.Graphs import dijsktra as djk
from DISClib.Utils import error as error
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
    analyzer["taxids"]=m.newMap(numelements=37,maptype="CHAINING",loadfactor=0.4,comparefunction=comparecompany)
    return analyzer
# ==============================
# Funciones Helper
# ==============================
def addtrip(analyzer,trip):
    lt.addLast( analyzer["lista"],trip)       
# ==============================
# Funciones de Comparacion
# ==============================
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
# ==============================
# Funciones requerimientos
# ==============================ç
def reportegeneral(analyzer,parametrom,parametron):
    listaviajes= analyzer["lista"]
    lista=[]
    companias=[]
    for i in range (lt.size(listaviajes)+1):
        taxiid=lt.getElement(listaviajes,i)["taxi_id"]
        compania=lt.getElement(listaviajes,i)["company"]
        if compania=="":
            compania="independent owner"
        if compania not in companias:
            companias.append(compania)
        
        if taxiid not in lista:
            lista.append(taxiid)

        addCompany(analyzer,compania,taxiid,lt.getElement(listaviajes,i))
        addtaxid(analyzer,taxiid)
    rankingm=lt.newList("ARRAY_LIST")
    rankingn=lt.newList("ARRAY_LIST")
    for i in companias:
        compania=m.get(analyzer["mapcompany"],i)
        lt.addLast(rankingm,compania)
        lt.addLast(rankingn,compania)
    mg.mergesort(rankingm,greater_company)
    mg.mergesort(rankingn,greater_company_taxis)

    rankingm=lt.subList(rankingm,1,parametrom+1)
    rankingn=lt.subList(rankingn,1,parametron+1)
    return len(lista),len(companias),rankingm,rankingn
def addCompany(analyzer, company_name,taxiid,trip):
    exist_company = m.contains( analyzer['mapcompany'],company_name)
    if exist_company:
        entry = m.get( analyzer['mapcompany'],company_name)
        entry= me.getValue(entry)
        entry["Cantidad de servicios: "]+=1
        if not m.contains(analyzer["taxids"],taxiid):
            entry["taxis: "]+=1
            m.remove(analyzer["taxids"],taxiid)
    else:
        company = Newcompany(company_name)
        m.put( analyzer['mapcompany'], company_name, company)
        entry = m.get( analyzer['mapcompany'],company_name)
        entry= me.getValue(entry)
        if not m.contains(analyzer["taxids"],taxiid):
            entry["taxis: "]+=1
            m.remove(analyzer["taxids"],taxiid)
       
def Newcompany(name):
    company = {'Compañía: ': "", "Cantidad de servicios: " : 0, "taxis: ":0}
    company['Compañía: '] = name
    company['Cantidad de servicios: '] = 1
    company['taxis: '] = 0
    return company

def addtaxid(analyzer, taxi_id):
    exist_taxi_id = m.contains( analyzer['taxids'],taxi_id)
    if not exist_taxi_id:
        taxiid = Newtaxi_id(taxi_id)
        m.put( analyzer['taxids'], taxi_id, taxiid)
def Newtaxi_id(taxi_id):
    taxi = {'id: ':""}
    taxi['id: '] = taxi_id
    return taxi