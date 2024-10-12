# Realizado por Angie Solís y Emilia Víquez

from rayTracer.colors import Colors

class Canvas:
  def __init__(self, cols, rows, color = Colors(0,0,0,0)):
    self.rows = rows
    self.cols = cols
    self.matrix = []
    for r in range(0, rows):
      self.matrix.append([Colors(color.r, color.g, color.b)])
      for c in range(0, cols-1):
        self.matrix[r].append(Colors(color.r, color.g, color.b, 0))

  def height(self):
    return self.rows
  
  def width(self):
    return self.cols

  def write_pixel(self, y, x, color):
    self.matrix[x][y].r = color.r
    self.matrix[x][y].g = color.g
    self.matrix[x][y].b = color.b

  def pixel_at(self, y, x):
    return (self.matrix[x][y]*255)
  
  def count_digits(number):
    if number < 10:
      return 1
    if number < 100:
      return 2
    else: # max is 255
      return 3

  def adapt_value(self, value, wpr, ppm_file):
    adapted_value = int(round((value * 255)))
    if adapted_value < 0:
      adapted_value = 0
    else:
      if adapted_value > 255:
        adapted_value = 255
    
    wpr += Canvas.count_digits(adapted_value)
    if wpr > 70:
      wpr = 0
      ppm_file.write("\n" + str(adapted_value) + " ")
    else:
      ppm_file.write(str(adapted_value) + " ")
    wpr += 1 # space could be the 70th char  
    return wpr

  def canvas_to_ppm(self, file_name):
    ppm_file = open(file_name, "w")
    ppm_file.write("P3\n" + str(self.cols) + " " 
                   + str(self.rows) + "\n255\n")
    wpr = 0 # words per row
    for r in range(0, self.rows):
      for c in range (0, self.cols):
        # Red
        wpr = self.adapt_value(self.matrix[r][c].r, wpr, ppm_file)
        
        # Green
        wpr = self.adapt_value(self.matrix[r][c].g, wpr, ppm_file)

        # Blue
        wpr = self.adapt_value(self.matrix[r][c].b, wpr, ppm_file)
      # end of row: insert new end line char
      ppm_file.write("\n")
      wpr = 0
