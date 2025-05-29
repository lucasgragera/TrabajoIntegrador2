#A. Operaciones con DNIs
#Ingreso de los DNIs (reales o ficticios).

dni1 = 46582392
dni2 = 43524123
dni3 = 41906566
dni4 = 45406120

#Generación automática de los conjuntos de dígitos únicos.

digitos_dni1 = set(map(int, str(dni1)))  
digitos_dni2 = set(map(int, str(dni2)))  
digitos_dni3 = set(map(int, str(dni3)))  
digitos_dni4 = set(map(int, str(dni4)))  

print("DNI 1:", dni1, "->", digitos_dni1)
print("DNI 2:", dni2, "->", digitos_dni2)
print("DNI 3:", dni3, "->", digitos_dni3)
print("DNI 4:", dni4, "->", digitos_dni4)

#Cálculo y visualización de: unión, intersección, diferencias y diferencia simétrica.

union12 = digitos_dni1 | digitos_dni2
union13 = digitos_dni1 | digitos_dni3
union32 = digitos_dni3 | digitos_dni2
union14 = digitos_dni1 | digitos_dni4
union24 = digitos_dni2 | digitos_dni4
union34 = digitos_dni3 | digitos_dni4

print("Unión 1-2:", union12)
print("Unión 1-3:", union13)
print("Unión 3-2:", union32)
print("Unión 1-4:", union14)
print("Unión 2-4:", union24)
print("Unión 3-4:", union34)

interseccion12 = digitos_dni1 & digitos_dni2
interseccion13 = digitos_dni1 & digitos_dni3
interseccion32 = digitos_dni3 & digitos_dni2
interseccion13 = digitos_dni1 & digitos_dni3
interseccion23 = digitos_dni2 & digitos_dni3
interseccion43 = digitos_dni4 & digitos_dni3

print("Intersección 1-2:", interseccion12)
print("Intersección 1-3:", interseccion13)
print("Intersección 3-2:", interseccion32)
print("Intersección 1-3:", interseccion13)
print("Intersección 2-3:", interseccion23)
print("Intersección 4-3:", interseccion43)

diferencia_1_2 = digitos_dni1 - digitos_dni2
diferencia_1_3 = digitos_dni1 - digitos_dni3
diferencia_1_4 = digitos_dni1 - digitos_dni4
diferencia_2_3 = digitos_dni2 - digitos_dni3
diferencia_2_1 = digitos_dni2 - digitos_dni1
diferencia_2_4 = digitos_dni2 - digitos_dni4
diferencia_3_2 = digitos_dni3 - digitos_dni2
diferencia_3_1 = digitos_dni3 - digitos_dni1
diferencia_3_4 = digitos_dni3 - digitos_dni4
diferencia_4_1 = digitos_dni4 - digitos_dni1
diferencia_4_2 = digitos_dni4 - digitos_dni2
diferencia_4_3 = digitos_dni4 - digitos_dni3

print("Diferencia (DNI1 - DNI2):", diferencia_1_2)
print("Diferencia (DNI1 - DNI3):", diferencia_1_3)
print("Diferencia (DNI1 - DNI4):", diferencia_1_4)
print("Diferencia (DNI2 - DNI3):", diferencia_2_3)
print("Diferencia (DNI2 - DNI1):", diferencia_2_1)
print("Diferencia (DNI2 - DNI4):", diferencia_2_4)
print("Diferencia (DNI3 - DNI2):", diferencia_3_2)
print("Diferencia (DNI3 - DNI1):", diferencia_3_1)
print("Diferencia (DNI3 - DNI4):", diferencia_3_4)
print("Diferencia (DNI4 - DNI1):", diferencia_4_1)
print("Diferencia (DNI4 - DNI2):", diferencia_4_2)
print("Diferencia (DNI4 - DNI3):", diferencia_4_3)

diferencia_simetrica12 = digitos_dni1 ^ digitos_dni2
diferencia_simetrica13 = digitos_dni1 ^ digitos_dni3
diferencia_simetrica32 = digitos_dni3 ^ digitos_dni2
diferencia_simetrica41 = digitos_dni4 ^ digitos_dni1
diferencia_simetrica42 = digitos_dni4 ^ digitos_dni2
diferencia_simetrica43 = digitos_dni4 ^ digitos_dni3

