import copy
import random
from collections import Counter

# Consider using the modules imported above.

class Hat:

  def __init__(self, **balls):
    self.contents = []
    for key in balls:
      for i in range(0, balls.get(key)):
        self.contents.append(key)
    
  def draw(self, n_balls):
    self.n_balls = n_balls
    contents = copy.copy(self.contents)
    d_balls = []
    km = len(contents)
    if self.n_balls > len(contents):
      d_balls = contents
      return d_balls
    else:
      for i in range(0, self.n_balls):
        k = random.randint(0, km-1)
        d_balls.append(contents[k])
        contents.remove(contents[k])
        km = len(contents) 
    self.contents = contents
    return d_balls

def containedInFirst(a, b):
  a_count = Counter(a)
  b_count = Counter(b)
  for key in b_count:
    if key in a_count == False:
      return False
    if b_count[key] > a_count[key]:
      return False
  return True

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  M = 0
  cont = []
  for key in expected_balls:
      for i in range(0, expected_balls.get(key)):
        cont.append(key)
  for i in range(0, num_experiments):
    hat_l = copy.copy(hat)
    b_d = hat_l.draw(num_balls_drawn)
    if containedInFirst(b_d, cont):
      M += 1
    
  
  P = M/num_experiments
  

  return(P)