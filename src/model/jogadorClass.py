class Jogador:
    def __init__(self, nome, elo=1500):
        """
        Cria um jogador com nome e Elo inicial (padrão: 1500).
        """
        self.nome = nome
        self.elo = elo
        self.pontuacao_torneio = 0  # Pontos acumulados no torneio
        self.oponentes = set()      # Registro de oponentes enfrentados

    def adicionar_oponente(self, oponente_nome):
        """
        Registra um oponente enfrentado neste torneio.
        """
        self.oponentes.add(oponente_nome)

    def atualizar_elo(self, novo_elo):
        """
        Atualiza o Elo do jogador após uma partida.
        """
        self.elo = novo_elo

    def adicionar_pontos(self, pontos):
        """
        Adiciona pontos à pontuação do torneio (ex: 1.0 para vitória).
        """
        self.pontuacao_torneio += pontos

    def __repr__(self):
        return f"{self.nome} (Elo: {self.elo}, Pontos: {self.pontuacao_torneio})"
