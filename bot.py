import random
def calculaJogadaDificuldadeEasy():
    x = random.randint(0, 2)
    y = random.randint(0, 2)

    jogada = [x, y]

    return jogada

def calculaJogadaDificuldadeHard(grade, jogador):
    if verificaVitoriaBot(grade, 1):
        return -1, -1, -10
    if verificaVitoriaBot(grade, 2):
        return -1, -1, 10
    elif tabuleiroCheioBot(grade):
        return -1, -1, 0


    movimentos = []

    for i in range(3):
        for j in range(3):
            if grade[i][j] == 0:
                movimento = {}
                movimento["x"] = i
                movimento["y"] = j
                grade[i][j] = jogador
                if jogador == 1:
                    resultado = calculaJogadaDificuldadeHard(grade, 2)
                    movimento["pontuacao"] = resultado[2]
                else:
                    resultado = calculaJogadaDificuldadeHard(grade, 1)
                    movimento["pontuacao"] = resultado[2]
                grade[i][j] = 0
                movimentos.append(movimento)

    melhorMovimento = None

    if jogador == 2:
        melhorPontuacao = -10000
        for movimento in movimentos:
            if movimento["pontuacao"] > melhorPontuacao:
                melhorPontuacao = movimento["pontuacao"]
                melhorMovimento = movimento
    else:
        melhorPontuacao = 10000
        for movimento in movimentos:
            if movimento["pontuacao"] < melhorPontuacao:
                melhorPontuacao = movimento["pontuacao"]
                melhorMovimento = movimento

    return melhorMovimento["x"], melhorMovimento["y"], melhorPontuacao


def verificaVitoriaBot(tabuleiro, jogador):
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == jogador:
            return True
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == jogador:
            return True
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True
    return False

def tabuleiroCheioBot(tabuleiro):
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == 0:
                return False
    return True


