def cuadratica(a, b, c):
    if a == 0:
        return "No es cuadrática"
    d = b**2 - 4*a*c
    if d < 0:
        return "No hay solución real"
    if d == 0:
        x = -b / (2*a)
        return f"Una solución: {x}"
    x1 = (-b + d**0.5) / (2*a)
    x2 = (-b - d**0.5) / (2*a)
    return f"Dos soluciones: {x1} y {x2}"

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
print(cuadratica(a, b, c))