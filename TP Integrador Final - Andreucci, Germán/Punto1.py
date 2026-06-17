### Se inicia un ciclo "While" para que el usuario pueda decidir si seguir introduciendo números o no
while True:
    num = int(input("Introduzca un número al azar de su preferencia: "))

    if num <= 1:
        print("NO es un número primo")
    else:
        divisores = 0
        
        for i in range(2, num):     ### se crea para dividir el número introducido, por los anteriores
            if num % i == 0:        ### obtenemos el resto de la división 
                divisores = divisores + 1

        ### Si no se encuentra ningun divisor en el proceso, es primo
        if divisores == 0:
            print("El número introducido ES primo")
        else:
            print("El número introducido NO es primo")

    ### Pregunta final para continuar o salir
    continuar = input("¿Querés ingresar otro número? (si/no): ")
    
    if continuar != "si" and continuar != "SI" and continuar != "Si":
        print("Programa terminado.")
        break