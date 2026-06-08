#SOTO JONATAN DNI N° 41.118.434
import math

def calcular_bhaskara(a, b, c):
    """
    Calcula las raíces de una ecuación cuadrática basándose en el discriminante.
    """
    if a == 0:
        print("Error crítico: el coeficiente 'a' no puede ser cero.")
        return

    discriminante = b**2 - (4 * a * c)
    print(f"\nEl discriminante calculado es: {discriminante}")

    if discriminante > 0:
        print("Resultado: el discriminante es positivo -> Hay 2 soluciones reales.")
       
        raiz1 = (-b + math.sqrt(discriminante)) / (2 * a)
        raiz2 = (-b - math.sqrt(discriminante)) / (2 * a)
        print(f"   ↳ X1 = {raiz1}")
        print(f"   ↳ X2 = {raiz2}")
        
    elif discriminante == 0:
        print("Resultado: el discriminante es cero -> Hay 1 única solución real.")
        raiz = -b / (2 * a)
        print(f"   ↳ X = {raiz}")
        
    else:
        print("Resultado: el discriminante es negativo -> NO hay solución real.")


print("====================================================")
print("    TP INTEGRADOR - PUNTO 2: ECUACIÓN CUADRÁTICA    ")
print("====================================================")

try:
    coef_a = float(input("Ingrese el coeficiente 'a': "))
    coef_b = float(input("Ingrese el coeficiente 'b': "))
    coef_c = float(input("Ingrese el coeficiente 'c': "))
    
    calcular_bhaskara(coef_a, coef_b, coef_c)

except ValueError:
    print("Error: ingrese valores numéricos válidos (use punto para los decimales).")