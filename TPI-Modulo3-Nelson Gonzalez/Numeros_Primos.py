#Solicita al usuario que ingrese un numero.
numero = int(input("Ingrese un número: "))
#Una variable booleana para determinar si el numero es primo o no.
es_primo = True
#verifica si el numero es menor o igual a 1, en caso de que sea asi, el numero no es primo.
if numero <= 1:
    es_primo = False
#Recorre todos los numeros desde el 2 hasta el numero ingresado, verifica si el numero es 
#divisible por alguno de esos numeros, si es asi, el numero no es primo y se detiene el ciclo.
else:
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break
#Break (Finaliza el ciclo inmeditamente al encontrar un divisor)        
#Recorre todo los posibles divisores hasta el numero anterior a ingresar
if es_primo:
    print("El número es primo.")
else:
    print("El número no es primo.")
#Imprime el resultado indicando si el numero es primo o no.1