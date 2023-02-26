import geom
import math as mth

class Square(geom.Geom):
  
  def __init__ (self, side):
    self.side = side
    super().__init__()
    self.type = 'square'

  # area method  
  def area(self):
     return self.side **2