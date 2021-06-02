print("Fibonacci Recursivo")

#Função de Fibonacci recursivo
def fib(n):
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        ans = fib(n - 1) + fib(n - 2)
    return ans

#Informa a quantidade de interações do n-ésimo termo de Fibonacci
n = int(input("Informe o número de iterações: "))

#Imprime a série de Fibonacci
for i in range(n):
    print(fib(i))