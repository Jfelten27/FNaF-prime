from gui import *
from sprite import *

class Animation(Sprite):
  def __init__(self):
    super().__init__()
    self.anims = {}
    self.current = None
    self.lastFrameTime = 0
    self.frameTimer = 0
    self.frame = 0
    self.done = True
    self.hang = False
    self.paused = True
    self.finish = False
    self.setFrame(-1)

  def play(self, name=None, looped=False, hang=True):
    if name is not None:
      self.current = name
      self.frame = 0
      self.looped = looped
      self.done = False
      self.lastFrameTime = time.lt
      self.hang = hang
    self.paused = False
    self.finish = False

  def pause(self):
    self.paused = True

  def stop(self):
    self.current = None
    self.paused = True

  def add(self, name, frames, fps=24):
    self.anims[name] = (frames, fps)

  def update(self):
    super().update()
    if self.current is None:
      return
    self.frameTimer = time.lt - self.lastFrameTime
    dt = 1000 / self.anims[self.current][1]
    while self.frameTimer > dt:
      self.frameTimer -= dt
      self.lastFrameTime += dt
      if not self.paused:
        self.frame += 1
    self.finish = False
    if self.frame >= len(self.anims[self.current][0]):
      if self.looped:
        self.frame = 0
      else:
        self.frame = min(self.frame, len(self.anims[self.current][0]) - 1)
        if not self.done:
          self.finish = True
          self.done = True
    self.setFrame(self.anims[self.current][0][self.frame])

  def draw(self):
    if self.hang or not self.done:
      super().draw()