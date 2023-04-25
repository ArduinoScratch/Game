import pygame

pygame.init()

window = pygame.display.set_mode([1280, 720])

pygame.display.set_caption("MiniGame")

# Fundo
fundo = pygame.image.load("Image/stage.webp")
fundo = pygame.transform.scale(fundo, (1280, 720))
# Boyfriend
boyfriend = pygame.image.load("Image/boyfriend.png")
# Girlfriend
girlfriend = pygame.image.load("Image/girlfriend.gif")
girlfriend = pygame.transform.scale(girlfriend, (330, 289))
# DadDearest
dadearest = pygame.image.load("Image/Daddy_Dearest.webp")
dadearest = pygame.transform.scale(dadearest, (350, 350))
# Arrows1
arrows1 = pygame.image.load("Image/arrows.png")
arrows1 = pygame.transform.scale(arrows1, (300, 90))
# Arrows2
arrows2 = pygame.image.load("Image/arrows.png")
arrows2 = pygame.transform.scale(arrows2, (300, 90))
# (X , Y)
window.blit(fundo, (0, 0))
window.blit(girlfriend, (450, 200))
window.blit(boyfriend, (730, 300))
window.blit(dadearest, (250, 200))
window.blit(arrows1, (720, 100))
window.blit(arrows2, (300, 100))
# Loop
loop = True
while loop:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False

    pygame.display.update()
