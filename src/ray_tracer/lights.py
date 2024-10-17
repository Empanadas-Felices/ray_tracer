from rayTracer.tuples import Tuples
from rayTracer.colors import Colors

import math

class Lights:
  def __init__(self, position = Tuples(0, 0, 0, 1), color =  Colors(1,1,1)):
    self.intensity = color
    self.position = position

  def point_light(self, position = Tuples(0, 0, 0, 1), color =  Colors(1,1,1)):
    self.intensity = color
    self.position = position

  def lighting(self, material, light, point: Tuples, eyev, normalv, in_shadow = False):
    effective_color = material.color * light.intensity
    pos_point = light.position - point
    lightv = pos_point.normalize()
    ambient =  effective_color * material.ambient
    light_dot_normal = lightv.dot(normalv)
    diffuse = Colors(0, 0, 0) # black
    specular =  Colors(0, 0, 0) # black
    if (in_shadow == True):
      return ambient
    if light_dot_normal >= 0: # else, they are already black
      diffuse = effective_color * material.diffuse * light_dot_normal
      reflectv = (-lightv).reflect(normalv)
      reflect_dot_eye = reflectv.dot(eyev)
      if reflect_dot_eye > 0: # Else specular is already black
        factor = math.pow(reflect_dot_eye, material.shininess)
        specular = light.intensity *  material.specular *  factor
    return ambient + diffuse + specular

  def __str__(self):
    return "color " + str(self.intensity) + " position: " + str(self.position)
  
  def __eq__(self, other):
    return self.intensity == other.intensity and self.position == other.position


