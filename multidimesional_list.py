#macierz

import numpy
a= numpy.zeros((3, 3))
print(a)
# a[1][1]='długopis' ValueError: could not convert string to float: 'długopis'
a[1][1]=1
print(a)
