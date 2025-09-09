import random
from commander_suico.model.jogador import Jogador
from commander_suico.model.mesa import Mesa
from commander_suico.service.emparelhamento import gerar_rodada_suica
from commander_suico.service.desempates import calcular_buchholz

NUM_JOGADORES = 16
NUM_RODADAS = 3

# Criar jogadores com nomes fictícios e Elo base
nomes = [
    "Alice", "Bob", "Carol", "David", "Eve", "Frank", "Grace", "Heidi",
    "Ivan", "Judy", "Mallory", "Niaj", "Olivia", "Peggy", "Sybil", "Trent"
]

jogadores = [Jogador(nome, elo=random.randint(1400, 1600)) for nome in nomes[:NUM_JOGADORES]]

# Rodadas
for rodada in range(1, NUM_RODADAS + 1):
    print(f"\n🔁 Rodada {rodada}")

    mesas = gerar_rodada_suica(jogadores)

    for mesa in mesas:
        jogadores_na_mesa = mesa.jogadores
        nomes_ordenados = [j.nome for j in jogadores_na_mesa]
        random.shuffle(nomes_ordenados)  # Simula a ordem final

        print(f"  🎲 Mesa: {[j.nome for j in jogadores_na_mesa]}")
        print(f"     Resultado simulado: {nomes_ordenados}")

        mesa.registrar_resultado(nomes_ordenados)
        mesa.aplicar_pontuacao_e_elo()

# Ranking final com Buchholz
print("\n🏁 Ranking Final:")

# Calcular Buchholz para cada jogador
ranking_final = []
for jogador in jogadores:
    buchholz = calcular_buchholz(jogador, jogadores)
    ranking_final.append({
        'nome': jogador.nome,
        'pontos': jogador.pontuacao_torneio,
        'elo': jogador.elo,
        'buchholz': buchholz
    })

# Ordenar por pontos > buchholz > elo
ranking_ordenado = sorted(
    ranking_final,
    key=lambda x: (-x['pontos'], -x['buchholz'], -x['elo'])
)

# Mostrar ranking
for i, j in enumerate(ranking_ordenado, start=1):
    print(f"{i:2d}. {j['nome']:10} | Pontos: {j['pontos']:.2f} | Buchholz: {j['buchholz']:.2f} | Elo: {j['elo']}")
