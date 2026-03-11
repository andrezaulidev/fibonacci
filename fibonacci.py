def fibonacci(posicao):
    a = 1
    b = 1

    if posicao == 0 or posicao == 1:
        return 1

    for i in range(2, posicao + 1):
        a, b = b, a + b

    return b

posicao = int(input("Qual posição da sequência de Fibonacci você quer? "))

resultado = fibonacci(posicao)

print("O número na posição", posicao, "é:", resultado)