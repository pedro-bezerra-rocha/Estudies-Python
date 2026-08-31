n1 = float(input('what´s the width of your wall?'))
n2 = float(input('what´s the height of your wall?'))
paint = (n1 * n2) / 2
print('your wall has the dimension of {:.1f}x{:.1f} and it´s area is: {:.1f}m²' .format(n1, n2, n1 * n2))
print('to paint this wall you will need {:.1f}L of paint' .format (paint))
input('press enter to exit')
