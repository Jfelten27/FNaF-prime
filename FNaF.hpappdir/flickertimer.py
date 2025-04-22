from math import *
from urandom import *

import time

state = True
lastFlicker = -1
interval = 0

def init():
  global state
  global lastFlicker
  global interval
  time.init()
  state = True
  lastFlicker = time.lt

def update():
  global interval
  global lastFlicker
  global state
  if time.lt - lastFlicker >= interval:
    state = not state
    lastFlicker = time.lt
    if state:
      minDuration = 42
      maxDuration = 2000
      seed(time.lt)
      x = log(minDuration / maxDuration) * random()
      interval = maxDuration * exp(x) #randint(42, 2000)
      #print('x:', x)
    else:
      interval = 42
    #print(interval)