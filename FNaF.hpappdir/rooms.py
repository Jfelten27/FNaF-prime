import flickertimer
import time

class Room1A:
  @staticmethod
  def getFrame(freddy, bonnie, chica, foxy):
    if bonnie.location == Room1A:
      if chica.location == Room1A:
        return 1
      else:
        return 3
    else:
      if chica.location == Room1A:
        return 0
      elif freddy.location == Room1A:
        return 4
      else:
        return 6

class Room1B:
  @staticmethod
  def getFrame(freddy, bonnie, chica, foxy):
    if freddy.location == Room1B:
      return 5
    elif bonnie.location == Room1B:
      if chica.location == Room1B and chica.lastSuccessfulMove <= bonnie.lastSuccessfulMove:
        return 3 + chica.frame
      else:
        return 1 + bonnie.frame
    elif chica.location == Room1B:
      return 3 + chica.frame
    else:
      return 0

class Room1C:
  @staticmethod
  def getFrame(freddy, bonnie, chica, foxy):
    return foxy.stage - 1

class Room2A:
  @staticmethod
  def getFrame(freddy, bonnie, chica, foxy):
    if foxy.location == Room2A:
      return min(3 + (time.lt - foxy.clock) // (1000 / 24), 34) % 34
    elif bonnie.location == Room2A:
      return 2
    else:
      return int(flickertimer.state)

class Room2B:
  @staticmethod
  def getFrame(freddy, bonnie, chica, foxy):
    return int(bonnie.location == Room2B)

class Room3:
  @staticmethod
  def getFrame(freddy, bonnie, chica, foxy):
    return int(bonnie.location == Room3)

class Room4A:
  @staticmethod
  def getFrame(freddy, bonnie, chica, foxy):
    return 0

class Room4B:
  @staticmethod
  def getFrame(freddy, bonnie, chica, foxy):
    return 0
class Room5:
  @staticmethod
  def getFrame(freddy, bonnie, chica, foxy):
    return 0

class Room6:
  @staticmethod
  def getFrame(freddy, bonnie, chica, foxy):
    return 0

class Room7:
  @staticmethod
  def getFrame(freddy, bonnie, chica, foxy):
    return 0

class Office: pass


rooms = (
  Room1A,
  Room1B,
  Room1C,
  Room2A,
  Room2B,
  Room3,
  Room4A,
  Room4B,
  Room5,
  Room6,
  Room7
)