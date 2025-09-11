from __future__ import annotations
from dataclasses import dataclass
from typing import Final
import statistics
from src.commander_suico.model.jogador import Jogador

@dataclass
class Mesa:
    jogadores: list[Jogador]

    def __post_init__(self) -> None:
        if len(self.jogadores) != 4:
            raise ValueError("Uma mesa deve ter exatamente 4 jogadores.")

    # posições: nome -> posição (1, 2, 3, 4)
    def registrar_resultado(self, posicoes: dict[str, int]) -> list[Jogador]:
        # 1) validações básicas
        if len(posicoes) != 4:
            raise ValueError("Deve haver exatamente 4 posições registradas.")

        nomes_mesa = {j.nome for j in self.jogadores}
        nomes_recebidos = set(posicoes.keys())

        # nomes desconhecidos
        desconhecidos = nomes_recebidos - nomes_mesa
        if desconhecidos:
            raise ValueError(f"Nomes não pertencem à mesa: {sorted(desconhecidos)}")

        # nomes faltando
        faltando = nomes_mesa - nomes_recebidos
        if faltando:
            raise ValueError(f"Faltam posições para: {sorted(faltando)}")

        # posições devem ser exatamente {1,2,3,4}
        valores = list(posicoes.values())
        if sorted(valores) != [1, 2, 3, 4]:
            raise ValueError("As posições devem ser 1, 2, 3 e 4 sem repetição.")

        # 2) ordenar por posição (1º → 4º)
        ordenados = sorted(posicoes.items(), key=lambda kv: kv[1])  # [(nome, pos), ...]
        nome_para_jogador = {j.nome: j for j in self.jogadores}
        self.resultado_posicoes = [nome_para_jogador[nome] for nome, _ in ordenados]

        # 3) atualizar oponentes (todos contra todos na mesa)
        for jogador in self.jogadores:
            for oponente in self.jogadores:
                if oponente is not jogador:
                    jogador.adicionar_oponente(oponente.nome)

        # 4) retorna a lista já ordenada (opcional mas útil)
        return self.resultado_posicoes

    def aplicar_pontuacao_e_elo(self, k: float = 32.0) -> None:
        """
        Aplica pontuação de torneio e atualiza ELO com base no resultado da mesa (1º → 4º).
        Requer que `resultado_posicoes` já esteja preenchido por `registrar_resultado`.
        """
        if not self.resultado_posicoes or len(self.resultado_posicoes) != 4:
            raise ValueError("Resultados ainda não foram registrados corretamente.")

        # Pontuação de torneio (exemplo com frações)
        PONTOS_TORNEIO: Final[tuple[float, float, float, float]] = (1.0, 0.5, 0.25, 0.0)

        # Resultado esperado do “match” 4p (heurística): 1.0, 2/3, 1/3, 0.0
        # Se preferir, mantenha 0.66/0.33 (mas fracionário “exato” ajuda na doc/tipos)
        RESULTADO_ELO: Final[tuple[float, float, float, float]] = (1.0, 2/3, 1/3, 0.0)

        for idx, jogador in enumerate(self.resultado_posicoes):
            pontos: float = PONTOS_TORNEIO[idx]
            resultado: float = RESULTADO_ELO[idx]

            # oponentes = os demais da mesa
            oponentes: list[Jogador] = [j for j in self.jogadores if j is not jogador]

            # média de ELO dos oponentes (float)
            elo_medio: float = statistics.mean(j.elo for j in oponentes)

            # ELO esperado (modelo clássico)
            esperado: float = 1.0 / (1.0 + 10.0 ** ((elo_medio - jogador.elo) / 400.0))
            delta: float = k * (resultado - esperado)
            novo_elo: int = round(jogador.elo + delta)  # int

            jogador.atualizar_elo(novo_elo)
            jogador.adicionar_pontos(pontos)

    def __repr__(self) -> str:
        nomes = ", ".join(j.nome for j in self.jogadores)
        return f"Mesa({nomes})"