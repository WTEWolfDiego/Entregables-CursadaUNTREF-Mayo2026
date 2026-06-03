def numero_primo(numero):
    if numero <= 1:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
    for i in range(3, int(numero**0.5) + 1, 2):
        if numero % i == 0:
            return False
    return True
print("Bienvenido al programa para verificar números primos.")
Num = int(input("Ingresar un Numero: "))
if numero_primo(Num):
    print(f"{Num} es un número primo.")
else:
    print(f"{Num} no es un número primo.")