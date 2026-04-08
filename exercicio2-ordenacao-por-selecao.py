def buscaMenor(arr):
    menor = arr[0]
    menorIndice = 0

    for index in range(1, len(arr)):
        if arr[index] < menor:
            menor = arr[index]
            menorIndice = index

    return menorIndice

def ordenacaoPorSelecao(arr):
    arrayOrdenado = []
    for index in range(len(arr)):
        menorIndice = buscaMenor(arr)
        arrayOrdenado.append(arr.pop(menorIndice))

    return arrayOrdenado


print(ordenacaoPorSelecao([5, 3, 6, 2, 10]))