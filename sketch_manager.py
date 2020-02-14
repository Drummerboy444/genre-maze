from p5 import size, background, stroke, ellipse
from audio.manager import Manager



class SketchManager:
    def setup(self):
        self.audio_manager = Manager()
        self.audio_manager.authenticate()
        size(400, 400)

    def draw(self):
        if mouse_x > 50:
            self.audio_manager.get_sample()
            self.audio_manager.play_sample()
            stroke(255)
            ellipse((10,10),20,20)
            play = True 
        background(100)
