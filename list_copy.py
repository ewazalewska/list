import copy

A = [1, 2, 3]
B = A
C = A.copy()
D = A[:]    
E = list(A)
F = copy.copy(A)
G = copy.deepcopy(A)

B.append(4)

print("lista A:", A, id(A)) #lista A: [1, 2, 3, 4] A nad B the same id
print("lista B:", B, id(B)) #lista B: [1, 2, 3, 4] 
print("lista C:", C, id(C)) #lista C: [1, 2, 3] C, D, E, F, G different id
print("lista D:", D, id(D)) #lista D: [1, 2, 3]
print("lista E:", E, id(E)) #lista E: [1, 2, 3]
print("lista F:", F, id(F)) #lista F: [1, 2, 3]
print("lista G:", G, id(G)) #lista G: [1, 2, 3]
