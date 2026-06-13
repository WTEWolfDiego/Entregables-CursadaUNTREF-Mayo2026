rta = 's'
while(rta == 's'):
    divisores = [1]
    nro = int(input("Ingrese número a evaluar: "))
    if nro <= 0:
        print("Solo se aceptan números mayores a cero.")
    elif(nro>=1):
        if (nro>1):
            for divisor in range(2,nro//2):  #para acortar la cantidad de números posibles almacenando el entero
                if (nro%divisor == 0):
                    divisores.append(divisor)
            divisores.append(nro)
        if len(divisores) > 2:
            print(f"El número {nro} no es primo, puede dividirse por {divisores}")
        else:
            print(f"El número {nro} es primo, solo se divide por {divisores}")
    rta = input("¿Desea ingresar otro número? (s/n): ")
