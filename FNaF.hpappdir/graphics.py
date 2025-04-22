from math import *
from hpprime import *
from linalg import *

import time

from spritesheet import *

xo = 106
angles = linspace(-3*pi/16, 3*pi/16, 320)
scenes = {
  'office': 0,
  '1a': 1,
  '1b': 2,
  '1c': 3,
  '2a': 4,
  '2b': 8,
  '3': 9,
  '4a': 10,
  '4b': 11,
  '5': 12,
  '7': 13
}

def init():
  dimgrob(1, 320, 240, 0)
  dimgrob(2, 533, 240, 0)
  eval('G8:=AFiles("scenes.png")')
  eval('G5:=AFiles("jumpscares.png")')
  eval('G6:=AFiles("static.png")')

def renderScene(name, id):
  strblit2(2, 0, 0, 533, 240, 8, 533 * (id % 9), 240 * (scenes[name] + id // 9), 533, 240)

def render():
  global xo
  for i, a in enumerate(angles):
    h = 240 // cos(a)
    y = (240 - h) // 2
    strblit2(1, i, y, 1, h, 2, i + xo, 0, 1, 240)
  textout(1, 1, 1, str(int(time.get_fps() * 10) / 10), 0xffffff)