rta = 's'
while(rta == 's'):
    print("Se requiere la carga de las variables para el cálculo de la raíz")
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    evaluacion = (b)**2-(4*a*c)
    raiz_positiva = (-b+evaluacion**0.5)/(2*a)
    raiz_negativa = (-b-evaluacion**0.5)/(2*a)
    if (evaluacion>0):
        print(f"Para las variables a:{a}, b:{b}, c:{c} las soluciones son {int(raiz_negativa)} y {int(raiz_positiva)}")
    elif (evaluacion==0):
        print(f"Para las variables a:{a}, b:{b}, c:{c} la solución es {int(raiz_positiva)}")
    else:
        print(f"Para las variables a:{a}, b:{b}, c:{c} no hay solución")
    rta = input("¿Calcular otra raíz? (s/n): ")