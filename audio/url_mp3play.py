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
        with open("temp_mp3s/temp.mp3", "wb") as output:
            output.write(http_object.data)
        self.song = "temp_mp3s/temp.mp3"
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(self.song)

    def play(self):
        pygame.mixer.music.play()
        # This while loop controls the music playback.
        # Without it the script will finish and pygame will exit.
        while pygame.mixer.music.get_busy():
            self.clock.tick(30)

# Test
# player = Player('https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3')
# player.play()



