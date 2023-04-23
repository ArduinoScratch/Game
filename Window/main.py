import pygame


pygame.init()

window = pygame.display.set_mode([1280, 720])

pygame.display.set_caption("MiniGame")

fundo = pygame.image.load("Game/Image/stage.png")
fundo = pygame.transform.scale(fundo, (1280, 720))
personagem = pygame.image.load("Game/Image/boyfriend.png")
window.blit(fundo, (0,0))
window.blit(personagem, (720,300))
loop = True
while loop:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False



    pygame.display.update()





    pygame.display.update()