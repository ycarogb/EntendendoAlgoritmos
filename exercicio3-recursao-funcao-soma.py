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


def somar(lista):
    if lista == []:  
        return 0 
    
    return lista[0] + somar(lista[1:])  

print(somar([2,4,6]))

