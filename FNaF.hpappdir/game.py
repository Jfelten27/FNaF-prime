from urandom import *

from gui import *
from spritesheet import *

from rooms import *

window = None

spritesheet = None

freddy = None
bonnie = None
chica = None
foxy = None
animatronics = [freddy, bonnie, chica, foxy]
startTime = 0
activeCam = -1
leftDoor = False
rightDoor = False
changeScene = False
running = True
dead = False
attacker = ''
power = 999
usage = 1

class Animatronic:
  def __init__(self):
    self.location = Room1A
    self.prevLocation = None
    self.level = 20
    self.lastMove = time.lt
    self.lastSuccessfulMove = -1
    self.interval = 999999
    self.frame = 0
    self.attacking = False
    self.path = {
      Room1A: (),
      Room1B: (),
      Room1C: (),
      Room2A: (),
      Room2B: (),
      Room3: (),
      Room4A: (),
      Room4B: (),
      Room5: (),
      Room6: (),
      Room7: (),
      Office: ()
    }

  def update(self):
    if time.lt - self.lastMove >= self.interval:
      self.lastMove += self.interval
      if self.isStalled():
        return
      if self.level >= randint(1, 20):
        self.move()
        if self.location == Room1B:
          self.frame = randint(0, 1)

  def move(self):
    global changeScene
    self.lastSuccessfulMove = self.lastMove
    self.prevLocation = self.location
    self.location = choice(self.path[self.location])
    if self.location == rooms[activeCam] or self.prevLocation == rooms[activeCam]:
      changeScene = True
    #print(self.location)

  def isStalled(self):
    return False
    return rooms[activeCam] == self.location

class Freddy(Animatronic):
  ...

class Bonnie(Animatronic):
  def __init__(self):
    super().__init__()
    self.interval = 4970
    self.interval = 999999
    self.path = {
      Room1A: (Room1B, Room5),
      Room1B: (Room2A, Room5),
      Room2A: (Room2B, Room3),
      Room2B: (Room3, Office),
      Room3: (Room2A, Office),
      Room5: (Room1B, Room2A),
      Office: (Room1B,)
    }

  def move(self):
    if self.location == Office and not leftDoor:
      self.attacking = True
    else:
      super().move()

class Chica(Animatronic):
  def __init__(self):
    super().__init__()
    self.interval = 4980
    self.interval = 999999
    self.path = {
      Room1A: (Room1B,),
      Room1B: (Room6, Room7),
      Room4A: (Room1B, Room4B),
      Room4B: (Room4A, Office),
      Room6: (Room4A, Room7),
      Room7: (Room4A, Room6),
      Office: (Room4A,)
    }

  def move(self):
    if self.location == Office and not rightDoor:
      self.attacking = True
    else:
      super().move()

class Foxy(Animatronic):
  def __init__(self):
    super().__init__()
    self.stage = 1
    self.interval = 5010
    self.interval = 1
    self.clock = -1

  def move(self):
    global power
    if self.stage == 4:
      if self.clock == -1:
        self.clock = time.lt + 2000
      if rooms[activeCam] is Room2A and self.location is not Room2A:
        self.location = Room2A
        self.clock = time.lt
      if time.lt > self.clock + 31000 // 24:
        self.location = Office
        if leftDoor:
          power -= 1
          self.location = Room1C
          self.stage = randint(1, 2)
        else:
          self.attacking = True
    else:
      self.stage += 1

def update():
  for a in animatronics:
    a.update()

def die():
  global animatronics
  global attacker
  global dead
  anims = [a for a in animatronics if a.attacking]
  anims.sort(key=lambda a: -a.lastSuccessfulMove)
  attacker = {
    Bonnie: 'bonnie',
    Chica: 'chica',
    Freddy: 'freddy2',
    Foxy: 'foxy'
  }[type(anims[0])]
  dead = True

def init():
  global spritesheet
  global window
  global animatronics
  global running
  global freddy
  global bonnie
  global chica
  global foxy
  global power
  global usage
  global startTime
  running = True
  power = 999
  usage = 1
  freddy = Freddy()
  bonnie = Bonnie()
  chica = Chica()
  foxy = Foxy()
  animatronics = [freddy, bonnie, chica, foxy]
  spritesheet = SpriteSheet(g=7, temp=9, w=3520, h=4096, xmax=3520, ymax=240)
  spritesheet.add('office.png')
  spritesheet.add('fan.png')
  spritesheet.add('door_left.png')
  spritesheet.add('door_right.png')
  spritesheet.add('switch.png')
  spritesheet.add('cam_anim.png')
  spritesheet.add('glitch.png')
  spritesheet.add('glitch_transparent.png')
  spritesheet.add('cam_map.png')
  spritesheet.add('cam_label.png')