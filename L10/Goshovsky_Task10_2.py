from math import sqrt
class Point:
  def __init__(self,x,y):
    self.x = x
    self.y = y
  def __str__(self): return '(' + str(self.x) + ',' + str(self.y) + ')'

class Vector(Point):
  def __init__(self,a,b): self.a = Point(b.x-a.x,b.y-a.y)
  def getX(self): return self.a.x
  def getY(self): return self.a.y
  def __str__(self): return '(' + str(self.a.x) + ',' + str(self.a.y) + ')'
  def Len(self): return sqrt(self.a.x**2 + self.a.y**2)
  def Mul(self, k):
    self.a.x *= k
    self.a.y *= k
    return self.a
  def __mul__(self,other): return self.a.x*other.a.x + self.a.y*other.a.y

a = Vector(Point(1,2),Point(2,4))
print ('A =',a)
print ('Довжина =',a.Len())
print ('Множимо A на число 2:', a.Mul(2))
b = Vector(Point(0,0),Point(4,8))
print ('A*B = {}*{} + {}*{} = {}'.format(a.getX(),b.getX(),a.getY(),b.getY(),a*b))