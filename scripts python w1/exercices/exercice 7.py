n1 = float(input('what´s the width of your wall?'))
n2 = float(input('what´s the height of your wall?'))
paint = (n1 * n2) / 2
print(f'your wall has the dimension of {n1:.1f}x{n2:.1f} and it´s area is: {n1 * n2:.1f}m²')
print(f'to paint this wall you will need {paint:.1f}L of paint')
input('press enter to exit')
