import pygame


class Jogo:
    def __init__(self):
        pygame.init()
        from code.const import LARGURA, ALTURA
        self.tela = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption('Jogo Lorrainy')

    def executar(self):
        from code.menu import Menu
        from code.nivel import Level

        # TOCA MÚSICA DE FUNDO
        pygame.mixer.music.load('./asset/som_jogo.wav')
        pygame.mixer.music.play(-1)

        executando = True

        while executando:
            menu = Menu(self.tela)
            opcao_menu = menu.executar()

            if opcao_menu == 0:  # Jogar
                while True:
                    nivel = Level(self.tela)
                    resultado = nivel.executar()

                    if resultado == 'menu':  # Voltar ao menu
                        break
                    elif resultado == 'reiniciar':  # Jogar novamente
                        continue
                    else:  # Sair ou pontuação final
                        print(f'Pontuação final: {resultado}')
                        break
            else:  # Sair
                executando = False

        pygame.mixer.music.stop()
        pygame.quit()