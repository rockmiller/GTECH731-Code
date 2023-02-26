import random
import math as mth

class Geom():
  geomType = 'Generic Geometry Type'
  
  # Constructor of the class: used to initialize an object
  def __init__(self):
    # Check out the names and the faker packages for random names
    self.name = random.choice(['Bill','Sally','Tamica','Josh','Lammar','Hussain'])
    self.color = random.choice(['BLUE', 'RED', 'PURPLE'])
    self.type = "geometry"
  
  # This is a method that all children will inherit. 
  # In other words, all children will have this method without explicitly defining it. 

  def print_name(self):
    print('My name is',self.name, ', a', self.type, ', and my color is',self.color)

  # Another method: why we can call self.area without defining it here?
  def makeString(self):
    return f"Name: {self.name}, Type: {self.type}, Color: {self.color}, Area: {self.area()}"
  
  def print_geom(g):
    print(g.makeString())

class Circle(Geom):
  
  def __init__ (self, radius):
    self.radius = radius
    super().__init__()
    self.type = 'circle'

  # area method  
  def area(self):
     return mth.pi * self.radius **2
  
class Square(Geom):
  
  def __init__ (self,side):
    super().__init__()
    self.side = side
    self.type = "square"

  # area method  
  def area(self):
     return self.side **2
  
class Triangle(Geom):
  
  def __init__ (self,base,height):
    super().__init__()
    self.base = base
    self.height = height
    self.type = "triangle"

  # area method for the triangle class  
  def area(self):
     return self.base * 0.5 * self.height