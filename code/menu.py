#!/usr/bin/python
from pygame.font import Font
import pygame.image
from pygame import Surface, Rect

from code.const import WIN_WIDTH
import pygame


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/menu.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, text_size=None):
        pygame.mixer_music.load('./asset/som.wav')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(text_size=50, text="Jogo", text_color=(0, 0, 0), text_center_pos=((WIN_WIDTH / 2), 70))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):

        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)