import pygame
import sys


class Menu:
    def __init__(self, tela):
        self.tela = tela
        self.opcao_selecionada = 0
        self.fonte = pygame.font.SysFont(None, 48)
        self.fonte_pequena = pygame.font.SysFont(None, 24)

        # CARREGA IMAGEM DO MENU
        self.imagem_menu = pygame.image.load('./asset/fundo1.png').convert()
        self.imagem_menu = pygame.transform.scale(self.imagem_menu, (800, 400))

    def executar(self):
        from code.const import OPCOES_MENU, BRANCO, AZUL

        relogio = pygame.time.Clock()
        executando = True

        while executando:
            # DESENHA FUNDO DO MENU
            self.tela.blit(self.imagem_menu, (0, 0))

            titulo = self.fonte.render('JOGO LORRAINY', True, BRANCO)
            self.tela.blit(titulo, (400 - titulo.get_width() // 2, 80))

            # OPÇÕES DO MENU
            for i, opcao in enumerate(OPCOES_MENU):
                cor = AZUL if i == self.opcao_selecionada else BRANCO
                texto = self.fonte.render(opcao, True, cor)
                self.tela.blit(texto, (400 - texto.get_width() // 2, 180 + i * 60))

            # INSTRUÇÕES DO JOGO
            instrucoes = [
                'Controles: ESPAÇO para pular',
                'Desvie dos obstáculos!',
                '↑↓: Navegar   ENTER: Selecionar'
            ]

            for i, instrucao in enumerate(instrucoes):
                texto_instrucao = self.fonte_pequena.render(instrucao, True, BRANCO)
                self.tela.blit(texto_instrucao, (400 - texto_instrucao.get_width() // 2, 300 + i * 30))

            pygame.display.flip()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_UP:
                        self.opcao_selecionada = (self.opcao_selecionada - 1) % len(OPCOES_MENU)
                    elif evento.key == pygame.K_DOWN:
                        self.opcao_selecionada = (self.opcao_selecionada + 1) % len(OPCOES_MENU)
                    elif evento.key == pygame.K_RETURN:
                        return self.opcao_selecionada
                    elif evento.key == pygame.K_ESCAPE:
                        return 1

            relogio.tick(30)