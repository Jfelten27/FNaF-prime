from hpprime import *

from animation import *

class Static(Animation):
  def __init__(self):
    super().__init__()
    self.setSourceSize(320, 240)
    self.alpha = 255
    self.add('run', range(8))
    self.play('run', looped=True)

  def setAlpha(self, a):
    self.alpha = a

  def setFrame(self, f):
    #print(f)
    self.sx = f % 4
    self.sy = f // 4

  def draw(self):
    eval('blit_p(G1, 0, 0, 320, 240, G6, {0}, {1}, {0} + 320, {1} + 240, #FF0000, {2})'.format(self.sx * 320, self.sy * 240, self.alpha))