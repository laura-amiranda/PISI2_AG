NUM_CIDADES = 13

coordenadas = {
    1:(0,3), 
    2:(1,5),  
    3:(2,1), 
    4:(3,7), 
    5:(4,2), 
    6:(5,8), 
    7:(6,5), 
    8:(7,9),  
    9:(8,3),  
    10:(9,6), 
    11:(9,10),
    12:(2,10),
    13:(0,8)
}

nomes_cidades = {
    1: "A",
    2: "B",
    3: "C",
    4: "D",
    5: "E",
    6: "F",
    7: "G",
    8: "H",
    9: "I",
    10: "J",
    11: "K",
    12: "L",
    13: "M"
}

distancias = {}

for i in coordenadas:
    for j in coordenadas:

        if i != j:

            x1,y1 = coordenadas[i]
            x2,y2 = coordenadas[j]

            distancia = abs(x1-x2) + abs(y1-y2)

            distancias[(i,j)] = distancia

import random

def custoCaminho(permutacao, dicDistancias):

    soma = 0

    for i in range(len(permutacao)-1):

        a = permutacao[i]
        b = permutacao[i+1]

        soma += dicDistancias[(a,b)]

    soma += dicDistancias[(permutacao[-1], permutacao[0])]

    return soma


def inicializaPopulacao(tamanho, qtdeCidades):

    populacao = []

    for _ in range(tamanho):

        individuo = list(range(1, qtdeCidades+1))

        random.shuffle(individuo)

        populacao.append(individuo)

    return populacao


def calculaAptidao(populacao, dicDistancias):

    lista = []

    for individuo in populacao:

        lista.append(
            custoCaminho(individuo, dicDistancias)
        )

    return lista