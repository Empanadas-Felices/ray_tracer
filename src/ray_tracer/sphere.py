# Realizado por Angie Solís y Emilia Víquez

from rayTracer.tuples import Tuples
from rayTracer.materials import Materials
from rayTracer.transformations import Transformations
from rayTracer.matrix import Matrix

class Sphere:
  IDSeed = 0

  def __init__(self, center = Tuples(0,0,0, 1), radius = 1
               , material = None, transformation = Matrix(4,4).identity()):
    self.center = center
    self.radius = radius
    if material == None:
      self.material = Materials()
    else:
      self.material = material
    self.transform = transformation
    self.id = self.helper_seed()
    

  @staticmethod
  def helper_seed():
    Sphere.IDSeed +=1
    return Sphere.IDSeed

  def set_transform(self, transformation):
    if isinstance(transformation, Transformations):
      self.transform = transformation.matrix
    elif isinstance(transformation, Matrix): # type == matrix
      self.transform = transformation
    return self
  
  def normal_at(self, p):
    object_point = self.transform.inverse() * p
    object_normal = object_point - Tuples().Point(0,0,0)
    world_normal = self.transform.inverse().transposing() * object_normal
    world_normal.w = 0
    return world_normal.normalize()


  def __str__(self):
    return "\n\n Centro: "+ str(self.center) + "\n Radio:" +  str(self.radius) + "\n ID: " + str(self.id)+ "\n Material: " + str(self.material)+ " \n Transformacion:\n " + str(self.transform) + "\n\n"
  
  def __eq__(self, other):
    return self.center == other.center and self.radius == other.radius and self.material == other.material and self.transform == other.transform