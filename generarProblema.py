import pygame
import random

def generarProblema(nivel):
#Devuelve una tupla con todo lo necesario para imprimir el problema en pantalla con su resultado y resultados falsos
#Los while del final son para asegurarse que no salga el resultado como opcion falsa y que no se repitan falsos
    op=random.choice("+-*/")
    if nivel == "facil":
        num1 = int(random.randrange(1,11,1))
        num2 = int(random.randrange(1,11,1))
    elif nivel == "medio":
        num1 = int(random.randrange(1,101,1))
        num2 = int(random.randrange(1,101,1))
    else:
        num1 = int(random.randrange(1,500,2))
        num2 = int(random.randrange(1,500,2))                    
    if op == "/":
        num2 = int(random.randrange(1,11,1))
        resCorrecto = num1
        num1 = num1 * num2
    else:
        resCorrecto = eval(str(num1)+op+str(num2))
    falso1 = falsear(num1,num2,op)
    while falso1 == resCorrecto:
        falso1 = falsear(num1,num2,op)
    falso2 = falsear(num1,num2,op)
    while falso1 == falso2 or falso2 == resCorrecto:
        falso2 = falsear(num1,num2,op)
    falso3 = falsear(num1,num2,op)
    while falso1 == falso3 or falso2 == falso3 or falso3 == resCorrecto:
        falso3 = falsear(num1,num2,op)
    devolver = (resCorrecto,num1,num2,op,falso1,falso2,falso3)
    return devolver


def falsear(x,y,op):
#Funcion auxiliar para devolver valores falsos
    if op == "/":
        ret = x / y + int(random.randrange(-3,3))
    else:
        num1 = x + int(random.randrange(-3,3))
        num2 = y + int(random.randrange(-3,3))
        ret = eval(str(num1)+op+str(num2))
    return ret
