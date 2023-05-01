import pygame
# Arrows

def load_up(window, y_up):
    up_arrow = pygame.image.load("Image/up.png")
    up_arrow = pygame.transform.scale(up_arrow, (80, 80))
    window.blit(up_arrow, (450, y_up))

def load_down(window, y_down):
    down_arrow = pygame.image.load("Image/down.png")
    down_arrow = pygame.transform.scale(down_arrow, (80, 80))
    window.blit(down_arrow, (370, y_down))

def load_right(window, y_right):
    right_arrow = pygame.image.load("Image/right.png")
    right_arrow = pygame.transform.scale(right_arrow, (81, 91))
    window.blit(right_arrow, (525, y_right))

def load_left(window, y_left):
    left_arrow = pygame.image.load("Image/left.png")
    left_arrow = pygame.transform.scale(left_arrow, (92, 78))
    window.blit(left_arrow, (290, y_left))

def load_left1(window, y_left1):
    left_arrow = pygame.image.load("Image/left.png")
    left_arrow = pygame.transform.scale(left_arrow, (92, 78))
    window.blit(left_arrow, (710, y_left1))

def load_down1(window, y_down1):
    down_arrow = pygame.image.load("Image/down.png")
    down_arrow = pygame.transform.scale(down_arrow, (80, 80))
    window.blit(down_arrow, (790, y_down1))

def load_up1(window, y_up1):
    up_arrow = pygame.image.load("Image/up.png")
    up_arrow = pygame.transform.scale(up_arrow, (80, 80))
    window.blit(up_arrow, (870, y_up1))

def load_right1(window, y_right1):
    right_arrow = pygame.image.load("Image/right.png")
    right_arrow = pygame.transform.scale(right_arrow, (81, 91))
    window.blit(right_arrow, (950, y_right1))