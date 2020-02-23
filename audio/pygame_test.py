import pygame

def load():
    pygame.mixer.init()
    pygame.mixer.music.load('temp_mp3s/temp.mp3')

def play(sound):
    pygame.mixer.music.play()
    h = input("enter to stop")


s = load()
play(s)
