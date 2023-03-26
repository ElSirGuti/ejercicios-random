# Funcion que genere la sucesion de Fibonacci hasta un numero n

# Funcion que realiza la sucesion
def serieFibonacci(num):
    a,b = 0,1
    
    # Iniciamos la serie con 0
    fibonacci = [0]

    for i in range(num):
        if b > num: return fibonacci
        else: 
            fibonacci.append(b)
            a,b = b,a+b

def main():
    num = int(input("Limite: "))

    resultado = serieFibonacci(num)
    
    print(resultado)

main()


