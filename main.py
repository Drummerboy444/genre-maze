from p5 import *
from sketch_manager import SketchManager

global sketch
sketch = SketchManager()


def setup():
    sketch.setup()


def draw():
    sketch.draw()


def key_pressed(key_event):
    sketch.key_pressed(key_event)


run()
