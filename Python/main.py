import pygame
from Python.mp3 import play_music
from Python.girlfriend import girlfriend
from Python.arrows import *
from Python.boyfriend import boyfriend
from Python.dadearest import dadearest
from Python.stage import stage
from Python.arrow_base import arrows
# Play Music
play_music()

pygame.init()

window = pygame.display.set_mode([1280, 720])
label_result = pygame.font.SysFont("monospace", 50)

pygame.display.set_caption("Friday Night Funkin - Dadbattle - Teclas: ASWD")
y_up = 715
mudar_foto_opponente_up = False
load_up(window, y_up)
y_down = 715
mudar_foto_opponente_down = False
load_down(window, y_down)
y_right = 715
mudar_foto_opponente_right = False
load_right(window, y_right)
y_left = 715
mudar_foto_opponente_left = False
load_left(window, y_left)
y_left1 = 715
load_left1(window, y_left1)
y_down1 = 715
load_down1(window, y_down1)
y_up1 = 715
load_up1(window, y_up1, label_result)
y_right1 = 715
load_right1(window, y_right1)

stage(window)
girlfriend(window)
boyfriend(window)
dadearest(window, mudar_foto_opponente_up, mudar_foto_opponente_right, mudar_foto_opponente_down, mudar_foto_opponente_left)
arrows(window)


# Loop
loop = True
while loop:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Atualizando Imagem de Fundo
    stage(window)
    # Colocando os Personagens
    girlfriend(window)
    dadearest(window, mudar_foto_opponente_up, mudar_foto_opponente_right, mudar_foto_opponente_down, mudar_foto_opponente_left)
    arrows(window)
    boyfriend(window)

    # Carregando as Setas
    # Opponent
    # Up
    y_up = load_up(window, y_up)
    if y_up > 39 and y_up < 151:
        mudar_foto_opponente_up = True
    else:
        mudar_foto_opponente_up = False
    # Down
    y_down = load_down(window, y_down)
    if y_down > 39 and y_up < 151:
        mudar_foto_opponente_down = True
    else: mudar_foto_opponente_down = False
    # Right
    y_right = load_right(window, y_right)
    if y_right > 39 and y_right < 151:
        mudar_foto_opponente_right = True
    else:
        mudar_foto_opponente_right = False
    # Left
    y_left = load_left(window, y_left)
    if y_left > 39 and y_left < 151:
        mudar_foto_opponente_left = True
    else:
        mudar_foto_opponente_left = False
    # Player
    y_left1 = load_left1(window, y_left1)
    y_down1 = load_down1(window, y_down1)
    y_up1 = load_up1(window, y_up1, label_result)
    y_right1 = load_right1(window, y_right1)

    pygame.display.update()



