M3_02_Nicolas_Rodriguez_Becerril/EJERCICIO3.py /
@NiCo7889
NiCo7889 cambio
Latest commit c9ff833 1 hour ago
 History
 1 contributor
20 lines (16 sloc)  637 Bytes

"""
Código a evaluar:
paises = { "españa":"español", "eeuu":"inglés", "italia":"italiano" } 
paises["alemania"]
"""

from ast import main 

def errorclave_out_diccionario(diccionario, clave):#Creo una función para resolver el ejercicio
    try:#Pruebo a ver si funciona
        clave = diccionario[clave]
        return clave 
    except KeyError: #Capturo el error
        print ("La clave {} no se encuentra en la lista".format(clave))     
    return 

errorclave_out_diccionario({ "españa":"español", "eeuu":"inglés", "italia":"italiano" } , "alemania")#Ejecuto la función

if __name__ == "__main__":
    main()

