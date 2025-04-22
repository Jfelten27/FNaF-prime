from gui import *

import game

class Sprite(Component):
  def __init__(self):
    super().__init__()
    self.src = ''
    self.sx = 0
    self.sy = 0
    self.sw = 0
    self.sh = 0
    self.g = 0

  def setSource(self, src, size=(0, 0)):
    self.src = src
    self.setSourceSize(*size)

  def setSourceSize(self, w, h, fit=True):
    self.sw = w
    self.sh = h
    self.setSize(w, h)

  def setGROB(self, g):
    self.g = g

  def setFrame(self, *args):
    assert len(args) in (1, 2)
    if len(args) == 1:
      self.sx = args[0]
      self.sy = 0
    elif len(args) == 2:
      self.sx, self.sy = args

  def draw(self):
    x, y = self.getPos()
    game.spritesheet.strblit2(self.g, x, y, self.w, self.h, self.src, self.sw * self.sx, self.sh * self.sy, self.sw, self.sh)