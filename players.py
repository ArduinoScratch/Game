import pygame


def load_players(window):

    # Fundo
    fundo = pygame.image.load("Image/stage.webp")
    fundo = pygame.transform.scale(fundo, (1280, 720))
    # (X , Y)
    window.blit(fundo, (0, 0))

    # Arrows1
    arrows1 = pygame.image.load("Image/arrows.png")
    arrows1 = pygame.transform.scale(arrows1, (300, 90))
    window.blit(arrows1, (720, 100))

    # Arrows2
    arrows2 = pygame.image.load("Image/arrows.png")
    arrows2 = pygame.transform.scale(arrows2, (300, 90))
    window.blit(arrows2, (300, 100))

    # Left Arrow
    left_arrow = pygame.image.load("Image/left.png")
    left_arrow = pygame.transform.scale(left_arrow, (80, 80))
    y_left = 715
    # Right Arrow
    right_arrow = pygame.image.load("Image/right.png")
    right_arrow = pygame.transform.scale(right_arrow, (81, 91))
    y_right = 715
    window.blit(right_arrow, (525, y_right))

    # DadDearest
    dadearest = pygame.image.load("Image/dad_battle.gif")
    dadearest = pygame.transform.scale(dadearest, (200, 350))
    window.blit(dadearest, (310, 200))

    # Girfriend
    girlfriend = pygame.image.load("Image/girlfriend.gif")
    girlfriend = pygame.transform.scale(girlfriend, (330, 289))
    window.blit(girlfriend, (450, 200))

    # Boyfriend
    boyfriend = pygame.image.load("Image/boyfriend.gif")
    boyfriend = pygame.transform.scale(boyfriend, (250, 242))
    window.blit(boyfriend, (730, 300))


def load_up(window, y_up):
    up_arrow = pygame.image.load("Image/up.webp")
    up_arrow = pygame.transform.scale(up_arrow, (80, 80))
    window.blit(up_arrow, (450, y_up))

def load_down(window, y_down):
    down_arrow = pygame.image.load("Image/down.png")
    down_arrow = pygame.transform.scale(down_arrow, (80, 80))
    window.blit(down_arrow, (370, y_down))
