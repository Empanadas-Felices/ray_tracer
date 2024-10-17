import math

class Tuples:
  EPSILON = 0.00001

  def __init__(self, x = 0, y = 0, z = 0, w = 0):  
    self.x = x
    self.y = y
    self.z = z
    self.w = w

  def Point(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
    self.w = 1
    return self

  def Vector(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
    self.w = 0
    return self

  def isPoint(self):
    return self.w == 1

  def isVector(self):
    return self.w == 0

  def __add__(self, other):
    new_tuple = Tuples (0.0, 0.0, 0.0, 0.0)
    new_tuple.x = self.x + other.x
    new_tuple.y = self.y + other.y
    new_tuple.z = self.z + other.z
    new_tuple.w = self.w + other.w
    if (new_tuple.w < 0.0):
      new_tuple.w = 0
    if (new_tuple.w > 1.0):
      new_tuple.w = 1
    return new_tuple
  
  def __sub__(self, other):
    new_tuple = Tuples ()
    new_tuple.x = self.x - other.x
    new_tuple.y = self.y - other.y
    new_tuple.z = self.z - other.z
    new_tuple.w = self.w - other.w
    if (new_tuple.w < 0.0):
      new_tuple.w = 0
    if (new_tuple.w > 1.0):
      new_tuple.w = 1
    return new_tuple

  def __mul__(self, number):
    new_tuple = Tuples(number*self.x, number*self.y, number*self.z, number*self.w)
    return new_tuple

  def __truediv__(self, number):
    return self.__mul__(1/number)

  def dot(self, other):
    result = self.x*other.x + self.y*other.y + self.z*other.z + self.w*other.w
    return result

  def cross(self, other):
    new_tuple = Tuples ()
    new_tuple.x = self.y*other.z - self.z*other.y
    new_tuple.y = self.z*other.x - self.x*other.z
    new_tuple.z = self.x*other.y - self.y*other.x
    return new_tuple
  
  def __neg__(self):
    return Tuples (-1*self.x, -1*self.y, -1*self.z, -1*self.w)
  
  def magnitude(self):
    result = self.x**2+ self.y**2 + self.z**2 + self.w**2
    return math.sqrt(result)
  
  def normalize(self):
    return self * ((1/self.magnitude()))

  def __eq__(self, other):
    return (self.equal(self.x, other.x) and self.equal(self.y, other.y) and self.equal(self.z, other.z) and self.equal(self.w, other.w))

  def equal(self, number1, number2):
    return abs(number1-number2) < self.EPSILON

  def __str__(self):
    result = "(" + str(self.x) + ", " + str(self.y) + ", "+ str(self.z) + ", " + str(self.w) + ")"
    return result
  
  def reflect(self, other):
    return (self - other * 2 * self.dot(other))