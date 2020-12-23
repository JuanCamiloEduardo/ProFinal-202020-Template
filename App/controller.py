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

import config as cf
from App import model
import csv
import os

"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta.  Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________
def init():
    analyzer= model.newAnalyzer()
    return analyzer


# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________
def loadTrips(analyzer):
    viajes=0
    for filename in os.listdir(cf.data_dir):
        
        if filename.endswith('.csv'):
            print('Cargando archivo: ' + filename)
            viajes+=loadFile(analyzer, filename)
    print("viajes totales: "+str(viajes))
    return analyzer

def loadFile(analyzer, tripfile):
    """
    """
    tripfile = cf.data_dir + tripfile
    input_file = csv.DictReader(open(tripfile, encoding="utf-8"),
                                delimiter=",")
    viajes=0
    for trip in input_file:
        viajes+=1
        model.addtrip(analyzer,trip)
        model.addMap(analyzer,trip)

    return viajes

def loadTripsGrafo(analyzer,horainicio,horafinal,communityareainicio,communityareafinal):
    viajes=0
    for filename in os.listdir(cf.data_dir):
        
        if filename.endswith('.csv'):
            print('Cargando archivo: ' + filename)
            viajes+=loadFileGrafo(analyzer,filename,horainicio,horafinal,communityareainicio,communityareafinal)
    print("viajes totales: "+str(viajes))
    return analyzer

def loadFileGrafo(analyzer,tripfile,horainicio,horafinal,communityareainicio,communityareafinal):
    """
    """
    tripfile = cf.data_dir + tripfile
    input_file = csv.DictReader(open(tripfile, encoding="utf-8"),
                                delimiter=",")
    viajes=0
    for trip in input_file:
        viajes+=1
        model.addareas(analyzer,trip,horainicio,horafinal,communityareainicio,communityareafinal)

    return viajes

def loadTripsDay(analyzer,Dia,Id):
    for filename in os.listdir(cf.data_dir):
        if filename.endswith('.csv'):
            loadFileDia(analyzer,filename,Dia,Id)
    return analyzer
def loadFileDia(analyzer,tripfile,Dia,Id):
    """
    """
    tripfile = cf.data_dir + tripfile
    input_file = csv.DictReader(open(tripfile, encoding="utf-8"),
                                delimiter=",")
    for trip in input_file:
        model.addTripDia(analyzer,trip,Dia,Id)

# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________
