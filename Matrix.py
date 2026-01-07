# máme 2 matice A, B
# A = [2	1 ; -4	-3]
# B = [2	2 ; 6	4]

# zjistěte A+B, A-B, B-A, A*B, B*A
# det A, det B, det (A+B), det (A-B), det (B-A), det (AB), det (BA)
# A transpon., B transpon.
# A^(-1)*B

import numpy as np

A = np.array([[2, 1],
             [-4, -3]])
B = np. array([[2, 2],
              [6, 4]])

# součty matic
print ("Součty:")
print (A+B , "= A+B")
print (A-B , "= A-B")
print (B-A , "= B-A")

# Součiny matic
print ("Součiny:")
print (A.dot(B), "= A*B")
print (B.dot(A), "= B*A")

# determinanty
print ("Determinanty:")
print (np.linalg.det(A), " = det A")
print (np.linalg.det(B), " = det B")
print (np.linalg.det(A+B), " = det A+B")
print (np.linalg.det(A-B), " = det B+A")
print (np.linalg.det(B-A), " = det B-A")
print (np.linalg.det(A.dot(B)), " = det A*B")
print (np.linalg.det(B.dot(A)), " = det B*A")

# transpozice
print ("Transpozice:")
print (A.transpose(), "= A transpon.")
print (B.transpose(), "= B transpon.")

# rovnice
print ("Rovnice A^(-1)*B")
x = np.linalg.inv(A)
print (x, "= A^(-1)")
print (x.dot(B), "= A^(-1)*B")