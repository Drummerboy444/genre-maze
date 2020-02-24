import pygame
import urllib3
import time

'''
Takes a url link to mp3 as input and saves the mp3 data to file when instantiated.
Also contains a play() function to play the audio.
The audio playback in this file is handled by pygame, an
audio player which can be paused and volume changed.
'''

class Player:
    def __init__(self, url):
    
        self.url = url
        self.clock = pygame.time.Clock()
        http_manager = urllib3.PoolManager()
        http_object = http_manager.request("GET", self.url)
        with open("audio/temp_mp3s/temp.mp3", "wb") as output:
            output.write(http_object.data)
        self.song = "audio/temp_mp3s/temp.mp3"
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(self.song)

    def play(self):
        pygame.mixer.music.play()
    
    def pause(self):
        pygame.mixer.music.pause()

    def set_volume(self, volume):
            # volume = float(volume)
            pygame.mixer.music.set_volume(volume)

    def is_playing(self):
        return pygame.mixer.music.get_busy()









