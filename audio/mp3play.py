import urllib3
from pydub import AudioSegment
from pydub.playback import play

'''
Takes a url link to mp3 as input and saves the mp3 data to file when instantiated.
Also contains a play() function to play the audio.
The audio playback currently takes up the terminal - needs fix.
'''

class Player:
    def __init__(self, url):
        self.url = url
        http_manager = urllib3.PoolManager()
        http_object = http_manager.request("GET", self.url)
        with open("./test.mp3", "wb") as output:
            output.write(http_object.data)
        self.song = AudioSegment.from_mp3("./test.mp3")

    def play(self):
        play(self.song)
