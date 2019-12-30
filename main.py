from p5 import *
from sketch_manager import SketchManager

global sketch
sketch = SketchManager()


def setup():
    sketch.setup()


def draw():
    sketch.draw()


def key_pressed():
    sketch.key_pressed(key)


run()
