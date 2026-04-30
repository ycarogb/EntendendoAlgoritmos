# def somar(numeros):
#     if (len(numeros) == 0):
#         return 0
    
#     primeiroNumero = numeros[0]
#     numeros.remove(primeiroNumero)

#     if (len(numeros) == 0):
#         return primeiroNumero
#     else:
#         return primeiroNumero + somar(numeros)


# print(somar([2, 4, 6]))


def somar(numeros, i = 0):
    if (len(numeros) == 0 ):
        return 0

    if(len(numeros) > i - 1):
        return numeros[i] + somar(numeros, i + 1)

print(somar([2,4,6]))

