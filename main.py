import pygame
from mp3 import play_music
from players import *
# Play Music
play_music()

pygame.init()

window = pygame.display.set_mode([1280, 720])

pygame.display.set_caption("Friday Night Funkin - Dadbattle - Teclas: ASWD")

load_players(window)
y_up = 715
load_up(window, y_up)
y_down = 715
load_down(window, y_down)
y_right = 715
load_right(window, y_right)
y_left = 715
load_left(window, y_left)
y_left1 = 715
load_left1(window, y_left1)
y_down1 = 715
load_down1(window, y_down1)
y_up1 = 715
load_up1(window, y_up1)
y_right1 = 715
load_right1(window, y_right1)


# Loop
loop = True
while loop:

    window.blit
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Movimentação
    # Oppponent
    y_up -= 5
    if y_up <= -70:
        y_up = 715
    y_down -= 7
    if y_down <= -70:
        y_down = 715
    y_right -= 9
    if y_right <= -70:
        y_right = 715
    y_left -= 11
    if y_left <= -70:
        y_left = 715
    #Player
    y_left1 -= 5
    if y_left1 <= -70:
        y_left1 = 715
    y_down1 -= 7
    if y_down1 <= -70:
        y_down1 = 715
    y_up1 -= 9
    if y_up1 <= -70:
        y_up1 = 715
    y_right1 -= 11
    if y_right1 <= -70:
        y_right1 = 715


    # Atualizando Imagem de Fundo
    load_players(window)

    # Carregando as Setas
    # Opponent
    load_up(window, y_up)
    load_down(window, y_down)
    load_right(window, y_right)
    load_left(window, y_left)
    # Player
    load_left1(window, y_left1)
    load_down1(window, y_down1)
    load_up1(window, y_up1)
    load_right1(window, y_right1)

    pygame.display.update()
