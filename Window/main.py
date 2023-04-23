import pygame


pygame.init()

window = pygame.display.set_mode([1280, 720])

pygame.display.set_caption("MiniGame")

fundo = pygame.image.load("Image/stage.png")
fundo = pygame.transform.scale(fundo, (1280, 720))
boyfriend = pygame.image.load("Image/boyfriend.png")
girlfriend = pygame.image.load("Image/girlfriend.gif")
girlfriend = pygame.transform.scale(girlfriend, (330, 289))
dadearest = pygame.image.load("Image/Daddy_Dearest.webp")
dadearest = pygame.transform.scale(dadearest, (350,350))
arrows1 = pygame.image.load("Image/arrows.png")
arrows1 = pygame.transform.scale(arrows1, (300,100))
arrows2 = pygame.image.load("Image/arrows.png")
arrows2 = pygame.transform.scale(arrows2, (300,100))
window.blit(fundo, (0,0))
window.blit(girlfriend, (450, 200))
window.blit(boyfriend, (730,300))
window.blit(dadearest, (250,200))
window.blit(arrows1, (720,100))
window.blit(arrows2, (300,100))
loop = True
while loop:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False



    pygame.display.update()





    pygame.display.update()
