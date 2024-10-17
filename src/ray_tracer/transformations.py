from ray_tracer.matrix import Matrix

import math

class Transformations:
  def __init__(self, matrix =  Matrix(4, 4)):
    self.matrix = matrix

  def translation(self, x, y, z):
    resultado = self.matrix.identity()
    resultado.mat[0][3] = x
    resultado.mat[1][3] = y
    resultado.mat[2][3] = z
    return resultado

  def scaling(self, x, y, z):
    m_scaling = Matrix(4, 4)
    m_scaling.mat[0][0] = x
    m_scaling.mat[1][1] = y
    m_scaling.mat[2][2] = z
    m_scaling.mat[3][3] = 1
    return m_scaling

  def rotation_x(self, angle):
    m_rotation = Matrix(4, 4)
    m_rotation.mat[0][0] = 1
    m_rotation.mat[3][3] = 1
    m_rotation.mat[1][1] = math.cos(angle)
    m_rotation.mat[1][2] = -1*math.sin(angle)
    m_rotation.mat[2][1] = math.sin(angle)
    m_rotation.mat[2][2] = math.cos(angle)
    return m_rotation

  def rotation_y(self, angle):
    m_rotation = Matrix(4, 4)
    m_rotation.mat[0][0] = math.cos(angle)
    m_rotation.mat[0][2] = math.sin(angle)
    m_rotation.mat[1][1] = 1
    m_rotation.mat[2][0] = -math.sin(angle)
    m_rotation.mat[2][2] = math.cos(angle)
    m_rotation.mat[3][3] = 1
    return m_rotation

  def rotation_z(self, angle):
    m_rotation = Matrix(4, 4)
    m_rotation.mat[0][0] = math.cos(angle)
    m_rotation.mat[0][1] = -math.sin(angle)
    m_rotation.mat[1][0] = math.sin(angle)
    m_rotation.mat[1][1] = math.cos(angle)
    m_rotation.mat[2][2] = 1
    m_rotation.mat[3][3] = 1
    return m_rotation

  def shearing(self, xy, xz, yx, yz, zx, zy):
    m_shearing = self.matrix.identity()
    m_shearing.mat[0][1] = xy
    m_shearing.mat[0][2] = xz
    m_shearing.mat[1][0] = yx
    m_shearing.mat[1][2] = yz
    m_shearing.mat[2][0] = zx
    m_shearing.mat[2][1] = zy
    return m_shearing
  
  def __eq__(self, other):
    return self.matrix == other.matrix
  
  def view_transform(self, p_from, p_to, p_up):
    forward = (p_to - p_from).normalize()
    upn = p_up.normalize()
    left = forward.cross(upn)
    true_up = left.cross(forward)
    orientation = Matrix(4, 4)
    orientation.mat[0][0] = left.x
    orientation.mat[0][1] = left.y
    orientation.mat[0][2] = left.z
    orientation.mat[0][3] = 0
    orientation.mat[1][0] = true_up.x
    orientation.mat[1][1] = true_up.y
    orientation.mat[1][2] = true_up.z
    orientation.mat[1][3] = 0
    orientation.mat[2][0] = -1*forward.x
    orientation.mat[2][1] = -1*forward.y
    orientation.mat[2][2] = -1*forward.z
    orientation.mat[2][3] = 0
    orientation.mat[3][0] = 0
    orientation.mat[3][1] = 0
    orientation.mat[3][2] = 0
    orientation.mat[3][3] = 1
    return orientation * self.translation(-1*p_from.x, -1*p_from.y, -1*p_from.z)
