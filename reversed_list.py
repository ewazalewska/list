a = ["one", "two", 3]

# 1
b = a[::-1]     #[start:stop:step]
print("a", a)
print("b", b)
print("----------")


# 2
c = list(reversed(a))
print("a", a)
print("c", c)
print("----------")

# 3
d =[]
for el in a:
    d.insert(0,el)
print("a", a)
print("d", d)
print("----------")

# 4
a.reverse()
e = a
print("a", a)   # --> [3, 'two', 'one']
print("e", e)     

