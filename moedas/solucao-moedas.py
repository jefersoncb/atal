def virar_moedas(moedas, i, K):
    for j in range(i, i+K):
        nova_posicao = 'C' if moedas[j] == 'V' else 'V'
        moedas[j] = nova_posicao


def minimo_operacoes(D: str, K: int) -> int:
    """Função que calcula o mínimo de operações a serem realizadas de forma a
    deixar todas as moedas com o valor voltado para cima.

    Parâmetros
    ----------
    D : str
        Estado inicial das moedas, onde V indica que uma moeda está com o valor
        voltado para cima, e C indica que uma moeda está com o valor voltado
        para baixo.

    K : int
        Número de moedas consecutivas que são viradas pela máquina.

    Retorna
    -------
    O menor número de operações a serem realizadas pela máquina, ou -1, caso
    não seja possível deixar todas as moedas com o valor voltado para cima.
    """
    moedas = list(D)
    N = len(D)
    operacoes = 0
    for i in range(N-K+1):
        if moedas[i] == 'C':
            operacoes += 1
            virar_moedas(moedas, i, K)
    if 'C' in moedas:
        return -1
    return operacoes

if __name__ == "__main__":
    help(minimo_operacoes)