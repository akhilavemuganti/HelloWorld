#Inheritance

from Area.square import Square
from Area.triangle import Triangle

s1 = Square()
s1.set_value(5,10)
print("Area of square is ", s1.area())

t1 = Triangle()
t1.set_value(10,6)
print("Area of triangle is ", t1.area())