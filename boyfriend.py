import pygame

def boyfriend(window):
    boyfriend = pygame.image.load("Image/boyfriend.gif").convert_alpha()
    boyfriend = pygame.transform.scale(boyfriend, (250, 242))
    window.blit(boyfriend, (730, 300))