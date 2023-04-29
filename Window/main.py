import pygame
from time import sleep
from mp3 import play_music
# Play Music
play_music()

pygame.init()

window = pygame.display.set_mode([1280, 720])

pygame.display.set_caption("Friday Night Funkin - Dadbattle")

# Fundo
fundo = pygame.image.load("Image/stage.webp")
fundo = pygame.transform.scale(fundo, (1280, 720))
# Boyfriend
boyfriend = pygame.image.load("Image/boyfriend.gif")
# Girlfriend
girlfriend = pygame.image.load("Image/girlfriend.gif")
girlfriend = pygame.transform.scale(girlfriend, (330, 289))
# DadDearest
dadearest = pygame.image.load("Image/dad_battle.gif")
dadearest = pygame.transform.scale(dadearest, (200, 350))
# Arrows1
arrows1 = pygame.image.load("Image/arrows.png")
arrows1 = pygame.transform.scale(arrows1, (300, 90))
# Arrows2
arrows2 = pygame.image.load("Image/arrows.png")
arrows2 = pygame.transform.scale(arrows2, (300, 90))
# Up Arrow
up_arrow = pygame.image.load("Image/up.webp")
up_arrow = pygame.transform.scale(up_arrow, (80, 80))
y_up = 715
# (X , Y)
window.blit(fundo, (0, 0))
window.blit(girlfriend, (450, 200))
window.blit(boyfriend, (730, 300))
window.blit(dadearest, (310, 200))
window.blit(arrows1, (720, 100))
window.blit(arrows2, (300, 100))
window.blit(up_arrow, (450, y_up))
# Loop
loop = True
while loop:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            quit()

        pygame.display.update()

repetir = True
while repetir:
    sleep(1)
    y_up = y_up-1
    if y_up <= 99:
        repetir = False
