a = [1, 2, 3]
b = a
c = a.copy()
b.append(4)

print("lista a:", a, id(a))
print("lista b:", b, id(b))
print("lista c:", c, id(c))