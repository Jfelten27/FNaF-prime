from urandom import *
from hpprime import *

import sys
sys.path.append('.')
sys.path.append('../primelibs.hpappdir')

from gui import *
from screen import *

from gamewindow import *
from camwindow import *
from jumpscare import *

import graphics
import time
import kbd
import pointer
import game
import flickertimer

graphics.init()
time.init()
kbd.init()
game.init()
flickertimer.init()
game.startTime = time.lt
#sprites.init()

screen = Screen()

screen.add(GameWindow())
screen.add(CamWindow())
screen.add(JumpscareWindow())

def render():
  screen.draw()
  blit(0,0,0,1)

def update():
  kbd.update()
  pointer.update()
  game.update()
  screen.update()
  time.update()
  flickertimer.update()

game.startTime = time.lt
while game.running:
  #seed(time.lt // 42)
  update()
  render()

print('done')