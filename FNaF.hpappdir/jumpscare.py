from hpprime import *

from gui import *

from animation import *
from static import *

import game
import graphics

class JumpscareAnimation(Animation):
  ids = {
    'bonnie': 0,
    'chica': 1,
    'foxy': 3,
    'freddy2': 5,
    'freddy1': 8
  }

  def __init__(self):
    super().__init__()
    self.setGROB(2)
    self.animStart = -1
    #animatronics = [a for a in game.animatronics if a.attacking]
    #animatronics.sort(key=lambda a: -a.lastSuccessfulMove)

  def setSource(self, name, size=(533, 240)):
    self.setSize(*size)
    self.setSourceSize(*size)
    self.animStart = self.ids[name]

  def draw(self):
    x, y = self.getPos()
    strblit2(self.g, x, y, self.w, self.h, 5, self.frame % 11 * self.sw, (self.animStart + self.frame // 11) * self.sh, self.sw, self.sh)
    #print(self.g, x, y, self.w, self.h, 5, self.frame % 11 * self.sw, (self.animStart + self.frame // 11) * self.sh, self.sw, self.sh)
    #print(self.master, self.current, self.sw, self.sh)

class Freddy1(JumpscareAnimation):
  ...

class JumpscareWindow(Frame):
  def __init__(self):
    super().__init__()
    self.type = 'jumpscare'
    self.setSize(320, 240)
    self.anim = JumpscareAnimation()
    self.anim.add('sentinel', (0,))
    self.add(self.anim)
    self.anim.play('sentinel', looped=True)
    self.statictimer = -1
    graphics.xo = 106

    self.camAnim = Animation()
    self.camAnim.setSource('cam_anim', (320, 240))
    self.camAnim.setGROB(1)
    self.camAnim.setPos(0, 0)
    self.camAnim.add('idle', (-1,))
    self.camAnim.add('open', tuple(range(11)))
    self.camAnim.add('close', tuple(range(11)[::-1]))
    #self.add(self.camAnim)
    self.camAnim.play('close', hang=False)

    self.static = Static()
    self.static.setAlpha(0)
    self.add(self.static)

  def update(self):
    if self.ret:
      self.anim.setSource(self.ret)
      self.anim.add('jumpscare', range({
        'bonnie': 11,
        'chica': 16,
        'foxy': 21,
        'freddy2': 31
      }[self.ret]))
      self.anim.play('jumpscare')
    super().update()
    self.camAnim.update()
    if self.anim.finish:
      #game.running = False
      self.static.setAlpha(255)
      self.statictimer = time.lt + 1200
      #print('e')
    #print(self.statictimer, time.lt)
    if -1 < self.statictimer < time.lt:
      self.static.pause()
      #print('e')

  def draw(self):
    super().draw()
    if self.statictimer < time.lt:
      if self.anim.done:
        #graphics.xo = 0
        graphics.renderScene('5', 4)
        eval('blit_p(G1, G2, 53, 0, 373, 240, #FF000000, {})'.format(int((time.lt - self.statictimer) / 2000 * 255)))
      else:
        graphics.render()
        self.camAnim.draw()