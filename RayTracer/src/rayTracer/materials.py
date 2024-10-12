# Realizado por Angie Solís y Emilia Víquez

from rayTracer.tuples import Tuples
from rayTracer.colors import Colors

# from tuples import Tuples
# from colors import Colors

class Materials:
  EPSILON = 0.00001

  def __init__(self, color = Colors(1,1,1), ambient = 0.1, diffuse = 0.9, specular = 0.9, shininess = 200.0):
    self.color = color
    self.ambient = ambient
    self.diffuse = diffuse
    self.specular = specular
    self.shininess = shininess

  def __str__(self):
   return "color: " + str(self.color) + " ambient: " + str(self.ambient)  + " diffuse: " + str(self.diffuse)  + " specular: " + str(self.specular)  + " shininess: " + str(self.shininess)
    
  def equal(self, number1, number2):
    return abs(number1-number2) < self.EPSILON
  
  def __eq__(self, other):
    return self.color == other.color and self.equal(self.ambient, other.ambient) and self.equal(self.diffuse, other.diffuse) and self.equal(self.shininess,other.shininess) and self.equal(self.specular, other.specular)