print("Diferencia simétrica 1-2:", diferencia_simetrica12)
print("Diferencia simétrica 1-3:", diferencia_simetrica13)
print("Diferencia simétrica 3-2:", diferencia_simetrica32)
print("Diferencia simétrica 4-1:", diferencia_simetrica41)
print("Diferencia simétrica 4-2:", diferencia_simetrica42)
print("Diferencia simétrica 4-3:", diferencia_simetrica43)


#Conteo de frecuencia de cada dígito en cada DNI utilizando estructuras repetitivas.
frecuencia_dni1 = {}
frecuencia_dni2 = {}
frecuencia_dni3 = {}
frecuencia_dni4 = {}

for digito in str(dni1):
    d = int(digito)
    if d in frecuencia_dni1:
        frecuencia_dni1[d] += 1
    else:
        frecuencia_dni1[d] = 1

for digito in str(dni2):
    d = int(digito)
    if d in frecuencia_dni2:
        frecuencia_dni2[d] += 1
    else:
        frecuencia_dni2[d] = 1

for digito in str(dni3):
    d = int(digito)
    if d in frecuencia_dni3:
        frecuencia_dni3[d] += 1
    else:
        frecuencia_dni3[d] = 1

for digito in str(dni4):
    d = int(digito)
    if d in frecuencia_dni4:
        frecuencia_dni4[d] += 1
    else:
        frecuencia_dni4[d] = 1

print("Frecuencia de dígitos en DNI 1:", frecuencia_dni1)
print("Frecuencia de dígitos en DNI 2:", frecuencia_dni2)
print("Frecuencia de dígitos en DNI 3:", frecuencia_dni3)
print("Frecuencia de dígitos en DNI 4:", frecuencia_dni4)

#Suma total de los dígitos de cada DNI.

suma_dni1 = 0
suma_dni2 = 0
suma_dni3 = 0
suma_dni4 = 0

for digito in str(dni1):
    suma_dni1 += int(digito)

for digito in str(dni2):
    suma_dni2 += int(digito)

for digito in str(dni3):
    suma_dni3 += int(digito)

for digito in str(dni4):
    suma_dni4 += int(digito)

print("Suma de los dígitos del DNI 1:", suma_dni1)
print("Suma de los dígitos del DNI 2:", suma_dni2)
print("Suma de los dígitos del DNI 3:", suma_dni3)
print("Suma de los dígitos del DNI 4:", suma_dni4)


#Evaluación de condiciones lógicas (condicionales), vinculadas con las expresiones escritas.

#Comparacion de la suna de digitos

if suma_dni1 > suma_dni2 and suma_dni1 > suma_dni3 and suma_dni1 > suma_dni4:
    print("La suma de los dígitos del DNI 1 es mayor.")
elif suma_dni2 > suma_dni1 and suma_dni2 > suma_dni3 and suma_dni2 > suma_dni4:
    print("La suma de los dígitos del DNI 2 es mayor.")
elif suma_dni3 > suma_dni1 and suma_dni3 > suma_dni2 and suma_dni3 > suma_dni4:
    print("La suma de los dígitos del DNI 3 es mayor.")
elif suma_dni4 > suma_dni1 and suma_dni4 > suma_dni2 and suma_dni4 > suma_dni3:
    print("La suma de los dígitos del DNI 4 es mayor.")
else:
    print("Hay al menos dos DNI con la suma de dígitos igual y mayor.")

#Interseccion total de digitos 

interseccion_total = digitos_dni1 & digitos_dni2 & digitos_dni3 & digitos_dni4
if interseccion_total:
    print("Dígito/s compartido/s entre todos los DNIs:", interseccion_total)
else:
    print("No hay dígito compartido entre todos los DNIs.")

# Evaluar diversidad numérica basada en cantidad de dígitos distintos

def evaluar_diversidad(digitos_unicos, dni_num):
    cantidad = len(digitos_unicos)
    if cantidad >= 7:
        print(f"DNI {dni_num}: Diversidad numérica alta ({cantidad} dígitos distintos)")
    elif cantidad >= 5:
        print(f"DNI {dni_num}: Diversidad numérica media ({cantidad} dígitos distintos)")
    else:
        print(f"DNI {dni_num}: Diversidad numérica baja ({cantidad} dígitos distintos)")
# Evaluar cada DNI
evaluar_diversidad(digitos_dni1, 1)
evaluar_diversidad(digitos_dni2, 2)
evaluar_diversidad(digitos_dni3, 3)
evaluar_diversidad(digitos_dni4, 4)