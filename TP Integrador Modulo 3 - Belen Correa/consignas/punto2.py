import math

def ecuacion_cuadratica(a, b, c):
    discriminante = b**2 - 4*a*c

    if discriminante > 0:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        return f"2 soluciones: x1 = {x1}, x2 = {x2}"
    elif discriminante == 0:
        x = -b / (2*a)
        return f"1 solución: x = {x}"
    else:
        return "No hay solución real"


a = float(input("Ingresá el valor de a: "))
b = float(input("Ingresá el valor de b: "))
c = float(input("Ingresá el valor de c: "))

print(ecuacion_cuadratica(a, b, c))