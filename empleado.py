"""
Diseña un programa que tome dos variables: ventas_mes (número) y asistencia_perfecta (booleano). Si las ventas 
superan las 50 unidades y el empleado tiene asistencia perfecta, gana el bono "Premium". 
Si cumple solo una de las dos, gana el bono "Estándar". Si no cumple ninguna, no recibe bono. Usa operadores lógicos (and, or).
"""

nombreEmpleado = "Juan Pérez"

ventas_mes = 60  # Número de ventas del mes
asistencia_perfecta = True  # Booleano que indica si el empleado tuvo asistencia perfecta

if ventas_mes > 50 and asistencia_perfecta:
    bono = "Premium"
elif ventas_mes > 50 or asistencia_perfecta:
    bono = "Estándar"
else:
    bono = "No recibe bono"

print(f"Empleado: {nombreEmpleado}")
print(f"Ventas del mes: {ventas_mes}")  
print(f"Asistencia perfecta: {asistencia_perfecta}")
print(f"Bono otorgado: {bono}")


