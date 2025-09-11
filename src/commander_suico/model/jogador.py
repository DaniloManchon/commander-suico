# src/commander_suico/model/jogador.py
from __future__ import annotations
from dataclasses import dataclass, field

def _empty_str_set() -> set[str]:
    return set()

@dataclass
class Jogador:
    nome: str
    elo: int = 1000
    pontuacao_torneio: float = 0.0
    # nomes dos oponentes enfrentados
    oponentes: set[str] = field(default_factory=_empty_str_set)
    

    def adicionar_oponente(self, oponente_nome: str) -> None:
        self.oponentes.add(oponente_nome)

    def atualizar_elo(self, novo_elo: int) -> None:
        self.elo = novo_elo

    def adicionar_pontos(self, pontos: float) -> None:
        self.pontuacao_torneio += pontos
