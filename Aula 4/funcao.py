# Implementação do algoritmo de ordenação por seleção
lista_01 = [40, 50, 60, 70, 0, -408593, 1, 50]
lista_02 = [10, 78, 55, 99, 0, -408593, 3, 2333]
lista_03 = [900, 700, 600, 7, 6, -408593, 15, 99]



def ordenar_lista_de_numeros(numeros: list)-> list:
    nova_lista_de_numeros = numeros.copy()
    
    for i in range(len(nova_lista_de_numeros)):
        for j in range(i+1, len(nova_lista_de_numeros)):
            if nova_lista_de_numeros[i] > nova_lista_de_numeros[j]:
                nova_lista_de_numeros[i], nova_lista_de_numeros[j] = nova_lista_de_numeros[j], nova_lista_de_numeros[i]
    return nova_lista_de_numeros

nova_lista = ordenar_lista_de_numeros(lista_01)
nova_lista_02 = ordenar_lista_de_numeros(lista_02)
nova_lista_03 = ordenar_lista_de_numeros(lista_03)
