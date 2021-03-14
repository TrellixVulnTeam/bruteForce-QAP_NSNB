# -*- coding: utf-8 -*-

# Imports
import numpy
from src.QAPBanco import QAPBanco
from itertools import permutations

# Algoritmo
def forca_bruta(n, D, F):
    """
    Algoritmo Força Bruta para calcular QAP do banco
    :param n: Número de dependências
    :type n: int
    :param D: Matriz de custo de deslocamento entre dependências
    :type D: class:`numpy.array` com shape=(n,n)
    :param F: Matriz de fator de risco
    :type F: class:`numpy.array` com shape=(n,n,n,n)
    :return: Matriz de escolha com rota ótima
    :rtype: class:`numpy.array` com shape=(n,n)
    """

    # Gera todas as possiveis permutações x
    permutacao = [numpy.array(perm) for perm in permutations(numpy.identity(n))]

    # Calculo do fator de escolha de acordo com cada permutação
    custo_ponderado = []
    for X in permutacao:
        fator_escolha = QAPBanco.calculo_fator_escolha(n, D, F, X)
        custo_ponderado = numpy.append(custo_ponderado, [fator_escolha])

    # Retorna matriz de escolha ótima
    idx = numpy.argmin(custo_ponderado)
    return permutacao[idx]
