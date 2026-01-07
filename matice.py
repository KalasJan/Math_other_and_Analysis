# jsou dány 3 matice A, B, C
# A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# B = [[6, 4, 5], [9, 7, 8], [2, 1, 3]]
# C = [[2, 1], [5, 4], [8, 7]]
# Vypočítejte: A+B, B-A, C-1, 3*A, A*B, B*A, A*C, det A, inverzní A, inv B, A^2, hodnost A,  C transform.

from numpy import array, linalg

A = array ([[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]])
B = array ([[6, 4, 5],
            [9, 7, 8], 
            [2, 1, 3]])
C = array ([[2, 1],
            [5, 4],
            [8, 7]])

print('A+B =', A+B)
print('B-A =', B-A)
print('C-1 =', C-1)
print('3*A =', 3*A)
print('A*B =', A*B) #násobení po prvcích
print('A*C =', A@C) # maticové násobení
print('DET A =', linalg.det(A))print('INV A =', linalg.inv(A))
print('INV B =', linalg.inv(B))
print('hodnost A =', linalg.matrix_rank(A))
print('C trans. =', C.T)

