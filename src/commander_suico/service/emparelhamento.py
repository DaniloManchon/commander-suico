from itertools import combinations

from commander_suico.model.jogador import Jogador
from commander_suico.model.mesa import Mesa


def jogadores_ja_se_enfrentaram(jogadores: Jogador) -> bool:
    """
    Verifica se algum jogador neste grupo de 4 já enfrentou todos os outros.
    Retorna True se houver qualquer repetição.
    """
    for j1, j2 in combinations(jogadores, 2):
        if j2.nome in j1.oponentes:
            return True
    return False


def gerar_rodada_suica(jogadores: Jogador) -> list[Mesa]:
    """
    Gera mesas para uma nova rodada do sistema suíço com 4 jogadores por mesa.
    Tenta evitar confrontos repetidos.

    Parâmetros:
        jogadores: lista de instâncias de Jogador

    Retorna:
        Lista de objetos Mesa
    """
    # Ordenar por pontuação, depois por Elo
    jogadores_ordenados = sorted(jogadores, key=lambda j: (-j.pontuacao_torneio, -j.elo))

    mesas = []
    usados = set()

    i = 0
    while i < len(jogadores_ordenados):
        # Formar grupos de 4
        grupo = []
        while len(grupo) < 4 and i < len(jogadores_ordenados):
            candidato = jogadores_ordenados[i]
            if candidato not in usados:
                grupo.append(candidato)
                usados.add(candidato)
            i += 1

        # Se não temos 4, deixar esse grupo para próxima rodada
        if len(grupo) < 4:
            print("⚠️ Jogadores restantes não suficientes para uma mesa completa. Rodada incompleta.")
            break

        # Tentar evitar confrontos repetidos
        if jogadores_ja_se_enfrentaram(grupo):
            print(f"⚠️ Mesa com repetição detectada: {[j.nome for j in grupo]}")
            # Aqui você pode tentar lógica mais avançada de troca de jogadores entre grupos
            # Para simplicidade, apenas avisa
        mesa = Mesa(grupo)
        mesas.append(mesa)

    return mesas
