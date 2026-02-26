def  pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1
    tentativa = 1

    while baixo <= alto:
        
        meio = (baixo + alto) // 2
        print("")
        print(f"baixo{tentativa} = {baixo}")
        print(f"alto{tentativa} = {alto}")
        print(f"meio{tentativa} = {meio}")
        chute = lista[meio]
        print(f"chute{tentativa} = {chute}")
        print("")

        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
        
        tentativa += 1

    return None

minha_lista = [1,3,5,7,9]


print ("Resultado para -1: ", pesquisa_binaria(minha_lista, -1))
