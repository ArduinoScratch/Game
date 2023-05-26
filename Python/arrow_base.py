import pygame

def arrows(window):
    arrows1 = pygame.image.load("Image/arrows.png")
    arrows1 = pygame.transform.scale(arrows1, (300, 90))
    window.blit(arrows1, (720, 100))
    
    arrows2 = pygame.image.load("Image/arrows.png")
    arrows2 = pygame.transform.scale(arrows2, (300, 90))
    window.blit(arrows2, (300, 100))