""" 
10. Conversor de Temperatura Universal con Múltiples Escalas

Crear un conversor completo que maneje múltiples escalas de temperatura (Celsius, Fahrenheit, Kelvin). Solicitar al usuario la temperatura origen, la escala actual y la escala deseada. 
"""


def convertir_temperatura(valor, escala_origen, escala_destino):
    if escala_origen == "C":
        if escala_destino == "F":
            return (valor * 9/5) + 32
        elif escala_destino == "K":
            return valor + 273.15
    elif escala_origen == "F":
        if escala_destino == "C":
            return (valor - 32) * 5/9
        elif escala_destino == "K":
            return (valor - 32) * 5/9 + 273.15
    elif escala_origen == "K":
        if escala_destino == "C":
            return valor - 273.15
        elif escala_destino == "F":
            return (valor - 273.15) * 9/5 + 32

    raise ValueError("Escala de origen o destino no válida.")

print("Bienvenido al conversor de temperatura universal.")

valor = float(input("Ingrese la temperatura a convertir: "))
escala_origen = input("Ingrese la escala de origen (C, F, K): ").upper()
escala_destino = input("Ingrese la escala de destino (C, F, K): ").upper()

try:
    resultado = convertir_temperatura(valor, escala_origen, escala_destino)
    print(f"{valor}°{escala_origen} es igual a {resultado:.2f}°{escala_destino}.")  
except ValueError as e:
    print(e)
