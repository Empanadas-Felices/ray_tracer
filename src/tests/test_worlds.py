import pytest
from ray_tracer.worlds import Worlds
from ray_tracer.rays import Rays
from ray_tracer.sphere import Sphere
from ray_tracer.intersection import Intersection
from ray_tracer.computations import Computations
from ray_tracer.tuples import Tuples
from ray_tracer.colors import Colors
from ray_tracer.lights import Lights
from ray_tracer.materials import Materials
from ray_tracer.transformations import Transformations

def test_creating_world():
    world = Worlds()
    assert len(world.objects) == 0

def test_creating_default_world():
    world = Worlds()
    world.default_world()

    light = Lights()
    point = Tuples().Point(-10, 10, -10)
    color = Colors(1, 1, 1)
    light.point_light(point, color)

    material = Materials()
    material_color = Colors(0.8, 1.0, 0.6)
    material.color = material_color
    material.diffuse = 0.7
    material.specular = 0.2

    s1 = Sphere()
    s1.material = material

    trans = Transformations()
    s2 = Sphere()
    s2.set_transform(trans.scaling(0.5, 0.5, 0.5))

    assert world.light == light
    assert s1 in world.objects
    assert s2 in world.objects

def test_intersect_world_ray():
    world = Worlds()
    world.default_world()

    origin = Tuples().Point(0, 0, -5)
    direction = Tuples().Vector(0, 0, 1)
    ray = Rays(origin, direction)
    xs = world.intersect_world(ray)

    assert len(xs) == 4
    assert xs[0].t == 4
    assert xs[1].t == 4.5
    assert xs[2].t == 5.5
    assert xs[3].t == 6

def test_shading_intersection():
    world = Worlds()
    world.default_world()

    origin = Tuples().Point(0, 0, -5)
    direction = Tuples().Vector(0, 0, 1)
    ray = Rays(origin, direction)

    shape = world.objects[0]

    i = Intersection(4, shape)
    com = Computations()
    comps = com.prepare_computations(i, ray)
    c = comps.shade_hit(world)
    col = Colors(0.38066, 0.47583, 0.2855)
    print(str(c))
    print(str(col))
    assert c == col

def test_shading_intersection_inside():
    world = Worlds()
    world.default_world()

    l = Lights()
    point = Tuples().Point(0, 0.25, 0)
    color = Colors(1, 1, 1)
    l.point_light(point, color)
    world.light = l

    origin = Tuples().Point(0, 0, 0)
    direction = Tuples().Vector(0, 0, 1)
    ray = Rays(origin, direction)

    shape = world.objects[1]

    i = Intersection(0.5, shape)
    com = Computations()
    comps = com.prepare_computations(i, ray)
    c = comps.shade_hit(world)
    col = Colors(0.90498, 0.90498, 0.90498)

    assert c == col

def test_color_ray_misses():
    world = Worlds()
    world.default_world()

    origin = Tuples().Point(0, 0, -5)
    direction = Tuples().Vector(0, 1, 0)
    ray = Rays(origin, direction)

    com = Computations()
    c = com.color_at(world, ray)
    col = Colors(0, 0, 0)

    assert c == col

def test_color_ray_hits():
    world = Worlds()
    world.default_world()

    origin = Tuples().Point(0, 0, -5)
    direction = Tuples().Vector(0, 0, 1)
    ray = Rays(origin, direction)

    com = Computations()
    c = com.color_at(world, ray)
    col = Colors(0.38066, 0.47583, 0.2855)

    assert c == col

def test_color_intersection_behind_ray():
    world = Worlds()
    world.default_world()

    outer = world.objects[0]
    outer.material.ambient = 1

    inner = world.objects[1]
    inner.material.ambient = 1

    origin = Tuples().Point(0, 0, 0.75)
    direction = Tuples().Vector(0, 0, -1)
    ray = Rays(origin, direction)

    com = Computations()
    c = com.color_at(world, ray)

    assert c == inner.material.color
       
def test_no_shadow_nothing_collinear_with_point_light():
    world = Worlds().default_world()
    p = Tuples().Point(0, 10, 0)
    assert not world.is_shadowed(p)
    
def test_shadow_with_object_between_point_light():
    world = Worlds().default_world()
    p = Tuples().Point(10, -10, 10)
    assert world.is_shadowed(p)
    
def test_no_shadow_with_object_behind_light():
    world = Worlds().default_world()
    p = Tuples().Point(-20, 20, -20)
    assert False == world.is_shadowed(p)
    
def test_no_shadow_with_object_behind_point():
    world = Worlds().default_world()
    p = Tuples().Point(-2, 2, -2)
    assert not world.is_shadowed(p)
    
def test_shade_hit_given_intersection_in_shadow():
    w = Worlds()
    l = Lights()
    l.point_light(Tuples().Point(0, 0, -10), Colors(1, 1, 1))
    w.light = l
    s1 = Sphere()
    w.objects.append(s1)
    s2 = Sphere()
    s2.transform = Transformations().translation(0, 0, 10)
    w.objects.append(s2)
    r = Rays(Tuples().Point(0, 0, 5), Tuples().Vector(0, 0, 1))
    i = Intersection(4, s2)
    comps = Computations().prepare_computations(i, r)
    c = comps.shade_hit(w)
    assert c == Colors(0.1, 0.1, 0.1)