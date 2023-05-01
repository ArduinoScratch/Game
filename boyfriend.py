import pygame
import random

def boyfriend(window):
    images = "Image/boyfriend.gif", "Image/boyfriend_up.png", "Image/boyfriend_left.png", "Image/boyfriend_down.png", "Image/boyfriend_up.png"
    image = random.choice(images)
    boyfriend = pygame.image.load(image)
    boyfriend = pygame.transform.scale(boyfriend, (250, 242))
    window.blit(boyfriend, (730, 300))
