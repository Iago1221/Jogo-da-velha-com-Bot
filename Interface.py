import pygame, sys
import bot
class main():
    global screen
    global clock
    global running
    global jogador

    def __init__(self):
        self.tela()

    def tela(self):
        pygame.init()
        self.screen = pygame.display.set_mode((303, 303))
        self.clock = pygame.time.Clock()
        self.running = True
        self.interface()

    def interface(self):
        screen = self.screen
        clock = self.clock
        self.jogador = 1

        quant_linha = 3
        quant_coluna = 3
        altura = 100
        largura = 100
        margem = 1
        grade = self.configuracaoTela(quant_linha, quant_coluna)

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
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

            self.verificaVencedor(grade, quant_linha, quant_coluna)

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()

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

    def verificaVencedor(self, grade, quant_linha, quant_coluna, running = True):
        for linha in range(quant_linha):
            if grade[linha][0] != 0 and grade[linha][0] == grade[linha][1] and grade[linha][1] == grade[linha][2]:
                running = False

        for coluna in range(quant_coluna):
            if grade[0][coluna] != 0 and grade[0][coluna] == grade[1][coluna] and grade[1][coluna] == grade[2][coluna]:
                running = False

        if grade[0][0] != 0 and grade[0][0] == grade[1][1] and grade[1][1] == grade[2][2]:
            running = False

        if grade[0][2] != 0 and grade[0][2] == grade[1][1] and grade[1][1] == grade[2][0]:
            running = False

        self.running = running

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
                botJogada = bot.calculaJogada()
                linha = botJogada[0]
                coluna = botJogada[1]

                if grade[linha][coluna] == 0:
                    grade[linha][coluna] = jogador
                    jogador = self.defineJogador(jogador)

        self.jogador = jogador

