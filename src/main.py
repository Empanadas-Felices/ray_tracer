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
                            Colors(1, 1, 1))
    
    floor = Sphere()
    floor.transform = Transformations().scaling(10, 0.01, 10)
    floor.material = Materials()
    floor.material.color = Colors(0.0627, 0.4902, 0.7333)
    floor.material.specular = 0
    
    left_wall = Sphere()
    left_wall.transform = Transformations().translation(0, 0, 5) * Transformations().rotation_y(-math.pi/4) * Transformations().rotation_x(math.pi/2) * Transformations().scaling(10, 0.01, 10)
    left_wall.material = floor.material
    
    right_wall = Sphere()
    right_wall.transform = Transformations().translation(0, 0, 5) * Transformations().rotation_y(math.pi/4) * Transformations().rotation_x(math.pi/2) * Transformations().scaling(10, 0.01, 10)
    right_wall.material = floor.material
    

    ball1 = Sphere()
    ball1.transform = Transformations().translation(0, 0.5,  0.7)* Transformations().scaling(0.8, 0.8, 0.8)
    ball1.material = Materials()
    ball1.material.color = Colors(1, 1, 1)
    ball1.material.diffuse = 0.9
    ball1.material.specular = 0.5

    ball2 = Sphere()
    ball2.transform = Transformations().translation(0, 1.5,  0.7) * Transformations().scaling(0.6, 0.6, 0.6)
    ball2.material = Materials()
    ball2.material.color = Colors(1, 1, 1)
    ball2.material.diffuse = 0.9
    ball2.material.specular = 0.5

    ball3 = Sphere()
    ball3.transform = Transformations().translation(0, 2.3,  0.7) * Transformations().scaling(0.4, 0.4, 0.4)
    ball3.material = Materials()
    ball3.material.color = Colors(1, 1, 1)
    ball3.material.diffuse = 0.9
    ball3.material.specular = 0.5
    
    
    button1 = Sphere()
    button1.transform = Transformations().translation(0, 0.5, -0.09) * Transformations().scaling(0.06, 0.06, 0.06)
    button1.material = Materials()
    button1.material.color = Colors(0.4784, 0.1882, 0)
    button1.material.diffuse = 0.9
    button1.material.specular = 0.5   

    button2 = Sphere()
    button2.transform = Transformations().translation(0, 1, -0.5) * Transformations().scaling(0.06, 0.06, 0.06)
    button2.material = Materials()
    button2.material.color = Colors(0.4784, 0.1882, 0)
    button2.material.diffuse = 0.9
    button2.material.specular = 0.5  

    button3 = Sphere()
    button3.transform = Transformations().translation(0, 1.58, -0.4) * Transformations().scaling(0.06, 0.06, 0.06)
    button3.material = Materials()
    button3.material.color = Colors(0.4784, 0.1882, 0)
    button3.material.diffuse = 0.9
    button3.material.specular = 0.5  
    

    eye1 = Sphere()
    eye1.transform = Transformations().translation(0.1, 2.25, -0.4) * Transformations().scaling(0.05, 0.05, 0.05)
    eye1.material = Materials()
    eye1.material.color = Colors(0, 0, 0)
    eye1.material.diffuse = 0.9
    eye1.material.specular = 0.5  
    
    eye2 = Sphere()
    eye2.transform = Transformations().translation(-0.1, 2.25, -0.4) * Transformations().scaling(0.05, 0.05, 0.05)
    eye2.material = Materials()
    eye2.material.color = Colors(0, 0, 0)
    eye2.material.diffuse = 0.9
    eye2.material.specular = 0.5  
    

    nose = Sphere()
    nose.transform = Transformations().translation(0, 2.1, -0.4) * Transformations().scaling(0.05, 0.05, 0.05)
    nose.material = Materials()
    nose.material.color = Colors(0.8902, 0.3294, 0.0902)
    nose.material.diffuse = 0.9
    nose.material.specular = 0.5


    armRight1 = Sphere()
    armRight1.transform = Transformations().translation(0.65, 1.5, 0.5) * Transformations().scaling(0.1, 0.1, 0.1)
    armRight1.material = Materials()
    armRight1.material.color = Colors(0.2, 0.1373, 0.1098)
    armRight1.material.diffuse = 0.9
    armRight1.material.specular = 0.5

    armRight2 = Sphere()
    armRight2.transform = Transformations().translation(0.75, 1.6, 0.4) * Transformations().scaling(0.1, 0.1, 0.1)
    armRight2.material = Materials()
    armRight2.material.color = Colors(0.2, 0.1373, 0.1098)
    armRight2.material.diffuse = 0.9
    armRight2.material.specular = 0.5

    armRight3 = Sphere()
    armRight3.transform = Transformations().translation(0.85, 1.7, 0.4) * Transformations().scaling(0.1, 0.1, 0.1)
    armRight3.material = Materials()
    armRight3.material.color = Colors(0.2, 0.1373, 0.1098)
    armRight3.material.diffuse = 0.9
    armRight3.material.specular = 0.5

    armRight4 = Sphere()
    armRight4.transform = Transformations().translation(0.95, 1.8, 0.4) * Transformations().scaling(0.1, 0.1, 0.1)
    armRight4.material = Materials()
    armRight4.material.color = Colors(0.2, 0.1373, 0.1098)
    armRight4.material.diffuse = 0.9
    armRight4.material.specular = 0.5

    armLeft1 = Sphere()
    armLeft1.transform = Transformations().translation(-0.65, 1.5, 0.5) * Transformations().scaling(0.1, 0.1, 0.1)
    armLeft1.material = Materials()
    armLeft1.material.color = Colors(0.2, 0.1373, 0.1098)
    armLeft1.material.diffuse = 0.9
    armLeft1.material.specular = 0.5

    armLeft2 = Sphere()
    armLeft2.transform = Transformations().translation(-0.75, 1.6, 0.4) * Transformations().scaling(0.1, 0.1, 0.1)
    armLeft2.material = Materials()
    armLeft2.material.color = Colors(0.2, 0.1373, 0.1098)
    armLeft2.material.diffuse = 0.9
    armLeft2.material.specular = 0.5

    armLeft3 = Sphere()
    armLeft3.transform = Transformations().translation(-0.85, 1.7, 0.4) * Transformations().scaling(0.1, 0.1, 0.1)
    armLeft3.material = Materials()
    armLeft3.material.color = Colors(0.2, 0.1373, 0.1098)
    armLeft3.material.diffuse = 0.9
    armLeft3.material.specular = 0.5

    armLeft4 = Sphere()
    armLeft4.transform = Transformations().translation(-0.95, 1.8, 0.4) * Transformations().scaling(0.1, 0.1, 0.1)
    armLeft4.material = Materials()
    armLeft4.material.color = Colors(0.2, 0.1373, 0.1098)
    armLeft4.material.diffuse = 0.9
    armLeft4.material.specular = 0.5


    scarf1 = Sphere()
    scarf1.transform = Transformations().translation(-0.4, 2, 0.2) * Transformations().scaling(0.12, 0.12, 0.12)
    scarf1.material = Materials()
    scarf1.material.color = Colors(0.749, 0.0588, 0.0588)
    scarf1.material.diffuse = 0.9
    scarf1.material.specular = 0.5

    scarf2 = Sphere()
    scarf2.transform = Transformations().translation(-0.2, 1.96, 0.2) * Transformations().scaling(0.12, 0.12, 0.12)
    scarf2.material = Materials()
    scarf2.material.color = Colors(0.749, 0.0588, 0.0588)
    scarf2.material.diffuse = 0.9
    scarf2.material.specular = 0.5

    scarf3 = Sphere()
    scarf3.transform = Transformations().translation(0, 1.94, 0.2) * Transformations().scaling(0.12, 0.12, 0.12)
    scarf3.material = Materials()
    scarf3.material.color = Colors(0.749, 0.0588, 0.0588)
    scarf3.material.diffuse = 0.9
    scarf3.material.specular = 0.5

    scarf4 = Sphere()
    scarf4.transform = Transformations().translation(0.2, 1.96, 0.2) * Transformations().scaling(0.12, 0.12, 0.12)
    scarf4.material = Materials()
    scarf4.material.color = Colors(0.749, 0.0588, 0.0588)
    scarf4.material.diffuse = 0.9
    scarf4.material.specular = 0.5

    scarf5 = Sphere()
    scarf5.transform = Transformations().translation(0.4, 2, 0.2) * Transformations().scaling(0.12, 0.12, 0.12)
    scarf5.material = Materials()
    scarf5.material.color = Colors(0.749, 0.0588, 0.0588)
    scarf5.material.diffuse = 0.9
    scarf5.material.specular = 0.5


    world.objects.append(floor)
    world.objects.append(left_wall) 
    world.objects.append(right_wall)
    world.objects.append(ball1)
    world.objects.append(ball2)
    world.objects.append(ball3)
    world.objects.append(button1)
    world.objects.append(button2)
    world.objects.append(button3)
    world.objects.append(eye1)
    world.objects.append(eye2)
    world.objects.append(nose)
    world.objects.append(armRight1)
    world.objects.append(armRight2)
    world.objects.append(armRight3)
    world.objects.append(armRight4)
    world.objects.append(armLeft1)
    world.objects.append(armLeft2)
    world.objects.append(armLeft3)
    world.objects.append(armLeft4)
    world.objects.append(scarf1)
    world.objects.append(scarf2)
    world.objects.append(scarf3)
    world.objects.append(scarf4)
    world.objects.append(scarf5)

    camera = Camera(1000, 2000, math.pi/3)
    camera.transform = Transformations().view_transform(Tuples().Point(0, 1.5, -5),
                                                        Tuples().Point(0, 1, 0),
                                                        Tuples().Vector(0, 1, 0))
    canvas = camera.render(world)
    canvas.canvas_to_ppm("../results/snowman.ppm")
    
   
if __name__ == "__main__":
    main()