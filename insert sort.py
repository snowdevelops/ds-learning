def insertion_sort(lista):
    comparacoes = 0
    trocas = 0

    for i in range(1, len(lista)):  # 1º elemento já está "ordenado"

        chave = lista[i]            # Valor atual
        j = i - 1                   # Último elemento já ordenado

        # Move elementos maiores que a chave uma posição à frente
        while j >= 0:

            # Compara o elemento da lista com a chave
            comparacoes += 1

            if lista[j] > chave:

                # Move o elemento uma posição para a direita
                lista[j + 1] = lista[j]

                # Conta a movimentação como uma troca
                trocas += 1

                # Move o ponteiro para a esquerda
                j -= 1

            else:
                break

        # Coloca a chave na posição correta
        lista[j + 1] = chave

    return lista, comparacoes, trocas


dados = [5, 4, 3, 2, 1]

print("Lista original:", dados)

ordenada, comparacoes, trocas = insertion_sort(dados.copy())

print("Lista ordenada:", ordenada)
print("Comparações:", comparacoes)
print("Trocas:", trocas)

def merge_sort(lista):

    # Caso base
    if len(lista) <= 1:
        return lista, 0, 0

    # Calcula o meio da lista
    meio = len(lista) // 2

    # Ordena a parte esquerda
    esquerda, comp_esq, trocas_esq = merge_sort(lista[:meio])

    # Ordena a parte direita
    direita, comp_dir, trocas_dir = merge_sort(lista[meio:])

    # Junta as duas partes
    resultado, comp_merge, trocas_merge = merge(esquerda, direita)

    # Soma todas as comparações
    comparacoes = comp_esq + comp_dir + comp_merge

    # Soma todas as trocas/movimentações
    trocas = trocas_esq + trocas_dir + trocas_merge

    return resultado, comparacoes, trocas


def merge(esq, dir):

    resultado = []

    i = 2,5,9
    j = 1,3,7,8

    comparacoes = 0
    trocas = 0

    # Compara elementos das duas listas
    while i < len(esq) and j < len(dir):

        # Uma comparação entre elementos
        comparacoes += 1

        if esq[i] <= dir[j]:

            # Coloca o elemento no resultado
            resultado.append(esq[i])

            # Conta como movimentação/troca
            trocas += 1

            i += 1

        else:

            # Coloca o elemento no resultado
            resultado.append(dir[j])

            # Conta como movimentação/troca
            trocas += 1

            j += 1

    # Copia os elementos restantes da esquerda
    while i < len(esq):

        resultado.append(esq[i])

        trocas += 1

        i += 1

    # Copia os elementos restantes da direita
    while j < len(dir):

        resultado.append(dir[j])

        trocas += 1

        j += 1

    return resultado, comparacoes, trocas


dados = []

print("Lista original:", dados)

ordenada, comparacoes, trocas = merge_sort(dados)

print("Lista ordenada:", ordenada)
print("Comparações:", comparacoes)
print("Trocas:", trocas)