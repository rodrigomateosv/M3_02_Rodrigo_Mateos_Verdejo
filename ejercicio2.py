M3_02_Nicolas_Rodriguez_Becerril/EJERCICIO2.py /
@NiCo7889
NiCo7889 cambio
Latest commit 2d0ec3d 1 hour ago
 History
 1 contributor
19 lines (15 sloc)  617 Bytes

"""
Código a evaluar:
lista = [4, 7, 30, 23, 5]
lista[10]
"""

from ast import main

def error_elemento_fuera_lista(lista, elemento_lista): #Creo una función para resolver el ejercicio
    try: #Pruebo a ver si funciona
        elemento = lista[elemento_lista]#Busco el elemento que no pertenece a la lista
        return elemento
    except IndexError:#Capturo el error
        print("El elemento {} no pertenece a la lista, puesto que la lista es de {} elementos.".format(elemento_lista, len(lista)))

error_elemento_fuera_lista([4, 7, 30, 23, 5], 10)#Ejecuto la función

if __name__ == "__main__":
    main()

