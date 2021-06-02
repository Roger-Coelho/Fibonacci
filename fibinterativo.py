print("Fibonacci Interativo")

#Função de Fibonacci Iterativo
def fib(n):
    i = 0
    first = -1
    second  = 1

    while i <= n:
        aux = first + second
        first = second
        second = aux
        i = i + 1
        print(second)

#Informa a quantidade de interações do n-ésimo termo de Fibonacci
n = int(input("Informe o número de iterações: "))

#Imprime a série de Fibonacci
fib(n)