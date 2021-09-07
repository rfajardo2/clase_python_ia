# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 18:54:54 2021

@author: Desarrollo
"""

print("hola mundo");

# variables
a = 3
print(type(a))

a = "hola"
print(type(a))

a = 3.5
print(type(a))

# suma

a = 5
b = 2
c = a + b
print(c)

# resta

a = 5
b = 2
c = a - b
print(c)

# multiplicacion

a = 5
b = 2
c = a * b
print(c)

# division

a = 5
b = 2
c = a / b
print(c)

a = 5
b = 2
c = a // b
print(c)

# potencia

a = 5
b = 2
c = a ** b
print(c)

# raiz

a = 27
b = 2
c = a ** (1/3)
print(c)

import math
raiz = math.sqrt(25)
print(raiz)


# tipo de datos

# string str
a = "Hola mundo"
a = 'Hola mundo'
b = "I can't do it"
c = 'Alias "roberto" '

# Entero int
a = 5

# Decimal float
a = 5.6

# Boolean bool
x = True
y = False

# conversiones entre tipos de datos

# convertir de x a entero
a = '3'
y = int(a)
print(y)
print(type(y))

# convertir de x a decimal
a = '3'
y = float(a)
print(y)
print(type(y))


# convertir de x a string
a = 3
y = str(a)
print(y)
print(type(y))


# concatenar
a = "Hola"
b = "Mundo"
c = a + " " + b 
print(c)
print(type(c))

# capturar por pantalla

nombre = input("Digite su nombre: ")
print("hola",nombre)

# HUA  que sume dos numeros e imprima su resultado

n1 = input("Digite el primer numero: ")
n2 = input("Digite el segundo numero: ")
resultado = int(n1) + int(n2)
print("El resultado de la suma es",n1,"+",n2,"=",resultado)


n11 = float(input("Digite el primer numero: "))
n22 = float(input("Digite el segundo numero: "))
resultado2 = n11 + n22
print("El resultado es",resultado2)
print(f"{resultado2}")


# HUA  que lea un numero e imprima su resultado del cuadrado

n_cuadrado = float(input("Digite el numero que se va a elevar: "))
resultado_cuadrado = n_cuadrado ** 2
print(f"El resultado es : {resultado_cuadrado}")



resultado_cuadrado2 =  float(input("Digite el numero que se va a elevar: ")) ** 2
print(f"El resultado es : {resultado_cuadrado2}")


# HUA que tome el valos de un producto , le aplique el 20%
# de descuento e imprima
# valor inicial , valor con  des y valor de ahoroo

varlor_producto = float(input("Digite valor del producto: $"))
valor_descuento = varlor_producto * 0.20
valor_total = varlor_producto - valor_descuento
print(f"Valor producto: ${varlor_producto:,}\n Valor descuento: ${valor_descuento:,}\n Valor total: ${valor_total:,}")


# ------Calcule el valor de Y indicando paso a paso como llegó al resultado 1.1
# 1.1    y = ( (5+2-5)^2 * 5+8/2 -30 ) / 2 * 5 -3
# 1.1    y = ( (2)^2 * 5+ 4 -30 ) / 2 * 5 -3
# 1.1    y = ( 4 * 5 + 4 - 30 ) / 2 * 5 -3
# 1.1    y = (20 + 4 -30 ) / 2 * 5 -3
# 1.1    y = (-6) / 2 * 5 -3
# 1.1    y = -3 * 5 -3
# 1.1    y = -18

ej1_1resultado = ((((5 + 2 - 5) ** 2) * 5 + (8 / 2) - 30) / 2) * 5 - 3
print(f"ej 1.1 y = ((((5+2-5)**2) * 5 + (8/2) -30 ) / 2 )* 5 -3")
print(f"ej 1.1 Resultado: {ej1_1resultado}")



# ------Calcule el valor de Y indicando paso a paso como llegó al resultado 1.2

# z=5
# n=3
# m= z-n
# y = (( (z+2-n)^2 * m+8/2 -30 ) / 2 * 5 -3)^ 5 + 15 * 3 - 9/3 

ej1_2z = 5
ej1_2n = 3
ej1_2m = ej1_2z - ej1_2n
ej1_2resultado = float((((((ej1_2z + 2 - ej1_2n)** 2) * ej1_2m + 8 / 2 - 30) / 2) * 5 - 3)** 5 + 15 * 3 - (9 / 3))
print("ej 1.2 y = ((((5+2-5)**2) * 5 + (8/2) -30 ) / 2 )* 5 -3")
print(f"ej 1.2 Resultado: {ej1_2resultado}")

# ------Calcule el valor de Y indicando paso a paso como llegó al resultado 1.3
# z=5
# n=( (8+2-4)^2 * 5+8+7/2 -30*5 ) / 2 * 5 -3
# m= z^2*3+n
# m= (5)^2*3+(( (8+2-4)^2 * 5+8+7/2 -30*5 ) / 2 * 5 -3)
# y = ((( (z+2-n)^2 x m+8/2 -30 ) / 2 * 5 -3)^ 5 + 15 * 3 - 9/3) ^ 2 – 5/4
# y = ((( (5+2-(( (8+2-4)^2 * 5+8+7/2 -30*5 ) / 2 * 5 -3))^2 * ((5)^2*3+(( (8+2-4)^2 * 5+8+7/2 -30*5 ) / 2 * 5 -3))+8/2 -30 ) / 2 * 5 -3)^ 5 + 15 * 3 - 9/3) ^ 2 – 5/4

ej1_3z = float(5)
ej1_3n = float((((8 + 2 - 4)**2) * 5 + 8 + 7 / 2 - 30 * 5)/ 2 * 5 - 3)
ej1_3m = float(((ej1_3z)**2) * 3 + (ej1_3n))
print(f"ej 1.2 Resultado: {ej1_3m}  ,{ej1_3n} , {ej1_3z} ")


# ej1_3resultado = float( (((((ej1_3z) + 2 - ((ej1_3n)**2) * ej1_3m + 8/2 - 30 ) / 2 * 5 - 3)** 5 + 15 * 3 - 9/3)**2 – 5/4)

ej1_3resultado = float(((((((((ej1_3z)+2-(ej1_3n)) ** 2) * (ej1_3m)+8/2 -30 ) / 2 * 5 -3) ** 5) + 15 * 3 - 9/3) ** 2) - (5/4))

print("ej 1.3 y = y = ((( (5+2-(( (8+2-4)^2 * 5+8+7/2 -30*5 ) / 2 * 5 -3))^2 * ((5)^2*3+(( (8+2-4)^2 * 5+8+7/2 -30*5 ) / 2 * 5 -3))+8/2 -30 ) / 2 * 5 -3)^ 5 + 15 * 3 - 9/3) ^ 2 – 5/4")
print(f"ej 1.3 Resultado: {ej1_3resultado}")























