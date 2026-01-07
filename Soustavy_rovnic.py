# reste soustavu rovnic (Petakova)

# zpusob 1 maticove 
# Ax = B -> x = inv(A)*B
# 2x+y-z = 0 // 4x+2y+z = 0 // x-y+3z = 0

from numpy import array, linalg

A = array([[2, 1, -1],
          [4, 2, 1],
          [1, -1, 3]])
B = array([0,0,0])

x = linalg.inv(A)@B
print('Reseni teto rovnice je: ', x)

# zpusob 2 (i pro nelinearni soustavy)
# 1/x + 3/y = 5 // 2/x-6/y = 6

from sympy import symbols, Eq, solve

x, y = symbols('x y')

rovnice1 = Eq(1/x+3/y,5)
rovnice2 = Eq(2/x-6/y,6)

vysledek = solve((rovnice1, rovnice2), (x,y))
print (vysledek)

