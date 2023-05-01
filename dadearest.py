import pygame

def dadearest(window):
    dadearest = pygame.image.load("Image/dad_battle.gif")
    dadearest = pygame.transform.scale(dadearest, (200, 350))
    window.blit(dadearest, (310, 200))