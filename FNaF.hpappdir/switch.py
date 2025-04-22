from sprite import *

class Switch(Sprite):
  keys = ((0, 5), (4, 10))
  def __init__(self):
    super().__init__()
    self.setGROB(2)
    self.side = 0
    self.door = False
    self.light = False
    self.lock = False
    self.target = None
    self.jammed = False

  def setSide(self, side):
    self.side = side

  def bind(self, target):
    self.target = target

  def update(self):
    #elif self.light == self.master.light:
    #  self.light = False if game.animatronics[1 + self.side].attacking else bool((keyboard() >> self.keys[self.side][1]) & 1)
    #  self.master.light = self.light
    if kbd.testkey(self.keys[self.side][0]) and not self.lock:
      self.door = not self.door
      self.lock = True
    if game.animatronics[1 + self.side].attacking:
      self.door = False

    if self.light and game.animatronics[1 + self.side].attacking:
      self.master.lightsOff()
    if kbd.testkey(self.keys[self.side][1]):
      state = self.light
      self.master.lightsOff()
      self.light = False if game.animatronics[1 + self.side].attacking else not state

    self.setFrame(self.light + 2 * self.door, self.side)

    if self.door != self.target.state:
      if self.door:
        self.target.play('close')
      else:
        self.target.play('open')
      self.target.state = self.door
    if self.target.done:
      self.lock = False
      self.target.play(('idle', 'active')[self.target.state], True)