from urandom import *

from gui import *
from sprite import *
from animation import *
from door import *
from switch import *
from rooms import *

import game
import graphics
import flickertimer

class GameWindow(Frame):
  def __init__(self):
    super().__init__()
    self.switchconfig = SwitchConfig(init=False)
    self.type = 'game'
    self.light = False
    self.setSize(533, 240)

    self.fan = Animation()
    self.fan.setSource('fan', (45, 65))
    self.fan.add('run', range(3))
    self.fan.setGROB(2)
    self.fan.setPos(260, 101)
    self.fan.play('run', True)
    self.add(self.fan)

    self.leftDoor = Door()
    self.leftDoor.setSource('door_left', (74, 240))
    self.leftDoor.setPos(24, 0)
    self.add(self.leftDoor)

    self.leftSwitch = Switch()
    self.leftSwitch.setSource('switch', (31, 82))
    self.leftSwitch.setFrame(0)
    self.leftSwitch.setPos(0, 80)
    self.leftSwitch.setSide(0)
    self.leftSwitch.bind(self.leftDoor)
    self.add(self.leftSwitch)

    self.rightDoor = Door()
    self.rightDoor.setSource('door_right', (83, 240))
    self.rightDoor.setPos(421, 0)
    self.add(self.rightDoor)

    self.rightSwitch = Switch()
    self.rightSwitch.setSource('switch', (31, 82))
    self.rightSwitch.setFrame(0)
    self.rightSwitch.setPos(490, 80)
    self.rightSwitch.setSide(1)
    self.rightSwitch.bind(self.rightDoor)
    self.add(self.rightSwitch)

    self.camAnim = Animation()
    self.camAnim.setSource('cam_anim', (320, 240))
    self.camAnim.setGROB(1)
    self.camAnim.setPos(0, 0)
    self.camAnim.add('idle', (-1,))
    self.camAnim.add('open', tuple(range(11)))
    self.camAnim.add('close', tuple(range(11)[::-1]))
    self.add(self.camAnim)
    #self.camAnim.play('idle', True)

  def lightsOff(self):
    self.leftSwitch.light = False
    self.rightSwitch.light = False
    self.light = False

  def gameOver(self):
    game.die()
    self.switchview('jumpscare', game.attacker)

  def update(self):
    if self.prevwin == 'cam':
      self.camAnim.play('close', hang=False)
      graphics.xo = self.ret
      if game.bonnie.attacking or game.chica.attacking:
        self.gameOver()
    super().update()
    if game.foxy.attacking:
      self.gameOver()
    game.activeCam == -1
    game.leftDoor = self.leftDoor.state
    game.rightDoor = self.rightDoor.state
    #self.camAnim.update()
    graphics.xo = min(213, max(0, graphics.xo + pointer.dx + .3 * time.dt * (((keyboard() >> 39) & 1) - ((keyboard() >> 37) & 1))))
    if kbd.testkey('c'):
      self.camAnim.play('open')
    if self.camAnim.done and self.camAnim.current == 'open':
      self.switchview('cam', graphics.xo)

  def draw(self):
    seed(time.lt // 42)
    #game.spritesheet.blit(2, 0, 0, 'office')
    scene = 0
    if self.leftSwitch.light:
      scene = 1 + 2 * (game.animatronics[1].location == Office and not game.animatronics[1].attacking)
    elif self.rightSwitch.light:
      scene = 2 + 2 * (game.animatronics[1].location == Office and not game.animatronics[2].attacking)
    graphics.renderScene('office', scene * flickertimer.state)
    super().draw()
    #sprites.strblit2(2, 260, 101, 45, 65, 'fan', 45 * (time.lt // (1000 / 24) % 3), 0, 45, 65)
    #sprites.strblit2(2, 24, 0, 74, 240, 'door_left', 74 * (time.lt // (1000 / 24) % 14), 0, 74, 240)
    graphics.render()
    self.camAnim.draw()