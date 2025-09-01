import pygame
import random


class Level:
    def __init__(self, tela):
        self.tela = tela
        from code.jogador import Jogador
        self.jogador = Jogador()
        self.obstaculos = []
        self.temporizador_obstaculo = 0
        self.pontuacao = 0
        self.game_over = False
        self.fonte = pygame.font.SysFont(None, 36)

        # CARREGA FUNDO DO JOGO
        self.fundo = pygame.image.load('./asset/fundo2.png').convert()
        self.fundo = pygame.transform.scale(self.fundo, (800, 400))

    def executar(self):
        from code.const import FPS

        relogio = pygame.time.Clock()
        executando = True

        while executando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    return self.pontuacao
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_SPACE and not self.game_over:
                        self.jogador.pular()
                    if self.game_over:
                        if evento.key == pygame.K_n:  # Reiniciar
                            return 'reiniciar'
                        elif evento.key == pygame.K_v:  # Voltar ao menu
                            return 'menu'
                        elif evento.key == pygame.K_ESCAPE:  # Sair
                            return self.pontuacao

            if not self.game_over:
                self.atualizar()

            self.desenhar()
            relogio.tick(FPS)

        return self.pontuacao

    def atualizar(self):
        self.jogador.atualizar()

        self.temporizador_obstaculo += 1
        if self.temporizador_obstaculo > 60:
            self.temporizador_obstaculo = 0
            self.adicionar_obstaculo()

        for obstaculo in self.obstaculos[:]:
            obstaculo['x'] -= 5
            rect_obstaculo = pygame.Rect(obstaculo['x'], obstaculo['y'], obstaculo['largura'], obstaculo['altura'])

            if self.jogador.rect.colliderect(rect_obstaculo):
                self.game_over = True

            if obstaculo['x'] < -50:
                self.obstaculos.remove(obstaculo)
                self.pontuacao += 1

    def adicionar_obstaculo(self):
        altura = random.randint(30, 60)
        largura = 30

        # CARREGA SPRITE DO OBSTÁCULO
        sprite = pygame.image.load('./asset/obstaculo.png').convert_alpha()
        sprite = pygame.transform.scale(sprite, (largura, altura))

        self.obstaculos.append({
            'x': 800,
            'y': 340 - altura,
            'largura': largura,
            'altura': altura,
            'sprite': sprite
        })

    def desenhar(self):
        from code.const import PRETO

        # DESENHA FUNDO
        self.tela.blit(self.fundo, (0, 0))

        pygame.draw.rect(self.tela, PRETO, (0, 340, 800, 60))

        for obstaculo in self.obstaculos:
            self.tela.blit(obstaculo['sprite'], (obstaculo['x'], obstaculo['y']))

        self.jogador.desenhar(self.tela)

        texto_pontuacao = self.fonte.render(f'Pontuação: {self.pontuacao}', True, PRETO)
        self.tela.blit(texto_pontuacao, (20, 20))


        if self.game_over:
            from code.const import VERMELHO, BRANCO, AZUL, AMARELO

            overlay = pygame.Surface((800, 400), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))  # Fundo semi-transparente
            self.tela.blit(overlay, (0, 0))

            # Título GAME OVER
            texto_game_over = self.fonte.render('FIM DE JOGO', True, VERMELHO)
            self.tela.blit(texto_game_over, (400 - texto_game_over.get_width() // 2, 100))

            # Pontuação final
            texto_pontuacao_final = self.fonte.render(f'Pontuação Final: {self.pontuacao}', True, AMARELO)
            self.tela.blit(texto_pontuacao_final, (400 - texto_pontuacao_final.get_width() // 2, 160))

            # Opções
            opcoes = [
                'N - Jogar Novamente',
                'V - Voltar ao Menu',
                'ESC - Sair do Jogo'
            ]

            for i, opcao in enumerate(opcoes):
                texto_opcao = pygame.font.SysFont(None, 32).render(opcao, True, BRANCO)
                self.tela.blit(texto_opcao, (400 - texto_opcao.get_width() // 2, 220 + i * 40))

        pygame.display.flip()
    def reiniciar(self):
        return Level(self.tela).executar()