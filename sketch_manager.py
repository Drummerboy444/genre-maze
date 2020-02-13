from p5 import size, background, stroke, ellipse
from audio.manager import Manager



class SketchManager:
    def setup(self):
        audio_manager = Manager()
        Manager.authenticate
        Manager.play_sample
        size(400, 400)

    def draw(self):
        if mouse_x > 50:
            stroke(255)
            ellipse((10,10),20,20)
            play = True 
        background(100)
