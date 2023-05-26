import pygame



def play_music():
    pygame.init()

    pygame.mixer.music.load("Sounds/bopebbo.mp3")

    pygame.mixer.music.play()
