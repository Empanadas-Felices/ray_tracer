from ray_tracer.colors import Colors
from ray_tracer.tuples import Tuples
from ray_tracer.worlds import Worlds
from ray_tracer.sphere import Sphere
from ray_tracer.materials import Materials
from ray_tracer.transformations import Transformations
from ray_tracer.camera import Camera
import math

def main():
    world = Worlds()
    
    world.light.point_light(Tuples().Point(-10, 10, -10),
                            Colors(0.7451, 0.6588, 0.9333))
    
    floor = Sphere()
    floor.transform = Transformations().scaling(10, 0.01, 10)
    floor.material = Materials()
    floor.material.color = Colors(1, 0.9, 0.9)
    floor.material.specular = 0
    
    left_wall = Sphere()
    left_wall.transform = Transformations().translation(0, 0, 5) * Transformations().rotation_y(-math.pi/4) * Transformations().rotation_x(math.pi/2) * Transformations().scaling(10, 0.01, 10)
    left_wall.material = floor.material
    
    right_wall = Sphere()
    right_wall.transform = Transformations().translation(0, 0, 5) * Transformations().rotation_y(math.pi/4) * Transformations().rotation_x(math.pi/2) * Transformations().scaling(10, 0.01, 10)
    right_wall.material = floor.material
    
    middle = Sphere()
    middle.transform = Transformations().translation(-0.5, 1, 0.5)
    middle.material = Materials()
    middle.material.color = Colors(0.1019, 0.13725, 0.8431)
    middle.material.diffuse = 0.7
    middle.material.specular = 0.3
    
    right = Sphere()
    right.transform = Transformations().translation(1.5, 0.5, -0.5) * Transformations().scaling(0.5, 0.5, 0.5)
    right.material = Materials()
    right.material.color = Colors(0.5843, 0.4118, 0.9451)
    right.material.diffuse = 0.7
    right.material.specular = 0.3
    
    left = Sphere()
    left.transform = Transformations().translation(-1.5, 0.33, -0.75) * Transformations().scaling(0.33, 0.33, 0.33)
    left.material = Materials()
    left.material.color = Colors(0.6824, 0.6823, 0.7686)
    left.material.diffuse = 0.7
    left.material.specular = 0.3
    
    
    world.objects.append(floor)
    world.objects.append(left_wall) 
    world.objects.append(right_wall)
    world.objects.append(middle)
    world.objects.append(right)
    world.objects.append(left)

    camera = Camera(2000, 1000, math.pi/3)
    camera.transform = Transformations().view_transform(Tuples().Point(0, 1.5, -5),
                                                        Tuples().Point(0, 1, 0),
                                                        Tuples().Vector(0, 1, 0))
    canvas = camera.render(world)
    canvas.canvas_to_ppm("../results/purple_light.ppm")
    
   
if __name__ == "__main__":
    main()