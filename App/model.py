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
from DISClib.ADT import orderedmap as op
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
               "MapaId":None,
                }
    analyzer["lista"]=lt.newList("ARRAY_LIST")
    analyzer["mapcompany"]=m.newMap(numelements=37,maptype="CHAINING",loadfactor=0.4,comparefunction=comparecompany)
    analyzer["MapaId"]=op.newMap(omaptype='RBT', comparefunction=compareDates)
    analyzer["taxids"]=m.newMap(numelements=37,maptype="CHAINING",loadfactor=0.4,comparefunction=comparecompany)
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
def requerimientoB(analyzer,FechaI,FechaF,FechaO):
    ListaR=op.keys(analyzer["MapaId"],FechaI,FechaF)
    ListaU=op.keys(analyzer["MapaId"],FechaO,FechaO)
    if lt.isEmpty(ListaR)==True:
        OrdenadaR=False
    else:
        PuntosR=Rango(ListaR,analyzer,False)
        OrdenadaR=DiciaLista(PuntosR)
    if lt.isEmpty(ListaU)==True:
        OrdenadaU=False
    else:
        PuntosU=Rango(ListaU,analyzer,FechaO)
        OrdenadaU=DiciaLista(PuntosU)
    ListaFinal=lt.newList("ARRAY_LIST")
    lt.addFirst(ListaFinal,OrdenadaU)
    lt.addLast(ListaFinal,OrdenadaR)
    return ListaFinal
def DiciaLista(PuntosR):
    ListaStr=lt.newList("ARRAY_LIST")
    ListaL=m.keySet(PuntosR)
    for i in range(1+lt.size(ListaL)):
        Llave=lt.getElement(ListaL,i)
        Valor=m.get(PuntosR,Llave)
        Valor=Valor["value"]
        Str=str(Llave)+str("_: ")+str(Valor)
        lt.addLast(ListaStr,Str)
    mg.mergesort(ListaStr,GreaterTaxis)
    return ListaStr

def Rango(ListaR,analyzer,especifica):
    IdTaxis=m.newMap(numelements=37,maptype="CHAINING",loadfactor=0.4,comparefunction=comparecompany)
    if especifica==False:
        for i in range(1,lt.size(ListaR)+1):
            llave=lt.getElement(ListaR,i)
            valor=op.get(analyzer["MapaId"],llave)
            valor=valor["value"]
            for j in range(1,lt.size(valor)+1):
                Dato=lt.getElement(valor,j)
                TaxiId=lt.getElement(Dato,1)
                Precio=float(lt.getElement(Dato,2))
                Millas=float(lt.getElement(Dato,3))
                if m.contains(IdTaxis,TaxiId)==True:
                    Lista4=lt.newList("ARRAY_LIST")
                    viaje=m.get(IdTaxis,TaxiId)
                    viaje=viaje["value"]
                    Dato1=float(lt.getElement(viaje,1))
                    Dato2=float(lt.getElement(viaje,2))
                    Dato3=float(lt.getElement(viaje,3))
                    PrecioTotal=Precio+Dato1
                    MillasTotal=Millas+Dato2
                    TotalViajes=Dato3+1
                    lt.addFirst(Lista4,PrecioTotal)
                    lt.addLast(Lista4,MillasTotal)
                    lt.addLast(Lista4,TotalViajes)
                    m.put(IdTaxis,TaxiId,Lista4)
                else:
                    Lista5=lt.newList("ARRAY_LIST")
                    ViajesTotal=1
                    lt.addFirst(Lista5,Precio)
                    lt.addLast(Lista5,Millas)
                    lt.addLast(Lista5,ViajesTotal)
                    m.put(IdTaxis,TaxiId,Lista5)  
    else:
        valor=op.get(analyzer["MapaId"],especifica)
        valor=valor["value"]
        for j in range(1,lt.size(valor)+1):
            Dato=lt.getElement(valor,j)
            TaxiId=lt.getElement(Dato,1)
            Precio=float(lt.getElement(Dato,2))
            Millas=float(lt.getElement(Dato,3))
            if m.contains(IdTaxis,TaxiId)==True:
                Lista4=lt.newList("ARRAY_LIST")
                viaje=m.get(IdTaxis,TaxiId)
                viaje=viaje["value"]
                Dato1=float(lt.getElement(viaje,1))
                Dato2=float(lt.getElement(viaje,2))
                Dato3=float(lt.getElement(viaje,3))
                PrecioTotal=Precio+Dato1
                MillasTotal=Millas+Dato2
                TotalViajes=Dato3+1
                lt.addFirst(Lista4,PrecioTotal)
                lt.addLast(Lista4,MillasTotal)
                lt.addLast(Lista4,TotalViajes)
                m.put(IdTaxis,TaxiId,Lista4)
            else:
                Lista5=lt.newList("ARRAY_LIST")
                ViajesTotal=1
                lt.addFirst(Lista5,Precio)
                lt.addLast(Lista5,Millas)
                lt.addLast(Lista5,ViajesTotal)
                m.put(IdTaxis,TaxiId,Lista5)                          

    ListaLlaves=m.keySet(IdTaxis)
    for k in range(1,lt.size(ListaLlaves)+1):
        Llave1=lt.getElement(ListaLlaves,k)
        Cambio=m.get(IdTaxis,Llave1)
        Cambio=Cambio["value"]
        ActualizacionPrecio=float(lt.getElement(Cambio,1))
        if ActualizacionPrecio==0:
            ActualizacionPrecio=1
        ActualizacionMillas=float(lt.getElement(Cambio,2))
        ActualizacionViajes=float(lt.getElement(Cambio,3))
        Puntos=(ActualizacionMillas/ActualizacionPrecio)*ActualizacionViajes
        m.put(IdTaxis,Llave1,Puntos)
    return IdTaxis 
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
