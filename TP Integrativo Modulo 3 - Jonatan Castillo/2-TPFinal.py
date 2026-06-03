import math

def calcular_raiz(a, b, c):
    if a == 0:
        if b == 0:
            return ()
        else:
            raiz = -c / b
            return (raiz,)
        
    discriminante = b**2 - 4*a*c

    if discriminante < 0:
        return ()
    elif discriminante == 0:
        raiz = -b / (2*a)
        return (raiz,)
    else:
        raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
        raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
        return (raiz1, raiz2)
print("Bienvenido al programa para calcular las raíces de una ecuación cuadrática.")    
print("A continuación, ingrese las variables")
try:
    a = float(input("Ingrese el valor de a: "))
    b = float(input("Ingrese el valor de b: "))
    c = float(input("Ingrese el valor de c: "))
    
    resultado = calcular_raiz(a, b, c)
    if len(resultado) == 0:
        print("No se pudieron calcular las raíces. ecuación sin solución.")
    elif len(resultado) == 1:
        print(f"La raíz es: {resultado[0]}")
    else:
        print(f"Las raíces son: {resultado[0]} y {resultado[1]}")

except ValueError:
    print(f"Error: Ingrese solo valores numéricos válidos.")