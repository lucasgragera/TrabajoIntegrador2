#A. Operaciones con DNIs
#Ingreso de los DNIs (reales o ficticios).
dni1 = 12444356
dni2 = 43524123

#Generación automática de los conjuntos de dígitos únicos.
digitos_dni1 = set(map(int, str(dni1)))  
digitos_dni2 = set(map(int, str(dni2)))  

print("DNI 1:", dni1, "->", digitos_dni1)
print("DNI 2:", dni2, "->", digitos_dni2)

# Dígitos que están solo en uno de los dos (diferencia simétrica)
digitos_unicos = digitos_dni1 ^ digitos_dni2

print("Dígitos en solo uno de los dos DNI:", digitos_unicos)


#Cálculo y visualización de: unión, intersección, diferencias y diferencia simétrica.
union = digitos_dni1 | digitos_dni2
interseccion = digitos_dni1 & digitos_dni2
diferencia_1_2 = digitos_dni1 - digitos_dni2
diferencia_2_1 = digitos_dni2 - digitos_dni1
diferencia_simetrica = digitos_dni1 ^ digitos_dni2

print("\nUnión:", union)
print("Intersección:", interseccion)
print("Diferencia (DNI1 - DNI2):", diferencia_1_2)
print("Diferencia (DNI2 - DNI1):", diferencia_2_1)
print("Diferencia simétrica:", diferencia_simetrica)

#Conteo de frecuencia de cada dígito en cada DNI utilizando estructuras repetitivas.
frecuencia_dni1 = {}
frecuencia_dni2 = {}

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

print("Frecuencia de dígitos en DNI 1:", frecuencia_dni1)
print("Frecuencia de dígitos en DNI 2:", frecuencia_dni2)

#Suma total de los dígitos de cada DNI.

suma_dni1 = 0
suma_dni2 = 0

for digito in str(dni1):
    suma_dni1 += int(digito)

for digito in str(dni2):
    suma_dni2 += int(digito)

print("Suma de los dígitos del DNI 1:", suma_dni1)
print("Suma de los dígitos del DNI 2:", suma_dni2)

#Evaluación de condiciones lógicas (condicionales), vinculadas con las expresiones escritas.

#Comparacion de la suna de digitos
if suma_dni1 > suma_dni2:
    print("La suma de los dígitos del DNI 1 es mayor.")
elif suma_dni1 < suma_dni2:
    print("La suma de los dígitos del DNI 2 es mayor.")
else:
    print("Las sumas de ambos DNI son iguales.")

# Verificar si algún dígito aparece más de una vez en un DNI
if any(c > 1 for c in frecuencia_dni1.values()):
    print("El DNI 1 tiene dígitos repetidos.")
else:
    print("Todos los dígitos del DNI 1 son únicos.")

if any(c > 1 for c in frecuencia_dni2.values()):
    print("El DNI 2 tiene dígitos repetidos.")
else:
    print("Todos los dígitos del DNI 2 son únicos.")