import math
import pytest

from ray_tracer.camera import Camera
from ray_tracer.matrix import Matrix
from ray_tracer.tuples import Tuples
from ray_tracer.transformations import Transformations
from ray_tracer.worlds import Worlds
from ray_tracer.colors import Colors

EPSILON = 0.00001

def equals(a,b):
    if abs(a-b) < EPSILON:
        return True
    return False

@pytest.fixture
def sample_camera():
    c = Camera(201, 101, math.pi/2)
    return c

def test_constructing_camera():
    hsize = 160
    vsize = 120
    field_of_view = math.pi/2 
    c = Camera(hsize, vsize, field_of_view)
    m = Matrix(4,4)
    assert equals(c.hsize, hsize)
    assert equals(c.vsize, vsize)
    assert equals(c.field_of_view, field_of_view)
    assert c.transform == m.identity()
    
def test_pixel_size_horizontal():
    c = Camera(200, 125, math.pi/2)
    assert equals(c.pixel_size, 0.01) 
    
def test_pixel_size_vertical():
    c = Camera(125, 200, math.pi/2)
    assert equals(c.pixel_size, 0.01)  
    
def test_ray_through_canvas_center(sample_camera):
    r = sample_camera.ray_for_pixel(100,50)
    assert r.origin == Tuples().Point(0,0,0)
    assert r.direction == Tuples().Vector(0,0,-1)
    
def test_ray_through_canvas_corner(sample_camera):
    r = sample_camera.ray_for_pixel(0, 0)
    assert r.origin == Tuples().Point(0,0,0)
    assert r.direction == Tuples().Vector(0.66519, 0.33259, -0.66851)
    
def test_ray_through_camera_transformation(sample_camera):
    t = Transformations()
    sample_camera.transform = (t.rotation_y(math.pi/4) * t.translation(0, -2, 5))
    r = sample_camera.ray_for_pixel(100,50)
    assert r.origin == Tuples().Point(0,2,-5)
    assert r.direction == Tuples().Vector(math.sqrt(2)/2,0,-math.sqrt(2)/2)

def test_rendering_world_with_camera():
    w = Worlds().default_world()
    c = Camera(11, 11, math.pi/2)
    pfrom = Tuples().Point(0, 0, -5)
    to = Tuples().Point(0, 0, 0)
    up = Tuples().Vector(0, 1, 0)
    c.transform = Transformations().view_transform(pfrom, to, up)
    image = c.render(w)
    color = Colors(0.38066, 0.47583, 0.2855) * 255
    color.r = round(color.r)
    color.g = round(color.g)
    color.b = round(color.b)
    pixel_at = image.pixel_at(5,5)
    pixel_at.r = round(pixel_at.r)
    pixel_at.g = round(pixel_at.g)
    pixel_at.b = round(pixel_at.b)

    assert pixel_at  ==  color