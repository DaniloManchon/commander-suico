import FastAPI
from commander_suico.model.jogador import Jogador

app = FastAPI()


@app.get("/jogador")
def read_root():
    return {"Menu Jogador"}

@app.post("/jogador/new")
def criar_jogador(jogador: Jogador):
    novo_jogador = Jogador(jogador.id, jogador.username, jogador.link, jogador.nome)
    return {"jogador " + novo_jogador.username + "adicionado"}
