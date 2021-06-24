from typing import List, Tuple

esquinas_visitadas = None
movimentos = [('N', -1, 0), ('S', 1, 0), ('L', 0, 1), ('O', 0, -1)]

def backtracking(M, N, L, C, B, l_atual, c_atual, rota_atual):
    global esquinas_visitadas

    # Testa se chegamos ao destino.
    if l_atual == L and c_atual == C:
        return "".join(rota_atual)
    
    # Testa cada um dos movimentos (N, S, L, O).
    for movimento in movimentos:
        direcao = movimento[0]
        l_destino = l_atual + movimento[1]
        c_destino = c_atual + movimento[2]
        # Se já passou pela esquina, não adianta voltar lá.
        if (l_destino, c_destino) in esquinas_visitadas:
            continue

        # Condições fora do mapa.
        if l_destino == -1 or l_destino == M:
            continue
        if c_destino == -1 or c_destino == N:
            continue
        if (l_destino, c_destino, l_atual, c_atual) in B:
            continue
        if (l_atual, c_atual, l_destino, c_destino) in B:
            continue

        # Se não visitou ainda a esquina e ela está dentro do mapa, chama
        # backtracking recursivamente.
        esquinas_visitadas.add((l_destino, c_destino))
        solucao = backtracking(M, N, L, C, B, l_destino, c_destino, list(rota_atual) + [direcao])
        if solucao is not None:
            return solucao
    
    # Caso nenhum dos caminhos leve ao destino, retorna None
    return None


def encontra_rota(M: int, N: int, L: int, C: int, B: List[Tuple[int, int, int, int]]) -> str:
    """Função que calcula uma rota entre as coordenadas (0, 0) e as coordenadas
    (L, C), em um grid de tamanho MxN, levando em consideração trechos que estão
    em obras, indicados na variável B.

    Parâmetros
    ----------
    M, N : int
        Dimensões do mapa da cidade.

    L, C : int
        Coordenadas do destino (L, C).

    B: List[Tuple[int, int, int, int]]
        Array com localização dos trechos em obras na cidade.

    Retorna
    -------
    Uma string indicando a direção de cada movimento feito no trajeto, ou
    "IMPOSSIVEL", caso não seja possível traçar uma rota.
    """
    global esquinas_visitadas
    # Inicialmente, nenhuma esquina foi visitada, a não ser a posição inicial de
    # Joãozinho (0,0).
    esquinas_visitadas = set()
    esquinas_visitadas.add((0,0))
    solucao = backtracking(M, N, L, C, set(B), 0, 0, [])
    if solucao is not None:
        return solucao
    return "IMPOSSIVEL"

if __name__ == "__main__":
    help(encontra_rota)
