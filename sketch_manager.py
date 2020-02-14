from p5 import size, background, stroke, ellipse
from audio.manager import Manager



class SketchManager:
    def setup(self):

        size(400, 400)

    def draw(self):

        background(100)

    def mouse_pressed(self):
        self.audio_manager = Manager()
        self.audio_manager.authenticate()
        self.audio_manager.get_sample()
        self.audio_manager.play_sample()

        stroke(255)
        ellipse((10,10),20,20)
        play = True 
