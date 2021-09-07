# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 19:04:01 2021

@author: Desarrollo
"""
# condicionales

# Tabla de Verdad

# Tabla del AND
# V and V = V
# V and F = F
# F and V = F
# F and F = F
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False


# Tabla del OR
# V or V = V
# V or F = V
# F or V = V
# F or F = F
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False


# Tabla de Negacion
# not V = F
# Vnot F = V
print(not True)  # False
print(not False)  # True


print(True and False and True or False or True or True)  # True
print(True and (False and True) or False or (True or True))  # True


# Jeararquia de operadores
# 1. parentesis y llaves
# 2. potencias y raices
# 3. mustiplicacion y divicion
# 4. sumas y restas

# jearaquia de operadores booleanas
# 1.parentecis y llaves
# 2.tabla de verdad

# Estrctura if
x = 1
if(x > 0):
    print('1')
else:
    print('2')
print('3')


# HUA recive edad , dice mayor o menos de ead

ej1_edad = int(input("Digite su edad en años: "))

if(ej1_edad >= 18):
    print('Es mayor de edad')
else:
    print('Es menor de edad')


# HUA recive nota, aprovo > 3.0
ej2_nota = float(input("Digite su nota: "))

if(ej2_nota >= 3):
    print('Aprobó')
else:
    print('Reprobó')


# HUA resive numero y diga que es negativo , positivo o cero
ej3_n = float(input("Digite nuemro: "))

if(ej3_n >= 1):
    print('Positivo')
elif(ej3_n < 0):
    print('Negativo')
else:
    print('es cero')

# ciclos
# ciclo for

for valor in range(11):
    print(valor)


for valor in range(5, 11):
    print(valor)


for valor in range(2, 11, 2):
    print(valor)


# HUA n notas, promedio

ej4_nnotas = int(input("Digite numero de notas a registrar: "))
if (ej4_nnotas > 0):
    ej4_suma_notas = float(0)
    for n in range(ej4_nnotas):
        print(f'Digite el valor de la nota #{n + 1}: ')
        ej4_suma_notas = float(input())
    ej4_resultado = round(float(ej4_suma_notas / ej4_nnotas), 2)
else:
    print(f'{ej4_nnotas} no es un numero de notas valido ')



















