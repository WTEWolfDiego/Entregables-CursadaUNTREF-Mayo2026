#importamos la libreria matematica necesaria
import math 
#Defina una funcion para recibir los tres coeficientes
def calcular_raices(a, b, c):
#Calcula el discriminante usando formula matematica
 discriminante = b**2 - 4*a*c
 if discriminante > 0:
    #Vereficia si existen dos soluciones reales
    x1 = (-b + math.sqrt(discriminante)) / (2*a)
    x2 = (-b - math.sqrt(discriminante)) / (2*a)
#math.sqrt(discriminante) - Obtiene la raiz cuadrada del discriminante 
    print("La ecuación tiene dos soluciones:")
    print("x1 =", x1)
    print("x2 =", x2)
#Verifica si existe una unica solución
 elif discriminante == 0:
    x= -b / (2*a)
    print("La ecuacion tiene una unica solución:")
    print("x =", x)
#Si el discriminante es negativo o no existen raices reales se ejecuta
 else:
    print("La ecuacion no tiene soluciones reales")
#Input para pedir al usuario que ingrese lo valores de los discriminantes
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))
#Calculo matematico de raices 
calcular_raices(a, b, c)