print("A continuación se calcularán las raíces de un polinomio cuadrático o de 2do grado")

a = float(input("Introduzca el valor A que acompaña al término cuadrático de la ecuación:"))

if a == 0:
    print("El coeficiente A NO PUEDE SER 0 ya que sería una ecuación lineal y no se podría dividir por 0")
else:
    b = float(input("Introduzca el valor B que acompaña al término lineal de la ecuación:"))
    c = float(input("Introduzca el valor C que corresponde al término independiente:"))


elemento = (b**2 - 4*a*c)

if elemento < 0:
    print("La ecuación cuadrática NO tiene raíces reales")
else:
    raiz= elemento**0.5
    den = 2*a

    ### Cálculo de las respectivas raíces
    X_1 = (-b + raiz)/den
    X_2 = (-b - raiz)/den

    print(f"Las raíces de la ecuación cuadrática {a}x² + {b}x + {c} son {X_1} y {X_2}")