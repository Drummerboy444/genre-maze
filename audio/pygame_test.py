import pygame

def load():
    pygame.mixer.init()
    pygame.mixer.music.load('temp_mp3s/temp.mp3')

def play(sound):
    pygame.mixer.music.play()

def set_volume(volume):
    pygame.mixer.music.set_volume(volume)



s = load()
play(s)
while True:
    volume = input("set new volume between 0 and 1")
    
    if volume.isnumeric:
        volume = float(volume)
        set_volume(float(volume))
    else:
        print("exiting")
        break
