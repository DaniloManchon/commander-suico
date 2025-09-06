# Commander Suiço
## 🧩 Sistema Suíço com Elo para Partidas Free-for-All (4 Jogadores por Mesa)
Este projeto implementa um sistema de torneio baseado no **sistema suíço**, com partidas de **4 jogadores por mesa**, onde cada jogador compete **individualmente** (formato "cada um por si"). O sistema inclui:
- Organização de rodadas no estilo suíço
- Cálculo de pontos por posição
- Atualização de **rating Elo adaptado** para partidas multiplayer
- Controle de oponentes enfrentados
- Cálculo automático de **desempate Buchholz**


## 🚀 Funcionalidades
- 📊 **Classe `Jogador`**: armazena Elo, pontuação do torneio e histórico de oponentes
- 🎲 **Classe `Mesa`**: agrupa 4 jogadores, aplica pontuação e cálculo de Elo baseado na posição
- 🔁 **Sistema de emparelhamento suíço**: forma mesas balanceadas evitando confrontos repetidos
- 📈 **Cálculo de Buchholz**: desempate baseado na força dos oponentes enfrentados
- ⚖️ **Ranking final com critérios de desempate**


## 🧠 Regras de Pontuação
### Pontos por posição no torneio:

| Posição | Pontos |
|--|--|
| 1º      | 1.0    |
| 2º      | 0.5    |
| 3º      | 0.25   |
| 4º      | 0.0    |

### Resultado para cálculo de Elo:

| Posição | Resultado |
|--|--|
| 1º      | 1.0       |
| 2º      | 0.66      |
| 3º      | 0.33      |
| 4º      | 0.0       |


## 🛠 Estrutura do Código
- `Jogador`: representa um jogador, com Elo, pontuação e oponentes enfrentados.
- `Mesa`: agrupa 4 jogadores e registra resultados com atualização automática de Elo.
- `gerar_rodada_suica(jogadores)`: gera mesas para a próxima rodada com base em pontuação e histórico.
- `calcular_buchholz(jogador, todos_os_jogadores)`: calcula a soma dos pontos dos oponentes enfrentados.


## ✅ Exemplo de Uso
```python
# Criar jogadores
jogadores = [
    Jogador("Alice", 1500),
    Jogador("Bob", 1520),
    Jogador("Carol", 1480),
    Jogador("David", 1450),
    Jogador("Eve", 1510),
    Jogador("Frank", 1490),
    Jogador("Grace", 1465),
    Jogador("Heidi", 1530)
]

# Gerar rodada
mesas = gerar_rodada_suica(jogadores)

# Registrar resultados e aplicar pontuação
for mesa in mesas:
    mesa.registrar_resultado(["Alice", "Bob", "Carol", "David"])  # Ordem da colocação
    mesa.aplicar_pontuacao_e_elo()

# Calcular desempates
for jogador in jogadores:
    buchholz = calcular_buchholz(jogador, jogadores)
    print(f"{jogador.nome} - Pontos: {jogador.pontuacao_torneio}, Buchholz: {buchholz}")
```

## 📌 Critérios de Desempate (ordem sugerida)
1. Pontuação no torneio
2. Buchholz (soma dos pontos dos oponentes)
3. Elo atual
4. Sorteio (último recurso)


## 📎 Requisitos
- Python 3.7+
- Nenhuma biblioteca externa necessária


## 💡 Melhorias Futuras
- Suporte a desempates adicionais: Sonneborn-Berger, resultado direto, vitórias puras
- Exportação para CSV ou Excel
- Interface gráfica (Tkinter ou web com Flask)
- Suporte a mesas com 3 ou 5 jogadores


> Desenvolvido com o apoio do ChatGPT para facilitar a organização de torneios multiplayer com sistema justo e automatizado.