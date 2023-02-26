import geopack
from geopack import *

print('\nCircles\n')

for x in [circle.Circle(i) for i in range(2,4)]:
    #x.print_name()
    print(x.makeString())

print('\nSquares\n')

for x in [square.Square(i) for i in range(2,4)]:
    #x.print_name()
    print(x.makeString())

print('\nTriangles\n')

for x in [triangle.Triangle(i,j) for j in range(6,8) for i in range(3,5)]:
    #x.print.name()
    print(x.makeString())