#SOTO JONATAN DNI N° 41.118.434

def es_primo(nro):
    """
    Función que determina si un número es primo.
    Retorna True si es primo, o False si no lo es.
    """
    if nro <= 1:
        return False
    
    raiz_cuadrada = int(nro ** 0.5) + 1
    
    for i in range(2, raiz_cuadrada):
        if nro % i == 0:
            return False 
            
    return True  

print("=========================================")
print("TP INTEGRADOR MODULO 3 - PUNTO 1: PRIMOS ")
print("=========================================")

try:
    
    numero_usuario = int(input("Ingrese un número entero para verificar: "))
    
    
    if es_primo(numero_usuario):
        print(f"Resultado: El número {numero_usuario} ES primo.")
    else:
        print(f"Resultado: El número {numero_usuario} NO es primo.")

except ValueError:
    print("Error: Por favor, ingrese un número entero válido (sin letras ni decimales).")