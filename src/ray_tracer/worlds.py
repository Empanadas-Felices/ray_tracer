from ray_tracer.tuples import Tuples
from ray_tracer.colors import Colors
from ray_tracer.sphere import Sphere
from ray_tracer.lights import Lights
from ray_tracer.rays import Rays
from ray_tracer.transformations import Transformations
from ray_tracer.intersection import Intersection
from ray_tracer.materials import Materials

class Worlds:
    def __init__(self):
        self.objects = []
        self.light = Lights()

    def __eq__(self, other):
        return self.objects == other.objects and self.light == other.light

    def default_world(self):
        # Create a default world with a light source and two spheres
        self.light = Lights()
        self.light.point_light(
            Tuples().Point(-10, 10, -10),
            Colors(1, 1, 1)
        )

        material = Materials()
        material.color = Colors(0.8, 1.0, 0.6)
        material.diffuse = 0.7
        material.specular = 0.2

        s1 = Sphere()
        s1.material = material

        trans = Transformations()
        s2 = Sphere()
        s2.set_transform(trans.scaling(0.5, 0.5, 0.5))

        self.objects.append(s1)
        self.objects.append(s2)

        return self

    def intersect_world(self, ray):
        # Find and return a list of intersections between the ray and objects in the world
        intersections = []
        for obj in self.objects:
            result = Intersection().intersect(obj,ray)
            if len(result) == 2:
              intersections.append(result[0])
              intersections.append(result[1])
        intersections.sort(key = lambda x: x.t)
        return intersections

    def is_shadowed(self, point):
        v = self.light.position - point
        distance = v.magnitude()
        direction = v.normalize()
        r = Rays(point, direction)
        intersections = self.intersect_world(r)
        h = Intersection().hit(intersections)
        if h != None and h.t < distance:
            return True
        return False
