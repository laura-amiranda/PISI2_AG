import random
import time

from lerBrasil58 import *

POPULACAO_N = 150
GERACOES_N = 3000
TAXA_CRUZAMENTO = 0.8
TAXA_MUTACAO = 0.08
TORNEIO_K = 5
NUM_CIDADES = 58


def torneio(populacao):

    candidatos = random.sample(populacao, TORNEIO_K)

    melhor = candidatos[0]
    melhor_custo = custoCaminho(melhor, distancias)

    for individuo in candidatos[1:]:

        custo = custoCaminho(individuo, distancias)

        if custo < melhor_custo:
            melhor = individuo
            melhor_custo = custo

    return melhor[:]


def crossover(pai1, pai2):

    tamanho = len(pai1)

    inicio = random.randint(0, tamanho - 2)
    fim = random.randint(inicio + 1, tamanho - 1)

    filho = [-1] * tamanho

    for i in range(inicio, fim + 1):
        filho[i] = pai1[i]

    pos = (fim + 1) % tamanho

    for cidade in pai2:

        if cidade not in filho:

            filho[pos] = cidade
            pos = (pos + 1) % tamanho

    return filho


def mutacao(individuo):

    i = random.randint(0, len(individuo) - 2)
    j = random.randint(i + 1, len(individuo) - 1)

    individuo[i:j+1] = reversed(individuo[i:j+1])


inicio = time.time()

populacao = inicializaPopulacao(
    POPULACAO_N,
    NUM_CIDADES
)

melhor_individuo = None
melhor_custo = float("inf")

for geracao in range(GERACOES_N):

    melhor_geracao = min(
        populacao,
        key=lambda x: custoCaminho(x, distancias)
    )

    nova_populacao = [melhor_geracao[:]]

    while len(nova_populacao) < POPULACAO_N:

        pai1 = torneio(populacao)
        pai2 = torneio(populacao)

        if random.random() < TAXA_CRUZAMENTO:
            filho = crossover(pai1, pai2)
        else:
            filho = pai1[:]

        if random.random() < TAXA_MUTACAO:
            mutacao(filho)

        nova_populacao.append(filho)

    populacao = nova_populacao

    custo_geracao = custoCaminho(
        melhor_geracao,
        distancias
    )

    if custo_geracao < melhor_custo:

        melhor_custo = custo_geracao
        melhor_individuo = melhor_geracao[:]

fim = time.time()

tempo_total = fim - inicio


string_seta = " -> ".join(
    map(str, melhor_individuo)
)

string_seta += f" -> {melhor_individuo[0]}"


print("\n" + "="*45)
print("TSP - Algoritmo Genetico")
print("="*45)
print(f"Quantidade de Cidades    : {NUM_CIDADES}")
print(f"Numero de Geracoes       : {GERACOES_N}")
print(f"Tamanho da Populacao     : {POPULACAO_N}")
print(f"Taxa de Cruzamento       : {TAXA_CRUZAMENTO * 100:.2f}%")
print(f"Taxa de Mutacao          : {TAXA_MUTACAO * 100:.2f}%")
print(f"Selecao de Pais          : Torneio Binario (k={TORNEIO_K})")
print(f"Selecao Sobreviventes    : Elitismo")
print("-"*45)
print(f"Menor custo encontrado   : {melhor_custo}")
print(f"Tempo de processamento   : {tempo_total:.6f} S")
print(f"Rota completa            : {string_seta}")
print("="*45 + "\n")