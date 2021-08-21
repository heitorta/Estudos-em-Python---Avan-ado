#Método da bissecção
#f(x) = x³ + x +10 

import math
def inicio(a, b):
    return (a+b)/2

def tol(a, b):
    return math.fabs(b-a)/2
def f(x):
    return x**3 + x + 10
global a, b, c
a = -5
b = 5
c = (a+b)/2
#Utilizando o if, invoco a função f(x) que criei.

if f(a) * f(b) < 0 and f(a) * f(c) < 0:
    #O operador lógico and funciona de forma a simplificar o processo de criar vários if's
    print(f'A primeira iteração é:  {inicio(a, c)} e possui uma precisão TOL = {tol(a, b)}, caso continue o processo, usaremos o intervalo ({a}, {c}).')
    a = a
    b = c
    c = (a + b) / 2
else:
    print((f'A primeira iteração é:  {inicio(c, b)} e possui uma precisão TOL = {tol(a, b)}, caso continue o'
           f' processo, usaremos o intervalo [{c}, {b}). '))
    a = c
    b = b
    c = (a + b) / 2

#A segunda iteração funciona da mesma forma que a primeira, não há diferença alguma.

if f(a) * f(b) < 0 and f(a) * f(c) < 0:
    print(f'A segunda iteração é: {inicio(a, c)} e possui uma precisão TOL = {tol(a, b)}, caso continue o'
          f' processo, usaremos o intervalo ({a}, {c}). ')
    a = a
    b = c
    c = (a + b) / 2
else:
    print((f'A segunda iteração é: {inicio(c, b)} e possui uma precisão TOL = {tol(a, b)}, caso continue o'
           f' processo, usaremos o intervalo [{c}, {b}). '))
    a = c
    b = b
    c = (a + b) / 2

#E, novamente, a terceira iteração funciona da mesma maneira que todas as anteriores.

if f(a) * f(b) < 0 and f(a) * f(c) < 0:
    print(f'A terceira iteração é: {inicio(a, c)} e possui uma precisão TOL = {tol(a, b)}, caso continue o '
          f'processo, usaremos o intervalo ({a}, {c}). ')
    a = a
    b = c
    c = (a + b) / 2
else:
    print((f' A terceira iteração é: {inicio(c, b)} e possui uma precisão TOL = {tol(a, b)}, caso continue o '
           f' processo, usaremos o intervalo [{c}, {b}). '))
    a = c
    b = b
    c = (a + b) / 2
