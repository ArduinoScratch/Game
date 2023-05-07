import pygame
from PIL import Image

def girlfriend(window):
    girlfriend = pygame.image.load("Image/girlfriend.gif")
    girlfriend = pygame.transform.scale(girlfriend, (330, 289))
    window.blit(girlfriend, (450, 200))