from typing import List, Tuple
from queue import PriorityQueue

class Prato:
    # Representa um prato.
    def __init__(self, nome, valor, experiencia):
        self.nome = nome
        self.valor = valor
        self.experiencia = experiencia

class ConjuntoDePratos:
    # Representa uma escolha de pratos atual, e a melhor experiência possível.
    def __init__(self, pratos_escolhidos, pratos_disponiveis, valor_limite):
        self.pratos_escolhidos = pratos_escolhidos
        self.pratos_disponiveis = pratos_disponiveis
        self.experiencia_acumulada = sum([prato.experiencia for prato in self.pratos_escolhidos])
        self.valor_atual = sum([prato.valor for prato in pratos_escolhidos])
        proporcoes = [prato.experiencia/prato.valor for prato in pratos_disponiveis]
        self.maxima_experiencia_possivel = self.experiencia_acumulada + (valor_limite - self.valor_atual) * max(proporcoes)

    # Métodos de comparação, necessários para a fila de prioridade.
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

    # Se não tem nada no cardápio, a resposta é um array vazio.
    if len(C) == 0:
        return []

    # Cria os pratos baseado no cardápio.
    pratos = []
    for (nome, valor, experiencia) in C:
        pratos.append(Prato(nome, valor, experiencia))

    # Inicia a "mochila" com uma escolha vazia.
    escolha_vazia = ConjuntoDePratos([], pratos, L)

    # Cria a fila de "nós vivos", com a prioridade baseada na melhor experiência
    # possível de cada nó (o mais promissor será explorado primeiro).
    solucoes_possiveis = PriorityQueue()
    solucoes_possiveis.put(escolha_vazia)
    
    melhor_experiencia = 0
    escolha_final = escolha_vazia
    
    while not solucoes_possiveis.empty():
        # Recupera o nó mais promissor.
        proximo = solucoes_possiveis.get()

        # Como a fila está ordenada de acordo com a melhor experiência possível,
        # se o próximo nó não puder ser melhor que a melhor experiência já
        # conhecida, paramos a execução
        if proximo.maxima_experiencia_possivel <= melhor_experiencia:
            break

        # Joãozinho não tem dinheiro suficiente para comprar todos os pratos
        # dessa escolha.
        if proximo.valor_atual > L:
            continue

        # Encontramos uma escolha que Joãozinho pode pagar, e a experiência é
        # melhor que a anteriormente conhecida.
        if proximo.experiencia_acumulada > melhor_experiencia:
            melhor_experiencia = proximo.experiencia_acumulada
            escolha_final = proximo

        # Passo de expansão, onde adicionamos novos nós baseados no nó atual,
        # acrescentando um novo prato que ainda não foi escolhido.    
        for i in range(len(proximo.pratos_disponiveis)):
            prato_a_adicionar = proximo.pratos_disponiveis.pop(i)
            solucoes_possiveis.put(ConjuntoDePratos(list(proximo.pratos_escolhidos) + [prato_a_adicionar], list(proximo.pratos_disponiveis),L))
            proximo.pratos_disponiveis.insert(i, prato_a_adicionar)

    # Retorno da função. Obtemos o nome de cada um dos pratos presentes na
    # escolha final.        
    return [prato.nome for prato in escolha_final.pratos_escolhidos]

if __name__ == "__main__":
    help(melhor_experiencia)
