from p5 import size, background, stroke, ellipse
from audio.manager import Manager



class SketchManager:
    def setup(self):
        self.audio_manager = Manager()
        self.audio_manager.authenticate()
        self.audio_manager.get_sample()
        self.background = 250
        size(400, 400)

    def draw(self):
        background(mouse_x/width * 255)
        self.audio_manager.set_volume(mouse_x/width)



    def mouse_pressed(self):
        self.background = 0
        self.audio_manager.play_pause()
        stroke(255)
        ellipse((10,10),20,20)
    
    def key_pressed(self):
        self.background = 120
        self.audio_manager.new_random_genre()
        self.audio_manager.get_sample()
        self.audio_manager.play()
