# Realizado por Angie Solís y Emilia Víquez

from rayTracer.matrix import Matrix
from rayTracer.tuples import Tuples
from rayTracer.rays import Rays
from rayTracer.canvas import Canvas
from rayTracer.computations import Computations

import math

class Camera:
  def __init__(self, hsize, vsize, field_of_view):
    self.hsize = hsize
    self.vsize = vsize
    self.field_of_view = field_of_view
    self.transform = Matrix(4, 4).identity()
    self.aspect = self.hsize / self.vsize
    self.half_view = math.tan(self.field_of_view / 2)
    if self.aspect >= 1:
      self.half_width = self.half_view
      self.half_height = self.half_view / self.aspect
    else:
      self.half_width = self.half_view * self.aspect
      self.half_height = self.half_view
    self.pixel_size = (self.half_width*2)/self.hsize

  def ray_for_pixel(self, px, py):
    xoffset = (px + 0.5) * self.pixel_size
    yoffset = (py + 0.5) * self.pixel_size
    world_x = self.half_width - xoffset
    world_y = self.half_height - yoffset
    pixel = self.transform.inverse() * Tuples().Point(world_x, world_y, -1)
    origin = self.transform.inverse() * Tuples().Point(0, 0, 0)
    point = pixel - origin
    direction = point.normalize()
    return Rays(origin, direction)

  def render(self, world):
    image = Canvas(self.hsize, self.vsize)
    for y in range(0, self.vsize-1):
      for x in range(0, self.hsize - 1):
        ray = self.ray_for_pixel(x, y)
        color = Computations().color_at(world, ray)
        image.write_pixel(x, y, color)
    return image
