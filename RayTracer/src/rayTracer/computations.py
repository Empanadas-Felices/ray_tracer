# Realizado por Angie Solís y Emilia Víquez

from rayTracer.tuples import Tuples
from rayTracer.lights import Lights
from rayTracer.colors import Colors

class Computations:
    EPSILON = 0.00001

    def equal(self, number1, number2):
      return abs(number1-number2) < self.EPSILON

    def __init__(self, t = 0.0, obj = None, point = None, eyev = None, normalv = None, inside = False, over_point = None):
        self.t = t
        self.object = obj
        self.point = point
        self.eyev = eyev
        self.normalv = normalv
        self.inside = inside
        self.over_point = over_point

    def prepare_computations(self, intersection, ray):
        # Compute the intersection point using the ray's direction and t-value
        point = ray.position(intersection.t)
        eyev = -ray.direction
        self.object = intersection.obj
        self.t = intersection.t
        normalv = intersection.obj.normal_at(point)
        inside = False 

        # Check if the intersection is inside the object
        if normalv.dot(eyev) < 0:
            inside = True
            normalv = -normalv

        over_point = point + normalv * self.EPSILON

        return Computations(
            t = intersection.t,
            obj = intersection.obj,
            point = point,
            eyev = eyev,
            normalv = normalv,
            inside = inside,
            over_point = over_point
        )
    
    def hit(self, intersections):
      hits = []
      for i in intersections:
        if i.t > 0:
          hits.append(i)

      # If there are no hits, return None (no hit found)
      if not hits:
          return None
      
      # Find the hit with the smallest 't' value (closest intersection)
      return min(hits, key=lambda intersection: intersection.t)

    def shade_hit(self, world):
        shadowed = world.is_shadowed(self.over_point)
        result = Lights().lighting(self.object.material, world.light, self.over_point, self.eyev, self.normalv, shadowed)
        return result

    def color_at(self, world, ray):
      intersections = world.intersect_world(ray)
      hit = self.hit(intersections)

      if hit is None:
          return Colors(0, 0, 0)  # Return black if there's no hit
      comps = self.prepare_computations(hit, ray)
      shading = comps.shade_hit(world) 
      return shading

    def __eq__(self, other):
      return self.equals(self.t,other.t) and self.object == other.obj and self.point == other.point and self.eyev == other.eyev and self.normalv ==  other.normalv and self.inside == other.inside
    
    def __str__(self):
       return "\n\nt: " + str(self.t)+ "\nobject {" + str(self.object) + "} \npoint: " +  str(self.point) + "\neyev: " +  str(self.eyev) + "\nnormalv: " + str(self.normalv) + "\ninside: " + str(self.inside) + "\n\n"
