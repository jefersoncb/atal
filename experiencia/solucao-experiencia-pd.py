from typing import List, Tuple
from queue import PriorityQueue

class Prato:
    def __init__(self, nome, valor, experiencia):
        self.nome = nome
        self.valor = valor
        self.experiencia = experiencia

class ConjuntoDePratos:
    def __init__(self, pratos_escolhidos, pratos_disponiveis, valor_limite):
        self.pratos_escolhidos = pratos_escolhidos
        self.pratos_disponiveis = pratos_disponiveis
        self.experiencia_acumulada = sum([prato.experiencia for prato in self.pratos_escolhidos])
        self.valor_atual = sum([prato.valor for prato in pratos_escolhidos])
        proporcoes = [prato.experiencia/prato.valor for prato in pratos_disponiveis]
        self.maxima_experiencia_possivel = self.experiencia_acumulada + (valor_limite - self.valor_atual) * max(proporcoes)

    def __eq__(self, other):
        return self.maxima_experiencia_possivel == other.maxima_experiencia_possivel
    def __gt__(self, other):
        return self.maxima_experiencia_possivel > other.maxima_experiencia_possivel


def melhor_experiencia(L: int, C: List[Tuple[str, int, int]]) -> List[str]:
    """Função que determina qual escolha de pratos, dentro dos descritos no
    cardápio C, resulta na melhor experiência gastronômica possível, respeitando
    o limite de valor L.

    Parâmetros
    ----------
    L : int
        O limite de valor.

    C : List[Tuple[str, int, int]]
        Array com tuplas na forma (Nome, Valor, Experiência) de cada prato.

    Retorna
    -------
    Um array de strings indicando os pratos escolhidos.
    """
    pratos = [Prato(prato[0], prato[1], prato[2]) for prato in C]
    escolha_vazia = ConjuntoDePratos([], pratos, L)
    solucoes_possiveis = PriorityQueue()
    solucoes_possiveis.put(escolha_vazia)
    melhor_experiencia = 0
    escolha = None
    while not solucoes_possiveis.empty():
        proximo = solucoes_possiveis.get()
        if proximo.valor_atual > L:
            continue
        if proximo.experiencia_acumulada > melhor_experiencia:
            melhor_experiencia = proximo.experiencia_acumulada
            escolha = proximo
        for i in range(len(proximo.pratos_disponiveis)):
            prato_a_adicionar = proximo.pratos_disponiveis.pop(i)
            solucoes_possiveis.put(ConjuntoDePratos(list(proximo.pratos_escolhidos) + [prato_a_adicionar], list(proximo.pratos_disponiveis),L))
            proximo.pratos_disponiveis.insert(i, prato_a_adicionar)
    return [prato.nome for prato in escolha.pratos_escolhidos]

if __name__ == "__main__":
    help(melhor_experiencia)
