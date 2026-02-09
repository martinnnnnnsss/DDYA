def esfibonacci(n):
    a = 0
    b = 1
    while b < n:
        a = b
        b = a + b
    if a == n:
        print("El numero si pertenece")
    else:
        print("El numero no pertenece")
"""def primo(n):"""

def main():
    n = int(input("Ingresa un numero"))

    if n > 0: 
        print ("El numero es positivo")
    elif n < 0: 
        print ("El numero es negativo")
    else:
        print ("El numero es cero")

main()