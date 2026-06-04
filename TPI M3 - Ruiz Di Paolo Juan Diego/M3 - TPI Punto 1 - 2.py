def menu():
    print("1) Consultar si es número primo")
    print("2) Calcular raiz")
    nro_ingresado = input("Ingrese 1 o 2 para acceder a las funciones, o algo diferente para salir: ")
    match nro_ingresado:
        case "1":  es_primo()
        case "2": calcular_raiz()
        case _: exit()

    

def es_primo():
    nro = int(input("Ingrese número a evaluar: "))
    if nro <= 1:
        primo = False
    else:
        primo = True
        raiz_cuadrada = int(nro**0.5) + 1 # Es para tomar el entero que sigue a la raiz tomando su valor completo. 
        for i in range(2, raiz_cuadrada):
            if nro % i == 0:
                primo = False
                break
    if primo:
        print(f"El número {nro} es primo")
    else:
        print(f"El número {nro} no es primo")


def calcular_raiz():
    a = int(input("Ingrese valor de a: "))
    b = int(input("Ingrese valor de b: "))
    c = int(input("Ingrese valor de c: "))
    cantSoluciones = b**2 - (4 * a * c)
    positiva = ((-b) + (b**2 - (4 * a * c))**0.5)/(2*a)
    negativa = ((-b) - (b**2 - (4 * a * c))**0.5)/(2*a)
    if (cantSoluciones < 0):
        print("No tiene solución")
    elif (cantSoluciones > 0):
        print(f"Para los valores a: {a}, b: {b}, c: {c} se tienen dos raices que son {positiva:.0f} y {negativa:.0f}")
    else:
        print(f"Para los valores a: {a}, b: {b}, c: {c} tiene una única raiz que es {positiva:.0f}")

rta="s"

while (rta.lower() =="s"):
    menu()
    rta = input("Desea realizar otro procedimiento (s/n): ")


    