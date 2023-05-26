import pygame

def load_up(window, y_up):
    up_arrow = pygame.image.load("Image/up.png")
    up_arrow = pygame.transform.scale(up_arrow, (80, 80))
    window.blit(up_arrow, (450, y_up))
    y_up -= 16
    if y_up <= -70:
        y_up = 715
    return y_up


def load_down(window, y_down):
    down_arrow = pygame.image.load("Image/down.png")
    down_arrow = pygame.transform.scale(down_arrow, (80, 80))
    window.blit(down_arrow, (370, y_down))
    y_down -= 15
    if y_down <= -70:
        y_down = 715
    return y_down


def load_right(window, y_right):
    right_arrow = pygame.image.load("Image/right.png")
    right_arrow = pygame.transform.scale(right_arrow, (81, 91))
    window.blit(right_arrow, (525, y_right))
    y_right -= 13
    if y_right <= -70:
        y_right = 715
    return y_right


def load_left(window, y_left):
    left_arrow = pygame.image.load("Image/left.png")
    left_arrow = pygame.transform.scale(left_arrow, (92, 78))
    window.blit(left_arrow, (290, y_left))
    y_left -= 19
    if y_left <= -70:
        y_left = 715
    return y_left


def load_left1(window, y_left1):
    left_arrow = pygame.image.load("Image/left.png")
    left_arrow = pygame.transform.scale(left_arrow, (92, 78))
    window.blit(left_arrow, (710, y_left1))
    y_left1 -= 14
    if y_left1 <= -70:
        y_left1 = 715
    return y_left1


def load_down1(window, y_down1):
    down_arrow = pygame.image.load("Image/down.png")
    down_arrow = pygame.transform.scale(down_arrow, (80, 80))
    window.blit(down_arrow, (790, y_down1))
    y_down1 -= 10
    if y_down1 <= -70:
        y_down1 = 715
    return y_down1


def load_up1(window, y_up1, label_result):
    up_arrow = pygame.image.load("Image/up.png")
    up_arrow = pygame.transform.scale(up_arrow, (80, 80))
    window.blit(up_arrow, (870, y_up1))
    y_up1 -= 18
    atualizar_nota("Beleza", window, label_result)
    if y_up1 <= -70:
        y_up1 = 715
    if pygame.key.get_pressed()[pygame.K_w]:
        if y_up1 > 39 and y_up1 < 151:
            atualizar_nota("1", window, label_result)
        else:
            atualizar_nota("0", window, label_result)
    return y_up1

def atualizar_nota(nota, window, label_result):
    label = label_result.render(nota, 1, (255,255,0))
    window.blit(label, (610, 650))


def load_right1(window, y_right1):
    right_arrow = pygame.image.load("Image/right.png")
    right_arrow = pygame.transform.scale(right_arrow, (81, 91))
    window.blit(right_arrow, (950, y_right1))
    y_right1 -= 23
    if y_right1 <= -70:
        y_right1 = 715
    return y_right1
