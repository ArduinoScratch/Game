import pygame

def stage(window):
    fundo = pygame.image.load("Image/stage.png")
    fundo = pygame.transform.scale(fundo, (1280, 720))
    window.blit(fundo, (0, 0))