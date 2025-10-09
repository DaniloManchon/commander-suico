class Mesa:
    def __init__(self, numero, jogadores):
        """
        Cria uma mesa com 4 jogadores.
        :param jogadores: Lista de 4 instâncias da classe Jogador
        """
        self.numero = numero
        if len(jogadores) != 4:
            raise ValueError("Uma mesa deve ter exatamente 4 jogadores.")
        self.jogadores = jogadores
        self.resultado_posicoes = []  # Ex: [Jogador, Jogador, Jogador, Jogador] em ordem de colocação

    def registrar_resultado(self, posicoes):
        """
        Registra as posições dos jogadores após a partida.
        :param posicoes: Lista de nomes dos jogadores em ordem da posição (1º a 4º)
        """
        if len(posicoes) != 4:
            raise ValueError("Deve haver exatamente 4 posições registradas.")
        
        # Reorganizar jogadores conforme posição
        nome_para_jogador = {j.nome: j for j in self.jogadores}
        self.resultado_posicoes = [nome_para_jogador[nome] for nome in posicoes]

        # Atualizar histórico de oponentes para cada jogador
        for jogador in self.jogadores:
            for oponente in self.jogadores:
                if oponente != jogador:
                    jogador.adicionar_oponente(oponente.nome)

    def aplicar_pontuacao_e_elo(self, k=32):
        """
        Aplica a pontuação do torneio e atualiza os Elos dos jogadores da mesa.
        Deve ser chamado depois de `registrar_resultado()`.
        """
        if not self.resultado_posicoes:
            raise ValueError("Resultados ainda não foram registrados.")

        # Definir pontos do torneio e "resultado Elo"
        pontos_torneio = [1.0, 0.5, 0.25, 0.0]
        resultado_elo = [1.0, 0.66, 0.33, 0.0]

        for idx, jogador in enumerate(self.resultado_posicoes):
            pontos = pontos_torneio[idx]
            resultado = resultado_elo[idx]

            # Calcular Elo médio dos oponentes
            oponentes = [j for j in self.jogadores if j != jogador]
            elo_medio = sum(j.elo for j in oponentes) / 3

            # Expectativa
            E = 1 / (1 + 10 ** ((elo_medio - jogador.elo) / 400))
            delta = k * (resultado - E)
            novo_elo = round(jogador.elo + delta)

            jogador.atualizar_elo(novo_elo)
            jogador.adicionar_pontos(pontos)

    def __repr__(self):
        nomes = ", ".join(j.nome for j in self.jogadores)
        return f"Mesa({nomes})"
