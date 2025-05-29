#A. Operaciones con DNIs
#Ingreso de los DNIs (reales o ficticios).

dniA = 46582392
dniB = 43524123
dniC = 41906566
dniD = 45406120

#Generación automática de los conjuntos de dígitos únicos.

digitos_dniA = set(map(int, str(dniA)))  
digitos_dniB = set(map(int, str(dniB)))  
digitos_dniC = set(map(int, str(dniC)))  
digitos_dniD = set(map(int, str(dniD)))  

print("DNI A:", dniA, "->", digitos_dniA)
print("DNI B:", dniB, "->", digitos_dniB)
print("DNI C:", dniC, "->", digitos_dniC)
print("DNI D:", dniD, "->", digitos_dniD)

#Cálculo y visualización de: unión, intersección, diferencias y diferencia simétrica.

unionAB = digitos_dniA | digitos_dniB
unionAC = digitos_dniA | digitos_dniC
unionCB = digitos_dniC | digitos_dniB
unionAD = digitos_dniA | digitos_dniD
unionBD = digitos_dniB | digitos_dniD
unionCD = digitos_dniC | digitos_dniD

print("Unión A-B:", unionAB)
print("Unión A-C:", unionAC)
print("Unión C-B:", unionCB)
print("Unión A-D:", unionAD)
print("Unión B-D:", unionBD)
print("Unión C-D:", unionCD)

interseccionAB = digitos_dniA & digitos_dniB
interseccionAC = digitos_dniA & digitos_dniC
interseccionCB = digitos_dniC & digitos_dniB
interseccionAC = digitos_dniA & digitos_dniC
interseccionBC = digitos_dniB & digitos_dniC
interseccionDC = digitos_dniD & digitos_dniC

print("Intersección A-B:", interseccionAB)
print("Intersección A-C:", interseccionAC)
print("Intersección C-B:", interseccionCB)
print("Intersección A-C:", interseccionAC)
print("Intersección B-C:", interseccionBC)
print("Intersección D-C:", interseccionDC)

diferencia_A_B = digitos_dniA - digitos_dniB
diferencia_A_C = digitos_dniA - digitos_dniC
diferencia_A_D = digitos_dniA - digitos_dniD
diferencia_B_C = digitos_dniB - digitos_dniC
diferencia_B_A = digitos_dniB - digitos_dniA
diferencia_B_D = digitos_dniB - digitos_dniD
diferencia_C_B = digitos_dniC - digitos_dniB
diferencia_C_A = digitos_dniC - digitos_dniA
diferencia_C_D = digitos_dniC - digitos_dniD
diferencia_D_A = digitos_dniD - digitos_dniA
diferencia_D_B = digitos_dniD - digitos_dniB
diferencia_D_C = digitos_dniD - digitos_dniC

print("Diferencia (DNIA - DNIB):", diferencia_A_B)
print("Diferencia (DNIA - DNIC):", diferencia_A_C)
print("Diferencia (DNIA - DNID):", diferencia_A_D)
print("Diferencia (DNIB - DNIC):", diferencia_B_C)
print("Diferencia (DNIB - DNIA):", diferencia_B_A)
print("Diferencia (DNIB - DNID):", diferencia_B_D)
print("Diferencia (DNIC - DNIB):", diferencia_C_B)
print("Diferencia (DNIC - DNIA):", diferencia_C_A)
print("Diferencia (DNIC - DNID):", diferencia_C_D)
print("Diferencia (DNID - DNIA):", diferencia_D_A)
print("Diferencia (DNID - DNIB):", diferencia_D_B)
print("Diferencia (DNID - DNIC):", diferencia_D_C)

diferencia_simetricaAB = digitos_dniA ^ digitos_dniB
diferencia_simetricaAC = digitos_dniA ^ digitos_dniC
diferencia_simetricaCB = digitos_dniC ^ digitos_dniB
diferencia_simetricaDA = digitos_dniD ^ digitos_dniA
diferencia_simetricaDB = digitos_dniD ^ digitos_dniB
diferencia_simetricaDC = digitos_dniD ^ digitos_dniC

print("Diferencia simétrica A-B:", diferencia_simetricaAB)
print("Diferencia simétrica A-C:", diferencia_simetricaAC)
print("Diferencia simétrica C-B:", diferencia_simetricaCB)
print("Diferencia simétrica D-A:", diferencia_simetricaDA)
print("Diferencia simétrica D-B:", diferencia_simetricaDB)
print("Diferencia simétrica D-C:", diferencia_simetricaDC)


#Conteo de frecuencia de cada dígito en cada DNI utilizando estructuras repetitivas.
frecuencia_dniA = {}
frecuencia_dniB = {}
frecuencia_dniC = {}
frecuencia_dniD = {}

for digito in str(dniA):
    d = int(digito)
    if d in frecuencia_dniA:
        frecuencia_dniA[d] += 1
    else:
        frecuencia_dniA[d] = 1

for digito in str(dniB):
    d = int(digito)
    if d in frecuencia_dniB:
        frecuencia_dniB[d] += 1
    else:
        frecuencia_dniB[d] = 1

for digito in str(dniC):
    d = int(digito)
    if d in frecuencia_dniC:
        frecuencia_dniC[d] += 1
    else:
        frecuencia_dniC[d] = 1

for digito in str(dniD):
    d = int(digito)
    if d in frecuencia_dniD:
        frecuencia_dniD[d] += 1
    else:
        frecuencia_dniD[d] = 1

print("Frecuencia de dígitos en DNI A:", frecuencia_dniA)
print("Frecuencia de dígitos en DNI B:", frecuencia_dniB)
print("Frecuencia de dígitos en DNI C:", frecuencia_dniC)
print("Frecuencia de dígitos en DNI D:", frecuencia_dniD)

#Suma total de los dígitos de cada DNI.

suma_dniA = 0
suma_dniB = 0
suma_dniC = 0
suma_dniD = 0

for digito in str(dniA):
    suma_dniA += int(digito)

for digito in str(dniB):
    suma_dniB += int(digito)

for digito in str(dniC):
    suma_dniC += int(digito)

for digito in str(dniD):
    suma_dniD += int(digito)

print("Suma de los dígitos del DNI A:", suma_dniA)
print("Suma de los dígitos del DNI B:", suma_dniB)
print("Suma de los dígitos del DNI C:", suma_dniC)
print("Suma de los dígitos del DNI D:", suma_dniD)


#Evaluación de condiciones lógicas (condicionales), vinculadas con las expresiones escritas.

#Comparacion de la suna de digitos

if suma_dniA > suma_dniB and suma_dniA > suma_dniC and suma_dniA > suma_dniD:
    print("La suma de los dígitos del DNI A es mayor.")
elif suma_dniB > suma_dniA and suma_dniB > suma_dniC and suma_dniB > suma_dniD:
    print("La suma de los dígitos del DNI B es mayor.")
elif suma_dniC > suma_dniA and suma_dniC > suma_dniB and suma_dniC > suma_dniD:
    print("La suma de los dígitos del DNI C es mayor.")
elif suma_dniD > suma_dniA and suma_dniD > suma_dniB and suma_dniD > suma_dniC:
    print("La suma de los dígitos del DNI D es mayor.")
else:
    print("Hay al menos dos DNI con la suma de dígitos igual y mayor.")

#Interseccion total de digitos 

interseccion_total = digitos_dniA & digitos_dniB & digitos_dniC & digitos_dniD
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
evaluar_diversidad(digitos_dniA, 1)
evaluar_diversidad(digitos_dniB, 2)
evaluar_diversidad(digitos_dniC, 3)
evaluar_diversidad(digitos_dniD, 4)