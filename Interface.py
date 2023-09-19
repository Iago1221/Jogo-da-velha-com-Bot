import pygame, sys
import bot
class main():
    global screen
    global clock
    global running
    global jogador
    global dificuldade

    def __init__(self):
        self.tela()

    def tela(self):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((303, 303))
        self.clock = pygame.time.Clock()
        self.running = True
        self.inicio()

    def inicio(self):
        screen = self.screen
        clock = self.clock
        runInicio = self.running

        txtJogar = 'Jogar'
        fonte = pygame.font.get_default_font()
        fontesys = pygame.font.SysFont(fonte, 50)
        txtJogarTela = fontesys.render(txtJogar, 1, (0, 0, 0))

        while runInicio:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    runInicio = False
                    self.running = False
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if 82 <= mouse[0] <= 82 + 140 and 80 <= mouse[1] <= 80 + 40:
                        runInicio = False
                        self.dificuldadeEscolha()

            mouse = pygame.mouse.get_pos()

            screen.fill((255, 255, 255))

            pygame.draw.rect(screen, (170, 170, 170), [82, 80, 140, 40])

            screen.blit(txtJogarTela, (105, 82))
            pygame.display.update()

    def dificuldadeEscolha(self):
        screen = self.screen
        clock = self.clock
        runInicio = self.running

        txtDifFacil = 'Facil'
        txtDifDificil = 'Dificil'
        fonte = pygame.font.get_default_font()
        fontesys = pygame.font.SysFont(fonte, 50)
        txtDifFacilTela = fontesys.render(txtDifFacil, 1, (0, 0, 0))
        txtDifDificilTela = fontesys.render(txtDifDificil, 1, (0, 0, 0))

        while runInicio:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    runInicio = False
                    self.running = False
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if 82 <= mouse[0] <= 82 + 140 and 80 <= mouse[1] <= 80 + 40:
                        runInicio = False
                        self.setDificuldade(1)
                        self.jogo()
                    elif 82 <= mouse[0] <= 82 + 140 and 160 <= mouse[1] <= 160 + 40:
                        runInicio = False
                        self.setDificuldade(2)
                        self.jogo()

            mouse = pygame.mouse.get_pos()
            screen.fill((255, 255, 255))

            pygame.draw.rect(screen, (170, 170, 170), [82, 80, 140, 40])
            pygame.draw.rect(screen, (170, 170, 170), [82, 160, 140, 40])

            screen.blit(txtDifFacilTela, (115, 82))
            screen.blit(txtDifDificilTela, (105, 163))

            pygame.display.update()

    def jogo(self):
        screen = self.screen
        clock = self.clock
        self.jogador = 1
        runInicio = self.running

        quant_linha = 3
        quant_coluna = 3
        altura = 100
        largura = 100
        margem = 1
        grade = self.configuracaoTela(quant_linha, quant_coluna)

        while runInicio:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    runInicio = False
                    self.running = False
                    sys.exit()
                else:
                    self.defineJogadas(event, grade, largura, altura, margem)

            screen.fill((0, 0, 0))

            for linha in range(quant_linha):
                for coluna in range(quant_coluna):
                    cor = (255, 255, 255)
                    if grade[linha][coluna] == 1:
                        cor = ('purple')
                    if grade[linha][coluna] == 2:
                        cor = ('blue')

                    pygame.draw.rect(
                        screen,
                        cor,
                   [(margem + largura) * coluna + margem,
                        (margem + altura) * linha + margem, largura, altura])

            vencedor = self.verificaVencedor(grade, quant_linha, quant_coluna)

            if self.verificaEmpate(grade):
                runInicio = False
                self.fimDeJogo(vencedor)

            if vencedor != False:
                runInicio = False
                self.fimDeJogo(vencedor)

            pygame.display.update()
            clock.tick(60)

    def fimDeJogo(self, vencedor):
        screen = self.screen
        clock = self.clock
        runInicio = self.running

        if vencedor == 0:
            txtVencedor = '     Empate'
        elif vencedor == 1:
            txtVencedor = 'Você venceu!'
        elif vencedor == 2:
            txtVencedor = 'Você perdeu!'

        fonte = pygame.font.get_default_font()
        fontesys = pygame.font.SysFont(fonte, 50)
        fontesysSmall = pygame.font.SysFont(fonte, 30)
        txtVencedorTela = fontesys.render(txtVencedor, 1, (0, 0, 0))
        txtJogarNovamente = 'Jogar Novamente'
        txtJogarNovamenteTela = fontesysSmall.render(txtJogarNovamente, 1, (0, 0, 0))

        while runInicio:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    runInicio = False
                    self.running = False
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if 62 <= mouse[0] <= 62 + 140 and 160 <= mouse[1] <= 160 + 40:
                        runInicio = False
                        self.dificuldadeEscolha()

            mouse = pygame.mouse.get_pos()

            screen.fill((255, 255, 255))

            pygame.draw.rect(screen, (170, 170, 170), [62, 160, 190, 40])

            screen.blit(txtVencedorTela, (47, 52))
            screen.blit(txtJogarNovamenteTela, (72, 168))

            pygame.display.update()

    def configuracaoTela(self, quant_linha, quant_coluna):
        grade = []
        for linha in range(quant_linha):
            grade.append([])
            for coluna in range(quant_coluna):
                grade[linha].append(0)

        return grade

    def defineJogador(self, lastJogador):
        if lastJogador == 1:
            return 2
        else:
            return 1

    def verificaVencedor(self, grade, quant_linha, quant_coluna):
        vencedor = False

        if self.verificaEmpate(grade):
            vencedor = 0

        for linha in range(quant_linha):
            if grade[linha][0] != 0 and grade[linha][0] == grade[linha][1] and grade[linha][1] == grade[linha][2]:
                vencedor = grade[linha][0]

        for coluna in range(quant_coluna):
            if grade[0][coluna] != 0 and grade[0][coluna] == grade[1][coluna] and grade[1][coluna] == grade[2][coluna]:
                vencedor = grade[0][coluna]

        if grade[0][0] != 0 and grade[0][0] == grade[1][1] and grade[1][1] == grade[2][2]:
            vencedor = grade[0][0]

        if grade[0][2] != 0 and grade[0][2] == grade[1][1] and grade[1][1] == grade[2][0]:
            vencedor = grade[0][2]

        return vencedor

    def defineJogadas(self, event, grade, largura, altura, margem):
        jogador = self.jogador
        if jogador == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                coluna = mouse[0] // (largura + margem)
                linha = mouse[1] // (altura + margem)

                if grade[linha][coluna] == 0:
                    grade[linha][coluna] = jogador
                    jogador = self.defineJogador(jogador)
        else:
            while jogador == 2:
                if self.dificuldade == 1:
                    botJogada = bot.calculaJogadaDificuldadeEasy()
                else:
                    botJogada = bot.calculaJogadaDificuldadeHard(grade, 2)

                linha = botJogada[0]
                coluna = botJogada[1]

                if grade[linha][coluna] == 0:
                    grade[linha][coluna] = jogador
                    jogador = self.defineJogador(jogador)
                elif self.verificaEmpate(grade):
                    break

        self.jogador = jogador

    def setDificuldade(self, dificuldade):
        self.dificuldade = dificuldade

    def verificaEmpate(self, grade):
        for i in range(3):
            for j in range(3):
                if grade[i][j] == 0:
                    return False

        return True
