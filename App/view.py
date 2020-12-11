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


import sys
import config
from App import controller
from DISClib.ADT import stack
import timeit
assert config
from DISClib.ADT import list as lt

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones  y  por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Variables
# ___________________________________________________


# ___________________________________________________
#  Menu principal
# ___________________________________________________

"""
Menu principal
"""
def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información de viajes de taxis")
    print("3- Reportegeneral ")
    print("4- Top taxis (Dia,Rango) ")
    print("5- ")
    print("6- s ")


    print("0- Salir")
    print("*******************************************")

"-------------------------------------------------------------"
def optionTwo():
    print("\nCargando información de transporte de taxis ....")
    controller.loadTrips(analyzer)
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n>')

    if int(inputs[0]) == 1:
        print("\nInicializando....")
        # cont es el controlador que se usará de acá en adelante
        analyzer = controller.init()

    elif int(inputs[0]) == 2:
        executiontime = timeit.timeit(optionTwo, number=1)
    elif int(inputs[0]) == 3:
        parametrom=int(input("¿Cuantas companías que más servicios prestan desea conocer?"))
        parametron=int(input("¿Cuantas companías que más taxis poseen desea conocer?"))
        ntaxis,ncomapany,topm,topn=controller.reportegeneral(analyzer,parametrom,parametron)
        print("El número de taxis es: "+str(ntaxis))
        print("---------------------------------------------------------------")
        print("El número de compañías es: "+str(ncomapany))
        print("---------------------------------------------------------------")
        print("las "+ str(parametrom)+" compañías que más servicios prestan son:")
        print("     ")
        for i in range(1,parametrom+1):
            print(str(i)+".")
            print(lt.getElement(topm,i)["value"])
        print("---------------------------------------------------------------")
        print("las "+ str(parametron)+" compañías que más taxis tienen son:")
        print("     ")
        for i in range(1,parametron+1):
            print(str(i)+".")
            print(lt.getElement(topn,i)["value"])
    elif int(inputs[0]) == 4:
        print("Digite la fecha especifica")
        FechaO=input("Fecha Unica AAAA/MM/DD: ")
        CantidadN=input("Cuantos taxis desea conocer: ")
        print("Digite el Rango de una fecha")
        FechaI=input("Fecha Inicial AAAA/MM/DD: ")
        FechaF=input("Fecha Final AAAA/MM/DD: ")
        CantidadM=input("Cuantos taxis desea conocer: ")
        RespuestaFinal=controller.fechaRango(FechaI,FechaF,analyzer,FechaO)
        print("El top taxis en una fecha especifica es:")
        try:
            if lt.getElement(RespuestaFinal,1)==False:
                print("No hay taxis")
            else:
                ListaIndividuales=lt.getElement(RespuestaFinal,1)
                for i in range(1,int(CantidadN)+1):
                    top=lt.getElement(ListaIndividuales,i)
                    r=top.find("_:")
                    print(str(i)+"-"+top[0:r])
        except:
            print("Hubo un error")
        print("El top taxis por un rango es:")
        try:
            if lt.getElement(RespuestaFinal,2)==False:
                print("No hay taxis")
            else:
                ListaIndividuales=lt.getElement(RespuestaFinal,2)
                for j in range(1,int(CantidadM)+1):
                    top=lt.getElement(ListaIndividuales,j)
                    r=top.find("_:")
                    print(str(j)+"-"+top[0:r])
        except:
            print("Hubo un error")

    else:
        sys.exit(0)
