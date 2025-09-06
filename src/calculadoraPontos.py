import math

def calcular_resultado_partida(jogadores, posicoes, k=32):
    """
    Calcula a pontuação de torneio e atualização de Elo para uma partida de 4 jogadores.

    Parâmetros:
        jogadores: lista de dicionários com 'nome' e 'elo' (4 jogadores)
        posicoes: lista de posições finais (1 a 4), na mesma ordem da lista de jogadores
        k: fator K para cálculo do Elo (padrão: 32)

    Retorna:
        Uma lista com o novo estado de cada jogador (nome, elo antigo, novo elo, pontos torneio)
    """
    assert len(jogadores) == 4, "A partida deve ter 4 jogadores"
    assert set(posicoes) == {1, 2, 3, 4}, "As posições devem conter 1, 2, 3 e 4"

    # Pontuação de torneio baseada na posição final
    pontos_torneio = {
        1: 1.0,
        2: 0.5,
        3: 0.25,
        4: 0.0
    }

    # Resultado esperado para Elo, baseado na posição
    pontos_elo = {
        1: 1.0,
        2: 0.66,
        3: 0.33,
        4: 0.0
    }

    resultados = []
    for i, jogador in enumerate(jogadores):
        nome = jogador['nome']
        elo_antigo = jogador['elo']
        pos = posicoes[i]
        resultado = pontos_elo[pos]
        pontos = pontos_torneio[pos]

        # Média dos Elos dos oponentes
        elos_oponentes = [j['elo'] for j in jogadores if j != jogador]
        elo_medio_oponentes = sum(elos_oponentes) / 3

        # Expectativa de resultado
        E = 1 / (1 + 10 ** ((elo_medio_oponentes - elo_antigo) / 400))

        # Atualização do Elo
        delta = k * (resultado - E)
        novo_elo = round(elo_antigo + delta)

        resultados.append({
            'nome': nome,
            'elo_antigo': elo_antigo,
            'novo_elo': novo_elo,
            'pontos_torneio': pontos
        })

    return resultados

def calcular_buchholz(jogador, todos_os_jogadores):
    """
    Calcula o desempate Buchholz (soma dos pontos dos oponentes)
    para um jogador específico.

    Parâmetros:
        jogador: instância de Jogador
        todos_os_jogadores: lista com todas as instâncias de Jogador no torneio

    Retorna:
        Soma dos pontos dos oponentes do jogador
    """
    nome_para_jogador = {j.nome: j for j in todos_os_jogadores}
    soma = 0
    for nome_oponente in jogador.oponentes:
        oponente = nome_para_jogador.get(nome_oponente)
        if oponente:
            soma += oponente.pontuacao_torneio
    return soma
