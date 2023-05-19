import pygame

def girlfriend(window):
    images = "Image/Girlfriend/girlfriend14.png"
    girlfriend = pygame.image.load(images)
    girlfriend = pygame.transform.scale(girlfriend, (330, 289))
    window.blit(girlfriend, (450, 200))
