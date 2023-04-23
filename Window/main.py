import pygame


pygame.init()

window = pygame.display.set_mode([1280, 720])

pygame.display.set_caption("MiniGame")

fundo = pygame.image.load("Image/stage.png")
fundo = pygame.transform.scale(fundo, (1280, 720))
boyfriend = pygame.image.load("Image/boyfriend.png")
girlfriend = pygame.image.load("Image/girlfriend.gif")
girlfriend = pygame.transform.scale(girlfriend, (330, 289))
window.blit(fundo, (0,0))
window.blit(girlfriend, (450, 200))
window.blit(boyfriend, (730,300))
loop = True
while loop:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False



    pygame.display.update()





    pygame.display.update()
