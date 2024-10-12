# Realizado por Angie Solís y Emilia Víquez
import math

from rayTracer.matrix import Matrix
from rayTracer.tuples import Tuples
from rayTracer.sphere import Sphere
from rayTracer.rays import Rays

class Intersection:
    def __init__(self, t = 0.0, obj = Sphere()):
      self.t = t
      self.obj = obj

    def transform(self, ray, m):
      new_origin = m*ray.origin
      new_direction = m*ray.direction
      return Rays(new_origin, new_direction)

    def intersect(self, sphere, rayInitial):
      ray = self.transform(rayInitial, sphere.transform.inverse())
      result = []
      sphere_to_ray = ray.origin - sphere.center

      a = ray.direction.dot(ray.direction)
      b = 2 * (ray.direction.dot(sphere_to_ray))
      c = sphere_to_ray.dot(sphere_to_ray) - 1

      discriminant = (b ** 2) - (4 * a * c)

      if discriminant < 0:
        # No intersection
        return []

      t1 = (-b - math.sqrt(discriminant)) / (2 * a)
      t2 = (-b + math.sqrt(discriminant)) / (2 * a)

      result.append(Intersection(t1, sphere)) 
      result.append(Intersection(t2, sphere))
      return result
    
    def intersections(*args):
      xs = []
      for arg in args:
        xs.append(arg)
      for pos in range(0, len(xs)):
        posMin = pos
        for j in range(pos + 1, len(xs)):
          if xs[j].t < xs[posMin].t:
            posMin = j
        # swap
        (xs[pos], xs[posMin]) = (xs[posMin], xs[pos])
      return xs
    
    def hit(self, xs):
      posMin = 0
      foundResult = False
      for pos in range(0, len(xs)):
        if not foundResult and xs[pos].t >= 0:
          foundResult = True
          posMin = pos
        elif xs[pos].t > -1 and xs[pos].t < xs[posMin].t:
          posMin = pos
      if foundResult:
        return xs[posMin]
      else:
        return None

    def __str__(self):
      return str("Interseccion: " + str(self.t))
    
    def __eq__(self, other):
      if other == None:
        return False
      return self.t == other.t and self.obj == other.obj
