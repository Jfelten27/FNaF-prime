from animation import *

class Door(Animation):
  def __init__(self):
    super().__init__()
    self.state = False
    self.setGROB(2)
    self.add('idle', (0,))
    self.add('active', (15,))
    self.add('open', tuple(range(0, 16)[::-1]))
    self.add('close', tuple(range(0, 16)))
    self.play('idle', True)

  def update(self):
    super().update()
    #if self.done:
    #  self.play(('active', 'idle')[self.state], True)