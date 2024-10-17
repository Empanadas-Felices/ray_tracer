import math

class Colors:
  EPSILON = 0.00001

  def __init__(self, r, g, b, w=0):
    self.r = r
    self.g = g
    self.b = b
    self.w = w

  def __add__(self, other):
    result = Colors(0, 0, 0, 0)
    result.r = self.r + other.r
    result.g = self.g + other.g
    result.b = self.b + other.b
    return result
  
  def __sub__(self, other):
    result = Colors(0, 0, 0, 0)
    result.r = self.r - other.r
    result.g = self.g - other.g
    result.b = self.b - other.b
    return result
  
  def __mul__(self, other):
    result = Colors(0, 0, 0, 0)
    if isinstance(other, int) or isinstance(other, float):
      result.r = self.r * other
      result.g = self.g * other
      result.b = self.b * other
    else: # is color
      result.r = self.r * other.r
      result.g = self.g * other.g
      result.b = self.b * other.b
    return result

  def __eq__(self, other):
    return(abs(self.r- other.r) < self.EPSILON and abs(self.g- other.g) < self.EPSILON  and abs(self.b - other.b) < self.EPSILON )
  
  def __str__(self):
    result = "(" + str(self.r) + ", " + str(self.g) + ", "+ str(self.b) + ", " + str(self.w) + ")"
    return result
  
