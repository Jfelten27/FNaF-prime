from urandom import *
from hpprime import *

from gui import *
from screen import *

from rooms import *
from animation import *
from static import *

import graphics
import game

"""
1a: 36, 8
1b: 27, 27
1c: 17, 53
2a: 35, 91
2b: 35, 105
3: 8, 84
4a: 70, 91
4b: 70, 105
5: -6, 35
6: 103, 78
7: 104, 38
"""

scenes = (
  '1a',
  '1b',
  '1c',
  '2a',
  '2b',
  '3',
  '4a',
  '4b',
  '5',
  '6',
  '7'
)

class CamLabel(RadioButton, Frame):
  def __init__(self):
    Frame.__init__(self)
    super().__init__()
    self.setSize(20, 13)
    self.blinkStart = -1
    self.id = -1
    self.bg = Sprite()
    self.bg.setSource('cam_label', (20, 13))
    self.bg.setFrame(0)
    self.bg.setGROB(1)
    self.add(self.bg)
    self.fg = Sprite()
    self.fg.setSource('cam_label', (20, 13))
    self.fg.setGROB(1)
    self.add(self.fg)

  def setID(self, id):
    self.fg.setFrame(id + 2)
    self.id = id

  def getID(self):
    return self.id

  def update(self):
    super().update()
    Frame.update(self)
    if self.selected:
      self.bg.setFrame(1 - (time.lt - self.blinkStart) // 1000 % 2)
    else:
      self.bg.setFrame(0)

  def draw(self):
    Frame.draw(self)

  def getPos(self):
    x, y = self.master.getPos()
    return x + self.x, y + self.y

class CamMap(RadioButtonFrame):
  def __init__(self):
    super().__init__()
    self.setSize(133, 133)
    self.sprite = Sprite()
    self.sprite.setSource('cam_map', (133, 133))
    self.sprite.setSize(133, 134)
    self.sprite.setGROB(1)
    #self.add(self.sprite)

    self.label1A = CamLabel()
    self.label1A.setPos(36, 8)
    self.label1A.setID(0)
    self.add(self.label1A)
    self.select(self.label1A)

    self.label1B = CamLabel()
    self.label1B.setPos(27, 27)
    self.label1B.setID(1)
    self.add(self.label1B)

    self.label1C = CamLabel()
    self.label1C.setPos(17, 53)
    self.label1C.setID(2)
    self.add(self.label1C)

    self.label2A = CamLabel()
    self.label2A.setPos(35, 91)
    self.label2A.setID(3)
    self.add(self.label2A)

    self.label2B = CamLabel()
    self.label2B.setPos(35, 105)
    self.label2B.setID(4)
    self.add(self.label2B)

    self.label3 = CamLabel()
    self.label3.setPos(8, 84)
    self.label3.setID(5)
    self.add(self.label3)

    self.label4A = CamLabel()
    self.label4A.setPos(70, 91)
    self.label4A.setID(6)
    self.add(self.label4A)

    self.label4B = CamLabel()
    self.label4B.setPos(70, 105)
    self.label4B.setID(7)
    self.add(self.label4B)

    self.label5 = CamLabel()
    self.label5.setPos(-6, 35)
    self.label5.setID(8)
    self.add(self.label5)

    self.label6 = CamLabel()
    self.label6.setPos(103, 78)
    self.label6.setID(9)
    self.add(self.label6)

    self.label7 = CamLabel()
    self.label7.setPos(104, 38)
    self.label7.setID(10)
    self.add(self.label7)

  def select(self, button):
    super().select(button)
    button.blinkStart = time.lt
    #graphics.xo = 0
    if self.master:
      self.master.glitchOverlay.play('run', hang=False)

  def update(self):
    super().update()
    if kbd.testkey('left'):
      self.selectPrev()
    elif kbd.testkey('right'):
      self.selectNext()
    game.activeCam = self.getSelection().getID()

  def draw(self):
    self.sprite.draw()
    super().draw()

class CamWindow(Frame):
  def __init__(self):
    super().__init__()
    self.switchconfig = SwitchConfig(init=False)
    self.setSize(320, 240)
    self.type = 'cam'
    self.xo = 0
    self.statictimer = [-1] * 11

    self.static = Static()
    self.static.setAlpha(0)
    #self.static.add('run', range(8))
    #self.static.play('run', True)
    self.add(self.static)

    self.glitchOverlay = Animation()
    self.glitchOverlay.setSource('glitch_transparent', (1, 240))
    self.glitchOverlay.setGROB(1)
    self.glitchOverlay.add('run', range(10), 60)
    self.glitchOverlay.setSize(320,240)
    #self.glitchOverlay.play('run', True)
    self.add(self.glitchOverlay)

    self.glitch = Animation()
    self.glitch.setSource('glitch', (1, 240))
    self.glitch.setGROB(1)
    self.glitch.add('run', range(7), 60)
    self.glitch.setSize(320,240)
    self.add(self.glitch)

    self.map = CamMap()
    self.map.setPos(180, 107)
    self.add(self.map)

    self.glitchOverlay.play('run', hang=False)

  def update(self):
    if self.ret:
      self.xo = self.ret
      self.statictimer = [-1] * 11
    super().update()
    activeButton = self.map.getSelection()
    seed(activeButton.getID())
    if game.changeScene:
      game.changeScene = False
      self.statictimer[activeButton.getID()] = time.lt + 5000
    f = lambda x: x if x < 5000 else 9260 - x
    y = f((.6 * time.lt - activeButton.blinkStart) % 10000)
    graphics.xo = min(213, max(0, .05 * y))
    if kbd.testkey('c') or kbd.testkey('esc') or (game.foxy.attacking):
      self.switchview('game', self.xo)

  def draw(self):
    if self.ret:
      return
    id = self.map.getSelection().getID()
    if id == 9 or time.lt < self.statictimer[id]:
      self.static.setAlpha(255)
      #print(time.lt, self.statictimer[id])
      #fillrect(2, 0, 0, 533, 240, 0, 0)
    else:
      self.static.setAlpha(0)
      graphics.renderScene(scenes[id], rooms[id].getFrame(*game.animatronics))
    graphics.render()
    super().draw()