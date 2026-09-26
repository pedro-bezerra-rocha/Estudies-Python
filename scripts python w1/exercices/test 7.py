from math import sin, cos, tan, radians

a = float(input('enter a angle:'))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
          
print(f'the angle of: {a} has sine of:{s:.2f}')
print(f'the angle of: {a} has cosine of: {c:.2f}')
print(f'the angle of:{a} has tangent of: {t:.2f}')

input('press enter to exit')

