"""
Código a evaluar:
numero = 7/0
"""

from ast import main 

def errordivision_0(numerador,denominador): #Creo una función para resolver el ejercicio
    try: #Pruebo a ver si funciona
        numero = numerador/denominador
        return numero 
    except ZeroDivisionError: #Capturo el error
        print("No se puede dividir por 0.") #Pido que al dividir entre cero me de error

errordivision_0(7,0) #Ejecuto la función

if __name__ == "__main__":
    main()
