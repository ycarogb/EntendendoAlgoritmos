# def contarItensLista(lista):
#     if lista == []:
#         return 0

#     return 1 + contarItensLista(lista[1:])

# print(contarItensLista([2,1,4,5,3,6,7,8,9]))

def contar_itens_lista(lista, i=0):
    if i == len(lista):
        return 0
    return 1 + contar_itens_lista(lista, i + 1)

print(contar_itens_lista([2,1,4,5,3,6,7,8,9]))