import pygame
from mp3 import play_music
from girlfriend import girlfriend
from arrows import *
from boyfriend import boyfriend
from dadearest import dadearest
from stage import stage
from arrow_base import arrows
# Play Music
play_music()

pygame.init()

window = pygame.display.set_mode([1280, 720])

pygame.display.set_caption("Friday Night Funkin - Dadbattle - Teclas: ASWD")
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

stage(window)
girlfriend(window)
boyfriend(window)
dadearest(window)
arrows(window)


# Loop
loop = True
while loop:

    window.blit
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Atualizando Imagem de Fundo
    stage(window)

    # Colocando os Personagens9
    girlfriend(window)
    dadearest(window)
    arrows(window)
    boyfriend(window)

    # Carregando as Setas
    # Opponent
    y_up = load_up(window, y_up)
    y_down = load_down(window, y_down)
    y_right = load_right(window, y_right)
    y_left = load_left(window, y_left)
    # Player
    y_left1 = load_left1(window, y_left1)
    y_down1 = load_down1(window, y_down1)
    y_up1 = load_up1(window, y_up1)
    y_right1 = load_right1(window, y_right1)

    pygame.display.update()
