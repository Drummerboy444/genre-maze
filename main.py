from p5 import *
from sketch_manager import SketchManager

global sketch
sketch = SketchManager()


def setup():
    sketch.setup()


def draw():
    sketch.draw()


run()
