import pygame
from time import sleep
from mp3 import play_music
from players import *
# Play Music
play_music()

pygame.init()

window = pygame.display.set_mode([1280, 720])

pygame.display.set_caption("Friday Night Funkin - Dadbattle")

load_players(window)
y_up = 715
load_up(window, y_up)
y_down = 715
load_down(window, y_down) 


# Loop
loop = True
while loop:

    window.blit
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Movimentação
    y_up -= 5
    y_down -= 7

    # Atualizando Imagem de Fundo
    load_players(window)

    # Carregando as Setas
    load_up(window, y_up)
    load_down(window, y_down)

    pygame.display.update()
