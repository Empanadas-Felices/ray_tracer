from ray_tracer.tuples import Tuples

class Rays:
  def __init__(self, point, vector):
    self.origin = point
    self.direction = vector
  
  def position(self, num):
    result = self.origin + (self.direction * num) 
    return result
  
  def __eq__(self, other):
    return self.origin == other.origin and self.direction == other.direction
