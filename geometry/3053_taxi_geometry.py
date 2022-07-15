# x^2 + y^2 = r^2
# |x| + |y| = r => y = -x + r => 4*r*r*1/2
import math

r = int(input())
pie = math.pi
print('{:.6f}'.format(r*r*pie))
print('{:.6f}'.format(r*r*2))
