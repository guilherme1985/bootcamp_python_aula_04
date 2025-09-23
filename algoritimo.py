lista_numeros: list = [40, 50, 60, 70, 0, -408593, 1, 50]

# [40, 50, 60, 70, 0, -408593, 1, 50]
# [50, 60, , 700, -408593, 1, 50]
# ["asdf", "bsdef", "t", "d", "y", "m", "q"]

# ORDENAÇÃO SIMPLES
#for i in range(len(lista_numeros)):
#    for j in range (i+1, len(lista_numeros)):
#        if lista_numeros[i] > lista_numeros[j]:
#            lista_numeros[i], lista_numeros[j] = lista_numeros[j], lista_numeros[i]

#print(lista_numeros)


## TORNANDO A ORDENAÇAO UMA FUNÇAO
# lista_numeros.sort()
# lista_numeros.reverse()

# teste: list = lista_numeros
# print(teste)



def ordenar_lista_numeros (numeros: list) -> list:
    nova_lista_numeros = numeros.copy()

    for i in range(len(nova_lista_numeros)):
        for j in range (i+1, len(nova_lista_numeros)):
            if nova_lista_numeros[i] > nova_lista_numeros[j]:
                nova_lista_numeros[i], nova_lista_numeros[j] = nova_lista_numeros[j], nova_lista_numeros[i]    
    return nova_lista_numeros

nova_lista = ordenar_lista_numeros(lista_numeros)
print(nova_lista)

