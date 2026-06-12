# def encontrar_valor_mais_alto(lista, i = 0):
#     if len(lista) == 1:
#         return lista[0]
#     
#     return encontrar_valor_mais_alto(lista[1:])
#
# print(encontrar_valor_mais_alto([2,4,6]))
    
def encontrar_valor_mais_alto(lista, i=0):
    if not lista:
        raise ValueError("A lista não pode ser vazia")

    if i == len(lista) - 1:
        return lista[i]

    maior_do_resto = encontrar_valor_mais_alto(lista, i + 1)
    return lista[i] if lista[i] > maior_do_resto else maior_do_resto
    
print(encontrar_valor_mais_alto([2,4,6]))