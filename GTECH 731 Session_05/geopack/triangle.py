import geom
import math as mth

class Triangle(geom.Geom):
  
  def __init__ (self, base, height):
    super().__init__()
    self.base = base
    self.height = height
    self.type = 'triangle'

  # area method
  def area(self):
    return (self.base * 0.5 * self.height)