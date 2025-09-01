import pygame


class Jogador:
    def __init__(self):
        self.largura = 50
        self.altura = 60
        self.x = 100
        self.y = 300
        self.velocidade = 5
        self.forca_pulo = 15
        self.pulando = False
        self.contador_pulo = 0
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)

        # CARREGA SPRITE DO JOGADOR
        self.sprite = pygame.image.load('./asset/personagem.png').convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite, (self.largura, self.altura))

    def pular(self):
        if not self.pulando:
            self.pulando = True
            self.contador_pulo = self.forca_pulo

    def atualizar(self):
        if self.pulando:
            self.y -= self.contador_pulo
            self.contador_pulo -= 1

            if self.contador_pulo < -self.forca_pulo:
                self.pulando = False
                self.contador_pulo = 0

        if self.y > 300:
            self.y = 300

        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)

    def desenhar(self, tela):
        tela.blit(self.sprite, self.rect)