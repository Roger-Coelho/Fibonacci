print("Fibonacci Recursivo com Programação Dinâmica")

#Função de Fibonacci recursivo com Programação Dinâmica
def fib(n, f = {}):
    
    if n == 0:
        f[n] = 0
        return f[n]
    elif n <= 1:
        ans = 1
    else:
        ans = f[n - 1] + f[n - 2]
    
    f[n] = ans
    return f[n]

#Informa a quantidade de interações do n-ésimo termo de Fibonacci
n = int(input("Informe o número de iterações: "))

#Imprime a série de Fibonacci
for i in range(n):
    print(fib(i))