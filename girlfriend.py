import pygame

def girlfriend(window):
    girlfriend = pygame.image.load("Image/girlfriend.gif")
    girlfriend = pygame.transform.scale(girlfriend, (330, 289))
    window.blit(girlfriend, (450, 200))