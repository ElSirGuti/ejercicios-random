# Funcion que genere números primos hasta un número n y que muestre
# tambien los numeros que no son primos

# Función que verifica si un número es primo
def esPrimo(num):
    # Se verifica que el número anterior no pueda dividirse
    # por ningún número entre 2 y ese mismo número -1
    for i in range(2,num-1):
        # Si es divisible por alguno se retorna false y termina el bucle
        if num%i == 0: return False
    # Si termina el bucle, es porque no fue divisible entonces es primo
    return True

# Función que almacena los números primos en una lista
def limite(num):
    # Se crea la lista
    primos = []
    no_primos = []
    for i in range(2, num+1):
        # Se verifica si el valor es primo
        result = esPrimo(i)
        # De ser así se guarda en la lista
        if result == True: primos.append(i)
        else: no_primos.append(i)
    
    # Devolvemos el resultado
    return primos, no_primos


# Funcion principal
def main():
    num = int(input("N: "))

    # Desempaquetado de lo que retorna la funcion
    primos, no_primos = limite(num)

    # Salida formateada
    print(f"Numeros primos: {primos}. \nNumeros no primos: {no_primos}.")

main()